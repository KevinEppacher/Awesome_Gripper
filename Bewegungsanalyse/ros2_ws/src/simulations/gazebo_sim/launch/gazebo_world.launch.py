import os
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():
    # Declare launch arguments
    gazebo_gui_arg = DeclareLaunchArgument(
        "gazebo_gui", default_value="true", description="Start Gazebo GUI"
    )

    paused_arg = DeclareLaunchArgument(
        "paused", default_value="false", description="Start Gazebo paused"
    )

    world_name_arg = DeclareLaunchArgument(
        "world_name", default_value="worlds/empty.world", description="Gazebo world file"
    )

    # Get Gazebo launch file path
    gazebo_ros_pkg = get_package_share_directory("gazebo_ros")
    gazebo_launch_file = os.path.join(gazebo_ros_pkg, "launch", "gazebo.launch.py")

    # Include Gazebo launch
    gazebo_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(gazebo_launch_file),
        launch_arguments=[
            ("gui", LaunchConfiguration("gazebo_gui")),
            ("paused", LaunchConfiguration("paused")),
            ("world", LaunchConfiguration("world_name")),
        ],
    )

    return LaunchDescription([
        gazebo_gui_arg,
        paused_arg,
        world_name_arg,
        gazebo_launch,
    ])
