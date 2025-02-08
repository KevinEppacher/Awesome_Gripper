import os
import launch
import launch_ros.actions
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.substitutions import Command, LaunchConfiguration, PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    # Paths
    gripper_urdf_path = os.path.join(get_package_share_directory('gripper_moveit_config'), 'urdf', 'gripper.urdf.xacro')
    moveit_config_path = get_package_share_directory('gripper_moveit_config')

    return LaunchDescription([
        DeclareLaunchArgument('use_sim_time', default_value='true', description='Use simulation time'),

        # Start MoveIt and RViz
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                [os.path.join(moveit_config_path, 'launch', 'demo.launch.py')]
            ),
            launch_arguments={'use_sim_time': 'true'}.items(),
        ),

        # Start ros2_control controllers
        Node(
            package='controller_manager',
            executable='spawner',
            arguments=['joint_state_broadcaster', '--controller-manager', '/controller_manager'],
            output='screen'
        ),

        Node(
            package='controller_manager',
            executable='spawner',
            arguments=['gripper_planning_group_controller', '--controller-manager', '/controller_manager'],
            output='screen'
        ),
    ])
