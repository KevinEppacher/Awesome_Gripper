# Install script for directory: /home/kevin/Documents/Master/3_Semester/Produktentwicklung/Awesome_Gripper/Bewegungsanalyse/catkin_ws/src/cobot_moveit_config_gazebo

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
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/kevin/Documents/Master/3_Semester/Produktentwicklung/Awesome_Gripper/Bewegungsanalyse/catkin_ws/build/cobot_moveit_config_gazebo/catkin_generated/installspace/cobot_moveit_gazebo_config.pc")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/cobot_moveit_gazebo_config/cmake" TYPE FILE FILES
    "/home/kevin/Documents/Master/3_Semester/Produktentwicklung/Awesome_Gripper/Bewegungsanalyse/catkin_ws/build/cobot_moveit_config_gazebo/catkin_generated/installspace/cobot_moveit_gazebo_configConfig.cmake"
    "/home/kevin/Documents/Master/3_Semester/Produktentwicklung/Awesome_Gripper/Bewegungsanalyse/catkin_ws/build/cobot_moveit_config_gazebo/catkin_generated/installspace/cobot_moveit_gazebo_configConfig-version.cmake"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/cobot_moveit_gazebo_config" TYPE FILE FILES "/home/kevin/Documents/Master/3_Semester/Produktentwicklung/Awesome_Gripper/Bewegungsanalyse/catkin_ws/src/cobot_moveit_config_gazebo/package.xml")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/cobot_moveit_gazebo_config" TYPE DIRECTORY FILES "/home/kevin/Documents/Master/3_Semester/Produktentwicklung/Awesome_Gripper/Bewegungsanalyse/catkin_ws/src/cobot_moveit_config_gazebo/launch" REGEX "/setup\\_assistant\\.launch$" EXCLUDE)
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/cobot_moveit_gazebo_config" TYPE DIRECTORY FILES "/home/kevin/Documents/Master/3_Semester/Produktentwicklung/Awesome_Gripper/Bewegungsanalyse/catkin_ws/src/cobot_moveit_config_gazebo/config")
endif()

