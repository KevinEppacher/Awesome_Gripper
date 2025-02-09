# Awesome_Gripper
Mechanical Gripper Development
- 1: ros2 launch gripper_moveit_config demo.launch.py

- 2: ros2 launch gazebo_ros gazebo.launch.py

- 3:Generate the URDF from robot parameter server urdf.xacro 
    ros2 run xacro xacro /app/install/gripper_moveit_config/share/gripper_moveit_config/config/gripper.urdf.xacro -o /tmp/gripper.urdf

- 4: Spawn urdf in gazebo
    ros2 run gazebo_ros spawn_entity.py -file /tmp/gripper.urdf -entity gripper

// may need
- may before 4: ros2 service call /delete_entity gazebo_msgs/srv/DeleteEntity "{name: 'gripper'}"

- 4: ros2 run gazebo_ros spawn_entity.py -file /tmp/gripper.urdf -entity gripper -x 0 -y 0 -z 1



TUTORIAL:
https://docs.ros.org/en/humble/Tutorials/Intermediate/URDF/Using-a-URDF-in-Gazebo.html

Setps:

- 1: export gazebo model in package.xml
- 2: CMakeLists directories have to be installed
- 3: working xacro, check after colcon build:
    ros2 run xacro xacro $(ros2 pkg prefix gripper --share)/urdf/gripper.urdf.xacro > gripper.urdf
- 4: correct launch file -> path to urdf currently not working
     if no permissions:
        chmod +rwx /app/install/gripper/share/gripper/urdf/gripper.urdf.xacro
     check permissions:
        ls -l /app/install/gripper/share/gripper/urdf/gripper.urdf.xacro



