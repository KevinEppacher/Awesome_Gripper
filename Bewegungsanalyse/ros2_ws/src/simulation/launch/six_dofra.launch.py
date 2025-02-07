import os
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():
    # Declare launch arguments
    paused_arg = DeclareLaunchArgument(
        "paused", default_value="false", description="Whether simulation is paused"
    )

    robot_pose_arg = DeclareLaunchArgument(
        "robot_pose", default_value="-x 0 -y 0 -z 0.8 -R 0 -P 0 -Y 0", description="Robot spawn pose"
    )

    # Evaluate unpause argument
    unpause = LaunchConfiguration("paused").perform({}) == "false"

    # Get paths to URDF and controller files
    urdf_package = get_package_share_directory("urdf_6_dofra_v3")
    robot_urdf = os.path.join(urdf_package, "urdf", "URDF_Assembly_6_DOFRA_v3.xacro")

    moveit_config_package = get_package_share_directory("six_dofra_moveit_config_v3")
    gazebo_controllers_yaml = os.path.join(moveit_config_package, "config", "gazebo_controllers.yaml")
    ros_controllers_launch = os.path.join(moveit_config_package, "launch", "ros_controllers.launch.py")
    moveit_demo_launch = os.path.join(moveit_config_package, "launch", "demo.launch.py")

    # Spawn the robot in Gazebo
    spawn_robot = Node(
        package="gazebo_ros",
        executable="spawn_entity.py",
        name="spawn_gazebo_model",
        arguments=[
            "-entity", "robot",
            "-file", robot_urdf,
            "-x", "0", "-y", "0", "-z", "0.8",
            "-Y", "0",
            "-R", "0",
            "-P", "0",
        ] + (["-unpause"] if unpause else []),
        output="screen",
    )

    # Load controller parameters
    load_controllers = Node(
        package="ros2_control_node",
        executable="ros2_control_node",
        parameters=[gazebo_controllers_yaml],
        output="screen",
    )

    # Launch ROS controllers
    ros_controllers = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(ros_controllers_launch)
    )

    # Spawn the Gazebo ROS controllers
    spawn_controllers = Node(
        package="controller_manager",
        executable="spawner",
        arguments=["joint_state_controller"],
        output="screen",
    )

    # Robot state publisher
    robot_state_publisher = Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        output="screen",
    )

    # Launch MoveIt
    moveit_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(moveit_demo_launch),
        launch_arguments={
            "load_robot_description": "false",
            "moveit_controller_manager": "ros_control",
        }.items(),
    )

    return LaunchDescription([
        paused_arg,
        robot_pose_arg,
        spawn_robot,
        load_controllers,
        ros_controllers,
        spawn_controllers,
        robot_state_publisher,
        moveit_launch,
    ])
