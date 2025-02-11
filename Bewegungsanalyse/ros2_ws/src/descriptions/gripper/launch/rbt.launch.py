import os
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription, TimerAction
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import Command
from ament_index_python.packages import get_package_share_directory
from launch.substitutions import PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare
from launch_ros.parameter_descriptions import ParameterValue


def generate_launch_description():
    # Path to the Xacro file
    xacro_file = os.path.join(
        get_package_share_directory('gripper'),
        'urdf',
        'gripper.urdf.xacro'
    )

    # Generate URDF from Xacro
    robot_description = {'robot_description': ParameterValue(Command(['xacro ', xacro_file]), value_type=str)}

    # Path to the controller YAML file
    controller_config = os.path.join(
        get_package_share_directory('gripper'),
        'config',
        'gazebo_ros2_control.yaml'  # Ensure this matches your file name
    )

    # Robot State Publisher (Publishes `robot_description`)
    rsp_node = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        parameters=[robot_description],
        output='screen'
    )

    # Joint State Publisher GUI (Allows slider control in RViz)
    joint_state_publisher_node = Node(
        package='joint_state_publisher_gui',
        executable='joint_state_publisher_gui',
        output='screen'
    )

    # Launch RViz2 with the appropriate config file
    rviz_config_file = PathJoinSubstitution(
        [FindPackageShare('gripper'), 'cfg', 'rviz_config.rviz']
    )
    rviz_node = Node(
        package='rviz2',
        executable='rviz2',
        output='screen'
    )

    # Gazebo (Ensures Gazebo starts before loading controllers)
    gazebo_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            os.path.join(
                get_package_share_directory('gazebo_ros'),
                'launch',
                'gazebo.launch.py'
            )
        ]),
    )

    # Spawn Entity in Gazebo (Must happen after Gazebo is running)
    spawn_entity = TimerAction(
        period=5.0,  # Wait for Gazebo to fully start
        actions=[
            Node(
                package='gazebo_ros',
                executable='spawn_entity.py',
                arguments=[
                    '-topic', 'robot_description',
                    '-entity', 'gripper'
                ],
                output='screen'
            )
        ]
    )

    # Controller Manager (Must start after `robot_description` is available)
    controller_manager_node = TimerAction(
        period=6.0,  # Ensures `robot_state_publisher` is running before controllers start
        actions=[
            Node(
                package='controller_manager',
                executable='ros2_control_node',
                parameters=[controller_config],  # Load controller config
                output='screen'
            )
        ]
    )

    # Spawn the Joint Position Controller (Must start after Controller Manager)
    spawner_node = TimerAction(
        period=8.0,  # Wait for Controller Manager to be ready
        actions=[
            Node(
                package='controller_manager',
                executable='spawner',
                arguments=['gripper_position_controller'],  # Make sure this matches your YAML config
                output='screen'
            )
        ]
    )

    return LaunchDescription([
        rsp_node,                     # Publishes robot_description
        joint_state_publisher_node,   # Adds sliders for joint control
        gazebo_launch,                # Starts Gazebo
        spawn_entity,                 # Spawns robot in Gazebo
        controller_manager_node,       # Loads controllers
        spawner_node,                  # Starts position controller
        rviz_node                      # Launches RViz2
    ])