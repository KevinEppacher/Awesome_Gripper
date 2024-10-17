FROM osrf/ros:noetic-desktop-full

# Add vscode user with same UID and GID as your host system
# (copied from https://code.visualstudio.com/remote/advancedcontainers/add-nonroot-user#_creating-a-nonroot-user)
ARG USERNAME=vscode
ARG USER_UID=1000
ARG USER_GID=$USER_UID
RUN groupadd --gid $USER_GID $USERNAME \
    && useradd -s /bin/bash --uid $USER_UID --gid $USER_GID -m $USERNAME \
    && apt-get update \
    && apt-get install -y sudo \
    && echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME \
    && chmod 0440 /etc/sudoers.d/$USERNAME
# Switch from root to user
USER $USERNAME

# Add user to video group to allow access to webcam
RUN sudo usermod --append --groups video $USERNAME

# Update all packages
RUN sudo apt update && sudo apt upgrade -y

# Rosdep update
RUN rosdep update

RUN sudo apt update && sudo apt upgrade -y

RUN sudo apt install -y ros-${ROS_DISTRO}-ur-robot-driver

RUN sudo apt-get install -y ros-$ROS_DISTRO-universal-robots

RUN sudo apt-get install -y ros-$ROS_DISTRO-ur10-moveit-config

RUN sudo apt-get update -y

RUN sudo apt-get install -y ros-noetic-moveit-visual-tools

RUN sudo apt-get install -y ros-noetic-rosbridge-suite

RUN sudo apt-get install -y ros-noetic-ur-gazebo

RUN sudo apt-get install -y ros-noetic-moveit-commander

RUN sudo apt-get install -y libglfw3-dev

RUN sudo apt install -y ros-noetic-joint-state-controller

RUN sudo apt install -y ros-noetic-controller-manager*

RUN sudo apt install -y ros-noetic-moveit-ros-control-interface

# RUN sudo apt-get install -y ros-$ROS_DISTRO-ur-kinematics

# Install Git
RUN sudo apt install -y git

RUN sudo apt update -qq \
&& rosdep update


ENV XDG_RUNTIME_DIR=/tmp/runtime-$USERNAME
RUN mkdir -p $XDG_RUNTIME_DIR && chmod 700 $XDG_RUNTIME_DIR

RUN sudo usermod -a -G dialout $USERNAME

# Source the ROS setup file
RUN echo "source /opt/ros/${ROS_DISTRO}/setup.bash" >> ~/.bashrc

RUN sudo apt update -y && sudo apt install -y && sudo apt upgrade -y
