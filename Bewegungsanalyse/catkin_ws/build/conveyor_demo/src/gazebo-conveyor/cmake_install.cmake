# Install script for directory: /home/kevin/Documents/Master/3_Semester/Produktentwicklung/Awesome_Gripper/Bewegungsanalyse/catkin_ws/src/conveyor_demo/src/gazebo-conveyor

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
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/gazebo_conveyor/msg" TYPE FILE FILES "/home/kevin/Documents/Master/3_Semester/Produktentwicklung/Awesome_Gripper/Bewegungsanalyse/catkin_ws/src/conveyor_demo/src/gazebo-conveyor/msg/ConveyorBeltState.msg")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/gazebo_conveyor/srv" TYPE FILE FILES "/home/kevin/Documents/Master/3_Semester/Produktentwicklung/Awesome_Gripper/Bewegungsanalyse/catkin_ws/src/conveyor_demo/src/gazebo-conveyor/srv/ConveyorBeltControl.srv")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/gazebo_conveyor/cmake" TYPE FILE FILES "/home/kevin/Documents/Master/3_Semester/Produktentwicklung/Awesome_Gripper/Bewegungsanalyse/catkin_ws/build/conveyor_demo/src/gazebo-conveyor/catkin_generated/installspace/gazebo_conveyor-msg-paths.cmake")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include" TYPE DIRECTORY FILES "/home/kevin/Documents/Master/3_Semester/Produktentwicklung/Awesome_Gripper/Bewegungsanalyse/catkin_ws/devel/include/gazebo_conveyor")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/roseus/ros" TYPE DIRECTORY FILES "/home/kevin/Documents/Master/3_Semester/Produktentwicklung/Awesome_Gripper/Bewegungsanalyse/catkin_ws/devel/share/roseus/ros/gazebo_conveyor")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/common-lisp/ros" TYPE DIRECTORY FILES "/home/kevin/Documents/Master/3_Semester/Produktentwicklung/Awesome_Gripper/Bewegungsanalyse/catkin_ws/devel/share/common-lisp/ros/gazebo_conveyor")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/gennodejs/ros" TYPE DIRECTORY FILES "/home/kevin/Documents/Master/3_Semester/Produktentwicklung/Awesome_Gripper/Bewegungsanalyse/catkin_ws/devel/share/gennodejs/ros/gazebo_conveyor")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  execute_process(COMMAND "/usr/bin/python3" -m compileall "/home/kevin/Documents/Master/3_Semester/Produktentwicklung/Awesome_Gripper/Bewegungsanalyse/catkin_ws/devel/lib/python3/dist-packages/gazebo_conveyor")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python3/dist-packages" TYPE DIRECTORY FILES "/home/kevin/Documents/Master/3_Semester/Produktentwicklung/Awesome_Gripper/Bewegungsanalyse/catkin_ws/devel/lib/python3/dist-packages/gazebo_conveyor")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/kevin/Documents/Master/3_Semester/Produktentwicklung/Awesome_Gripper/Bewegungsanalyse/catkin_ws/build/conveyor_demo/src/gazebo-conveyor/catkin_generated/installspace/gazebo_conveyor.pc")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/gazebo_conveyor/cmake" TYPE FILE FILES "/home/kevin/Documents/Master/3_Semester/Produktentwicklung/Awesome_Gripper/Bewegungsanalyse/catkin_ws/build/conveyor_demo/src/gazebo-conveyor/catkin_generated/installspace/gazebo_conveyor-msg-extras.cmake")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/gazebo_conveyor/cmake" TYPE FILE FILES
    "/home/kevin/Documents/Master/3_Semester/Produktentwicklung/Awesome_Gripper/Bewegungsanalyse/catkin_ws/build/conveyor_demo/src/gazebo-conveyor/catkin_generated/installspace/gazebo_conveyorConfig.cmake"
    "/home/kevin/Documents/Master/3_Semester/Produktentwicklung/Awesome_Gripper/Bewegungsanalyse/catkin_ws/build/conveyor_demo/src/gazebo-conveyor/catkin_generated/installspace/gazebo_conveyorConfig-version.cmake"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/gazebo_conveyor" TYPE FILE FILES "/home/kevin/Documents/Master/3_Semester/Produktentwicklung/Awesome_Gripper/Bewegungsanalyse/catkin_ws/src/conveyor_demo/src/gazebo-conveyor/package.xml")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libConveyorBeltPlugin.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libConveyorBeltPlugin.so")
    file(RPATH_CHECK
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libConveyorBeltPlugin.so"
         RPATH "")
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE SHARED_LIBRARY FILES "/home/kevin/Documents/Master/3_Semester/Produktentwicklung/Awesome_Gripper/Bewegungsanalyse/catkin_ws/devel/lib/libConveyorBeltPlugin.so")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libConveyorBeltPlugin.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libConveyorBeltPlugin.so")
    file(RPATH_CHANGE
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libConveyorBeltPlugin.so"
         OLD_RPATH "/usr/lib/x86_64-linux-gnu/gazebo-11/plugins:/opt/ros/noetic/lib/x86_64-linux-gnu:/opt/ros/noetic/lib:"
         NEW_RPATH "")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/usr/bin/strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libConveyorBeltPlugin.so")
    endif()
  endif()
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libROSConveyorBeltPlugin.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libROSConveyorBeltPlugin.so")
    file(RPATH_CHECK
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libROSConveyorBeltPlugin.so"
         RPATH "")
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE SHARED_LIBRARY FILES "/home/kevin/Documents/Master/3_Semester/Produktentwicklung/Awesome_Gripper/Bewegungsanalyse/catkin_ws/devel/lib/libROSConveyorBeltPlugin.so")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libROSConveyorBeltPlugin.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libROSConveyorBeltPlugin.so")
    file(RPATH_CHANGE
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libROSConveyorBeltPlugin.so"
         OLD_RPATH "/usr/lib/x86_64-linux-gnu/gazebo-11/plugins:/home/kevin/Documents/Master/3_Semester/Produktentwicklung/Awesome_Gripper/Bewegungsanalyse/catkin_ws/devel/lib:/opt/ros/noetic/lib/x86_64-linux-gnu:/opt/ros/noetic/lib:"
         NEW_RPATH "")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/usr/bin/strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libROSConveyorBeltPlugin.so")
    endif()
  endif()
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
endif()

