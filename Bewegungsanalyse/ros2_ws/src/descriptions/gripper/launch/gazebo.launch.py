import os
import launch
import launch_ros.actions
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription, ExecuteProcess
from launch_ros.actions import Node
from launch.substitutions import Command, LaunchConfiguration, PathJoinSubstitution
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    # Get URDF and world file
    gripper_urdf_path = os.path.join(get_package_share_directory('gripper_moveit_config'), 'config', 'gripper.urdf.xacro')
    world_path = os.path.join(get_package_share_directory('gripper_moveit_config'), 'worlds', 'empty.world')

    return LaunchDescription([
        DeclareLaunchArgument('use_sim_time', default_value='true', description='Use simulation time'),
        
        # Launch Gazebo
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource([os.path.join(get_package_share_directory('gazebo_ros'), 'launch', 'gazebo.launch.py')]),
            launch_arguments={'world': world_path, 'use_sim_time': 'true'}.items(),
        ),

        # Spawn gripper in Gazebo
        Node(
            package='gazebo_ros',
            executable='spawn_entity.py',
            arguments=['-entity', 'gripper', '-file', gripper_urdf_path, '-x', '0', '-y', '0', '-z', '1'],
            output='screen'
        ),

        # Start ros2_control (if needed)
        Node(
            package='controller_manager',
            executable='ros2_control_node',
            parameters=[{
                'robot_description': Command(['xacro ', gripper_urdf_path]),
                'use_sim_time': True,
            }],
            output='screen'
        ),
    ])
