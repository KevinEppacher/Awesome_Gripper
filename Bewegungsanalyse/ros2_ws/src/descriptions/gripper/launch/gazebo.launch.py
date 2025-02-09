import os
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import Command, PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare
from launch_ros.parameter_descriptions import ParameterValue

def generate_launch_description():
    package_name = "gripper"

    # Correctly find the Xacro file
    urdf_xacro_file = PathJoinSubstitution([
        FindPackageShare(package_name),
        "urdf",
        "gripper.urdf.xacro"
    ])

    return LaunchDescription([
        # Robot State Publisher
        Node(
            package="robot_state_publisher",
            executable="robot_state_publisher",
            name="robot_state_publisher",
            output="screen",
            parameters=[{
                "robot_description": ParameterValue(Command([urdf_xacro_file]), value_type=str)
            }]
        ),

        # Spawn the model in Gazebo
        Node(
            package="gazebo_ros",
            executable="spawn_entity.py",
            arguments=[
                "-entity", "gripper",
                "-topic", "robot_description"
            ],
            output="screen"
        )
    ])