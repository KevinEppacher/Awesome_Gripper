import os
from launch import LaunchDescription
from launch.actions import ExecuteProcess
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    controllers_yaml = os.path.join(
        get_package_share_directory("six_dofra_config"), "config", "ros2_controllers.yaml"
    )

    return LaunchDescription([
        # Start Controller Manager
        ExecuteProcess(
            cmd=["ros2", "control", "load_controller", "--set-state", "active", "joint_state_broadcaster"],
            output="screen"
        ),
        ExecuteProcess(
            cmd=["ros2", "control", "load_controller", "--set-state", "active", "forward_position_controller"],
            output="screen"
        ),
    ])
