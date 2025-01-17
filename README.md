# MYNT EYE ROS2 Wrapper

This Repository contains ROS2 wrapper for MYNT EYE stereo camera.

## Supported Devices

- [MYNT EYE Standard (Non-IR version)](https://www.mynteye.com/products/mynt-eye-stereo-camera?variant=13183676973079)

## Prerequisites

- Operating System: Ubuntu 22.04
- ROS2 Iron 
- MYNT EYE S SDK

### Installing Prerequisites

1. Install ROS2 Iron by following instructions below.

    ```bash
    sudo apt-get update && sudo apt-get install locales
    sudo locale-gen en_US en_US.UTF-8
    sudo update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8
    export LANG=en_US.UTF-8

    sudo apt-get update && sudo apt-get install curl gnupg2 lsb-release
    curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | sudo apt-key add -
    sudo sh -c 'echo "deb [arch=$(dpkg --print-architecture)] http://packages.ros.org/ros2/ubuntu $(lsb_release -cs) main" > /etc/apt/sources.list.d/ros2-latest.list'

    sudo apt-get update
    sudo apt-get install ros-iron-desktop python3-colcon-common-extensions python3-rosdep
    sudo apt-get install python3-pip
    pip3 install -U argcomplete

    sudo apt-get install python3-opencv

    sudo rosdep init
    rosdep update

    echo "source /opt/ros/iron/setup.bash" >> ~/.bashrc
    ```

2. Install Mynt EYE S SDK by following the instructions below.

    ```bash
    sudo apt-get install build-essential cmake git
    git clone https://github.com/EgeSaykan/MYNT-EYE-S-SDK.git
    cd MYNT-EYE-S-SDK
    make init
    make install
    make samples
    ```

## Setup MYNT EYE ROS2 Wrapper

```bash
sudo apt-get install ros-iron-camera-info-manager ros-iron-launch-testing-ament-cmake
mkdir dev_ws
cd dev_ws
mkdir src
cd src
git clone https://github.com/EgeSaykan/MYNT-EYE-S-ROS2-WRAPPER-IRON.git
git clone https://github.com/ros-perception/image_pipeline.git
cd image_pipeline
git checkout iron
cd ../../
colcon build
```

## Run MYNT EYE ROS2 Wrapper

Open new tab in terminal to run mynteye camera.

```bash
cd dev_ws
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/lib
. install/setup.bash
ros2 launch mynteye_ros2_wrapper mynteye.launch.py
```

## Calibrate MYNT EYE

Open new tab in terminal to run mynteye calibration.

```bash
cd dev_ws
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/lib
. install/setup.bash
ros2 launch mynteye_ros2_wrapper mynteye_calib.launch.py
```

## Changes

This wrapper was modified from Harsha [Vardhan Koganti's wrapper](https://github.com/harsha-vk/mynteye_ros2_wrapper/tree/main).<br>
The original versoin does not support Ubuntu 22.04 or Ros2 Iron. This clone is updated to work on modern systems.