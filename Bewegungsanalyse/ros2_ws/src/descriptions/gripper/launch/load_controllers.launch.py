from launch import LaunchDescription
from launch.actions import ExecuteProcess, TimerAction


def generate_launch_description():
    return LaunchDescription([

        # Wait 10 seconds before loading controllers to allow startup
        TimerAction(
            period=10.0,
            actions=[
                ExecuteProcess(
                    cmd=['ros2', 'control', 'load_controller',
                         '--set-state', 'active', 'joint_state_broadcaster'],
                    output='screen'
                ),
                ExecuteProcess(
                    cmd=['ros2', 'control', 'load_controller', '--set-state',
                         'active', 'gripper_planning_group_controller'],
                    output='screen'
                )
            ]
        )
    ])
