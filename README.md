# Awesome_Gripper
Mechanical Gripper Development
- 1: gripper_moveit_config demo.launch.py

- 2: ros2 launch gazebo_ros gazebo.launch.py

- 3:Generate the URDF from robot parameter server urdf.xacro 
    ros2 run xacro xacro /app/install/gripper_moveit_config/share/gripper_moveit_config/config/gripper.urdf.xacro -o /tmp/gripper.urdf

- 4: Spawn urdf in gazebo
    ros2 run gazebo_ros spawn_entity.py -file /tmp/gripper.urdf -entity gripper

// may need
- may before 4: ros2 service call /delete_entity gazebo_msgs/srv/DeleteEntity "{name: 'gripper'}"

- 4: ros2 run gazebo_ros spawn_entity.py -file /tmp/gripper.urdf -entity gripper -x 0 -y 0 -z 1

