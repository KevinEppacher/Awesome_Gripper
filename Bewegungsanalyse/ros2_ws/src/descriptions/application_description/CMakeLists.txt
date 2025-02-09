cmake_minimum_required(VERSION 3.5)
project(application_description)

# Find the necessary packages
find_package(ament_cmake REQUIRED)

# Install directories
install(
  DIRECTORY launch urdf rviz
  DESTINATION share/${PROJECT_NAME}
)

# Export package dependencies
ament_package()
