# Install script for directory: /home/kevin/Documents/Master/3_Semester/Produktentwicklung/Awesome_Gripper/Bewegungsanalyse/catkin_ws/src/robotiq/robotiq_description

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/kevin/Documents/Master/3_Semester/Produktentwicklung/Awesome_Gripper/Bewegungsanalyse/catkin_ws/install")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/kevin/Documents/Master/3_Semester/Produktentwicklung/Awesome_Gripper/Bewegungsanalyse/catkin_ws/build/robotiq/robotiq_description/catkin_generated/installspace/robotiq_description.pc")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/robotiq_description/cmake" TYPE FILE FILES
    "/home/kevin/Documents/Master/3_Semester/Produktentwicklung/Awesome_Gripper/Bewegungsanalyse/catkin_ws/build/robotiq/robotiq_description/catkin_generated/installspace/robotiq_descriptionConfig.cmake"
    "/home/kevin/Documents/Master/3_Semester/Produktentwicklung/Awesome_Gripper/Bewegungsanalyse/catkin_ws/build/robotiq/robotiq_description/catkin_generated/installspace/robotiq_descriptionConfig-version.cmake"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/robotiq_description" TYPE FILE FILES "/home/kevin/Documents/Master/3_Semester/Produktentwicklung/Awesome_Gripper/Bewegungsanalyse/catkin_ws/src/robotiq/robotiq_description/package.xml")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/robotiq_description" TYPE DIRECTORY FILES
    "/home/kevin/Documents/Master/3_Semester/Produktentwicklung/Awesome_Gripper/Bewegungsanalyse/catkin_ws/src/robotiq/robotiq_description/launch"
    "/home/kevin/Documents/Master/3_Semester/Produktentwicklung/Awesome_Gripper/Bewegungsanalyse/catkin_ws/src/robotiq/robotiq_description/meshes"
    "/home/kevin/Documents/Master/3_Semester/Produktentwicklung/Awesome_Gripper/Bewegungsanalyse/catkin_ws/src/robotiq/robotiq_description/urdf"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "//robots/meshes")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
file(INSTALL DESTINATION "//robots" TYPE DIRECTORY FILES "/home/kevin/Documents/Master/3_Semester/Produktentwicklung/Awesome_Gripper/Bewegungsanalyse/catkin_ws/src/robotiq/robotiq_description/meshes")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "//robots/meshes")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
file(INSTALL DESTINATION "//robots" TYPE DIRECTORY FILES "/home/kevin/Documents/Master/3_Semester/Produktentwicklung/Awesome_Gripper/Bewegungsanalyse/catkin_ws/src/robotiq/robotiq_description/meshes")
endif()

