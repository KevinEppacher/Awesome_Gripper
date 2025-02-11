cmake_minimum_required(VERSION 3.5)
project(gripper)

# Find the necessary packages
find_package(urdf REQUIRED)
find_package(xacro REQUIRED)
find_package(ros2_control REQUIRED)
find_package(ros2_controllers REQUIRED)
find_package(gazebo_ros REQUIRED)

find_package(ament_cmake REQUIRED)

# Install directories
install(
  DIRECTORY config launch meshes urdf
  DESTINATION share/${PROJECT_NAME}
)

# Export package dependencies
ament_package()