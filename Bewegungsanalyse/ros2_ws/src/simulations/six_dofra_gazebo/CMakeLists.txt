cmake_minimum_required(VERSION 3.5)
project(six_dofra_gazebo)

# Find dependencies
find_package(ament_cmake REQUIRED)
find_package(urdf REQUIRED)

# Install the launch directory
install(DIRECTORY launch urdf meshes
	DESTINATION share/${PROJECT_NAME}
)

ament_package()
