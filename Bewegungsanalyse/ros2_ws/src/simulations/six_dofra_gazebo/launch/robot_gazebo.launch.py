import os
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.actions import TimerAction
from launch_ros.actions import Node
from launch.substitutions import Command, FindExecutable
from ament_index_python.packages import get_package_share_directory
from launch_ros.parameter_descriptions import ParameterValue
import launch_ros.actions  # Hier wird `launch_ros` definiert
from launch_ros.actions import Node

def generate_launch_description():
    # Xacro-Datei definieren
    # six_dofra_config_pkg = get_package_share_directory("six_dofra_gazebo")
    six_dofra_config_pkg = get_package_share_directory("six_dofra_config")
    gazebo_pkg = get_package_share_directory("gazebo_sim")

    # path_to_urdf = os.path.join(six_dofra_config_pkg, "urdf", "six_dofra_gazebo.xacro")
    path_to_urdf = os.path.join(six_dofra_config_pkg, "config", "urdf_6_dofra_v3.urdf.xacro")


    # # Gazebo starten
    # gazebo = IncludeLaunchDescription(
    #     PythonLaunchDescriptionSource(
    #         os.path.join(gazebo_pkg, "launch", "gazebo_world.launch.py")
    #     )
    # )

    # Joint State Publisher
    joint_state_publisher = Node(
        package="joint_state_publisher",
        executable="joint_state_publisher",
        name="joint_state_publisher",
        output="screen"
    )

    # Robot State Publisher
    robot_state_publisher = launch_ros.actions.Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        output="screen",
        parameters=[{
            "robot_description": ParameterValue(
                Command(['xacro ', str(path_to_urdf)]),
                value_type=str 
            )
        }]
    )

    # Spawn den Roboter, aber erst nach 5 Sekunden Verzögerung (damit Gazebo sicher läuft)
    spawn_entity = TimerAction(
        period=5.0,
        actions=[Node(
            package="gazebo_ros",
            executable="spawn_entity.py",
            arguments=[
                "-entity", "six_dofra",
                "-topic", "robot_description"
            ],
            output="screen"
        )]
    )

    return LaunchDescription([
        # gazebo,
        joint_state_publisher,
        robot_state_publisher,
        # spawn_entity
    ])
