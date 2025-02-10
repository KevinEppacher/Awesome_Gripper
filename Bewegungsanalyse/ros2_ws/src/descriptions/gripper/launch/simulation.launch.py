import os
import launch
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.substitutions import FindPackageShare
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    # Declare arguments
    gui_arg = DeclareLaunchArgument(
        name='gui',
        default_value='true',
        description='Launch Gazebo with GUI'
    )
    use_sim_time = DeclareLaunchArgument(
        'use_sim_time',
        default_value='true',
        description='Use simulation time'
    )

    # Get package paths
    gripper_description_path = get_package_share_directory('gripper')
    gripper_moveit_path = get_package_share_directory('gripper_moveit_config')

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

    # Start MoveIt and RViz
    moveit_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            PathJoinSubstitution([gripper_moveit_path, 'launch', 'demo.launch.py'])
        ),
        launch_arguments={'use_sim_time': 'true'}.items(),
    )

    # Start `ros2_control` in Gazebo
    ros2_control_node = Node(
        package='controller_manager',
        executable='ros2_control_node',
        parameters=[os.path.join(gripper_description_path, 'config', 'ros2_controllers.yaml')],
        output='screen'
    )

    # Spawn controllers for MoveIt to communicate with Gazebo
    spawner_joint_state_broadcaster = Node(
        package='controller_manager',
        executable='spawner',
        arguments=['joint_state_broadcaster', '--controller-manager', '/controller_manager'],
        output='screen'
    )

    spawner_trajectory_controller = Node(
        package='controller_manager',
        executable='spawner',
        arguments=['gripper_trajectory_controller', '--controller-manager', '/controller_manager'],
        output='screen'
    )

    return LaunchDescription([
        gui_arg,
        use_sim_time,
        gazebo_launch,
        spawn_gripper,
        moveit_launch,
        ros2_control_node,
        spawner_joint_state_broadcaster,
        spawner_trajectory_controller,
    ])
