import os
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import Command
from ament_index_python.packages import get_package_share_directory
from launch.substitutions import PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare
import launch_ros.descriptions
from launch.actions import ExecuteProcess


def generate_launch_description():
    # Path to the Xacro file
    xacro_file = os.path.join(
        get_package_share_directory('six_dofra_description'),
        'urdf',
        'six_dofra_description.urdf.xacro'
    )

    # Process the Xacro file to generate URDF
    robot_description = {'robot_description': Command(['xacro ', xacro_file])}

    # Path to the controller YAML file
    controller_config = os.path.join(
        get_package_share_directory('six_dofra_config'),
        'config',
        'ros2_controllers.yaml'  # Ensure this matches your file name
    )

    # Robot State Publisher (publishes TF and robot_description)
    robot_description_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        parameters=[robot_description],
        output='screen'
    )

    # Joint State Publisher GUI (allows slider control in RViz)
    joint_state_publisher_node = Node(
        package='joint_state_publisher_gui',
        executable='joint_state_publisher_gui',
        output='screen'
    )

    # Controller Manager (loads the control configuration)
    controller_manager_node = Node(
        package='controller_manager',
        executable='ros2_control_node',
        parameters=[robot_description, controller_config],  # Load controller config
        output='screen'
    )

    # Spawn the joint position controller
    spawner_node = Node(
        package='controller_manager',
        executable='spawner',
        arguments=['joint_position_controller'],  # Make sure this matches your YAML config
        output='screen'
    )

    # # Add Gazebo back
    # gazebo_launch = IncludeLaunchDescription(
    #     PythonLaunchDescriptionSource([
    #         os.path.join(
    #             get_package_share_directory('gazebo_ros'),
    #             'launch',
    #             'gazebo.launch.py'
    #         )
    #     ]),
    # )

    gazebo_server = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            PathJoinSubstitution([
                FindPackageShare('gazebo_ros'),
                'launch',
                'gzserver.launch.py'
            ])
        ]),
        launch_arguments={
            'pause': 'true'
        }.items()
    )

    gazebo_client = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            PathJoinSubstitution([
                FindPackageShare('gazebo_ros'),
                'launch',
                'gzclient.launch.py'
            ])
        ])
    )


    # Add Gazebo Spawn Entity
    spawn_entity = Node(
        package='gazebo_ros',
        executable='spawn_entity.py',
        arguments=[
            '-topic', 'robot_description',
            '-entity', 'six_dofra_description'
        ],
        output='screen'
    )

    load_joint_state_broadcaster = ExecuteProcess(
        cmd=['ros2', 'control', 'load_controller',
             '--set-state', 'active', 'joint_state_broadcaster'],
        output='screen')

    load_joint_trajectory_controller = ExecuteProcess(
        cmd=['ros2', 'control', 'load_controller', '--set-state',
             'active', 'joint_trajectory_controller'],
        output='screen')

    return LaunchDescription([
        robot_description_publisher,                      # Publishes robot_description
        joint_state_publisher_node,    # Adds sliders for joint control
        controller_manager_node,        # Loads controllers
        spawner_node,                   # Spawns position controller
        # gazebo_launch,                  # Launches Gazebo
        gazebo_server,
        gazebo_client,
        spawn_entity,                     # Spawns the robot in Gazebo
        load_joint_state_broadcaster,    # Load the joint state broadcaster
        load_joint_trajectory_controller  # Load the joint trajectory controller
    ])

