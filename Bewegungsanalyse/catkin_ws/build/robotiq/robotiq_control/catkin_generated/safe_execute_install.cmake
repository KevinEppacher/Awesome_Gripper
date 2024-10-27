execute_process(COMMAND "/home/kevin/Documents/Master/3_Semester/Produktentwicklung/Awesome_Gripper/Bewegungsanalyse/catkin_ws/build/robotiq/robotiq_control/catkin_generated/python_distutils_install.sh" RESULT_VARIABLE res)

if(NOT res EQUAL 0)
  message(FATAL_ERROR "execute_process(/home/kevin/Documents/Master/3_Semester/Produktentwicklung/Awesome_Gripper/Bewegungsanalyse/catkin_ws/build/robotiq/robotiq_control/catkin_generated/python_distutils_install.sh) returned error code ")
endif()
