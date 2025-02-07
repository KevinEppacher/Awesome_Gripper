cmake_minimum_required(VERSION 3.5)

project(urdf_6_dofra_v3)

find_package(ament_cmake REQUIRED)
find_package(urdf REQUIRED)

install(DIRECTORY config launch meshes urdf
	DESTINATION share/${PROJECT_NAME}
)

ament_package()