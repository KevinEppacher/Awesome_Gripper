import os
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.actions import TimerAction
from launch_ros.actions import Node
from launch.substitutions import Command, FindExecutable
from ament_index_python.packages import get_package_share_directory
from launch_ros.parameter_descriptions import ParameterValue
import launch_ros.actions  # This defines `launch_ros`
from launch_ros.actions import Node

def generate_launch_description():
    # Define the package directory for the robot URDF description
    gripper_description_pkg = get_package_share_directory("gripper")

    # Path to the robot's Xacro file
    path_to_urdf = os.path.join(gripper_description_pkg, "urdf", "gripper.urdf.xacro")

    # Joint State Publisher - broadcasts joint angle values
    joint_state_publisher = Node(
        package="joint_state_publisher",
        executable="joint_state_publisher",
        name="joint_state_publisher",
        output="screen"
    )

    # Joint State Publisher GUI - allows manual adjustment of joint angles, delayed start
    joint_state_publisher_gui = TimerAction(
        period=3.0,  # Add a delay before starting
        actions=[Node(
            package="joint_state_publisher_gui",
            executable="joint_state_publisher_gui",
            name="joint_state_publisher_gui",
            output="screen"
        )]
    )

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

    # RViz - Visualization tool for ROS
    rviz = Node(
        package="rviz2",
        executable="rviz2",
        name="rviz2",
        output="screen",
        arguments=["-d", os.path.join(gripper_description_pkg, "rviz", "display.rviz")],
    )

    return LaunchDescription([
        joint_state_publisher,    # Starts the Joint State Publisher
        joint_state_publisher_gui, # Adds the GUI for Joint States
        robot_state_publisher,    # Starts the Robot State Publisher
        rviz                      # Starts RViz
    ])
