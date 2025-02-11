import os
import launch
import launch_ros
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription, TimerAction
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution, Command
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.substitutions import FindPackageShare
from launch_ros.parameter_descriptions import ParameterValue
from ament_index_python.packages import get_package_share_directory
import launch_ros
from launch_ros.actions import Node


def generate_launch_description():
    # Declare launch arguments
    gui_arg = DeclareLaunchArgument(
        name='gui',
        default_value='true',
        description='Launch Gazebo with GUI'
    )
    use_sim_time = DeclareLaunchArgument(
        name='use_sim_time',
        default_value='true',
        description='Use simulation time'
    )

    # Get package paths
    gripper_description_path = get_package_share_directory('gripper')
    gripper_moveit_path = get_package_share_directory('gripper_moveit_config')

    path_to_urdf = os.path.join(gripper_description_path, "urdf", "gripper.urdf.xacro")

    # Paths for URDF/Xacro and ros2_control config
    xacro_file = PathJoinSubstitution([FindPackageShare('gripper'), 'urdf', 'gripper.urdf.xacro'])
    ros2_control_config = PathJoinSubstitution([FindPackageShare("gripper"), "config", "ros2_controllers.yaml"])

    # Start Gazebo with empty world
    gazebo_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            PathJoinSubstitution([FindPackageShare('gazebo_ros'), 'launch', 'gazebo.launch.py'])
        ),
        launch_arguments={'gui': LaunchConfiguration('gui'), 'pause': 'true'}.items(),
    )

    # Spawn gripper in Gazebo
    spawn_gripper = Node(
        package='gazebo_ros',
        executable='spawn_entity.py',
        name='spawn_gripper',
        arguments=['-topic', '/robot_description', '-entity', 'gripper', '-z', '0.5', '-unpause'],
        output='screen',
    )

    # Joint State Publisher (for publishing joint states)
    joint_state_publisher = Node(
        package="joint_state_publisher",
        executable="joint_state_publisher",
        name="joint_state_publisher",
        output="screen"
    )

    # Joint State Publisher GUI (adds delay to prevent launch race conditions)
    joint_state_publisher_gui = TimerAction(
        period=3.0,  # Add a delay before starting
        actions=[Node(
            package="joint_state_publisher_gui",
            executable="joint_state_publisher_gui",
            name="joint_state_publisher_gui",
            output="screen"
        )]
    )

    # Robot State Publisher (broadcasts TF frames based on URDF)
    # Robot State Publisher - publishes TF transformations based on joint angles
    robot_state_publisher = launch_ros.actions.Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        output="screen",
        parameters=[{
            "robot_description": ParameterValue(
                Command(['xacro ', str(path_to_urdf)]),  # Convert Xacro to URDF
                value_type=str 
            )
        }]
    )

    # Start MoveIt with RViz
    moveit_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            PathJoinSubstitution([gripper_moveit_path, 'launch', 'demo.launch.py'])
        ),
        launch_arguments={'use_sim_time': 'true'}.items(),
    )

    # Start ros2_control in Gazebo
    ros2_control_node = Node(
        package='controller_manager',
        executable='ros2_control_node',
        parameters=[ros2_control_config],
        output="screen",
    )

    # Spawn controllers for MoveIt to communicate with Gazebo
    spawner_joint_state_broadcaster = Node(
        package='controller_manager',
        executable='spawner',
        arguments=['joint_state_broadcaster'],
        output='screen'
    )

    spawner_trajectory_controller = Node(
        package='controller_manager',
        executable='spawner',
        arguments=['gripper_trajectory_controller'],
        output='screen'
    )

    return LaunchDescription([
        gui_arg,
        use_sim_time,
        gazebo_launch,
        spawn_gripper,
        joint_state_publisher,
        joint_state_publisher_gui,
        robot_state_publisher,
        moveit_launch,
        ros2_control_node,
        spawner_joint_state_broadcaster,
        spawner_trajectory_controller,
    ])
