cmake_minimum_required(VERSION 3.5)
project(gripper)

# Find necessary packages
find_package(ament_cmake REQUIRED)
find_package(urdf REQUIRED)
find_package(xacro REQUIRED)
find_package(ros2_control REQUIRED)
find_package(ros2_controllers REQUIRED)
find_package(gazebo_ros REQUIRED)
find_package(rclcpp REQUIRED)
find_package(sensor_msgs REQUIRED)
find_package(geometry_msgs REQUIRED)
find_package(std_msgs REQUIRED)
find_package(rosidl_default_runtime REQUIRED)

# Export package dependencies
ament_export_dependencies(urdf xacro ros2_control ros2_controllers gazebo_ros rclcpp sensor_msgs geometry_msgs std_msgs rosidl_default_runtime)

# Install configuration, launch, mesh, and URDF files
install(
  DIRECTORY cfg config launch meshes urdf
  DESTINATION share/${PROJECT_NAME}
  FILES_MATCHING PATTERN "*"
)

# Add ament package definition (must be at the end)
ament_package()
