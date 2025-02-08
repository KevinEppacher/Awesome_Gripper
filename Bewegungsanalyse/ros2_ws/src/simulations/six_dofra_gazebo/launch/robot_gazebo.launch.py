import os
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    # Pakete und Pfade abrufen
    package_path = get_package_share_directory("gazebo_sim")
    gazebo_world_launch = os.path.join(package_path,"launch","gazebo_world.launch.py")

    # URDF-Datei
    urdf_file = os.path.join(package_path, "urdf", "six_dofra_gazebo.xacro")

    # Launch-Argumente definieren
    gazebo_gui_arg = DeclareLaunchArgument("gazebo_gui", default_value="true", description="Start Gazebo GUI")
    paused_arg = DeclareLaunchArgument("paused", default_value="false", description="Start Gazebo paused")
    world_name_arg = DeclareLaunchArgument("world_name", default_value="worlds/empty.world", description="Gazebo world file")

    x_arg = DeclareLaunchArgument("x", default_value="0.0", description="X Position")
    y_arg = DeclareLaunchArgument("y", default_value="0.0", description="Y Position")
    z_arg = DeclareLaunchArgument("z", default_value="0.8", description="Z Position")

    # 1️ **Starte die Gazebo-Welt**
    gazebo_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(gazebo_world_launch),
        launch_arguments={
            "gui": LaunchConfiguration("gazebo_gui"),
            "paused": LaunchConfiguration("paused"),
            "world": LaunchConfiguration("world_name"),
        }.items(),
    )

    return LaunchDescription([
        gazebo_gui_arg,
        paused_arg,
        world_name_arg,
        x_arg,
        y_arg,
        z_arg,
        gazebo_launch,
    ])
