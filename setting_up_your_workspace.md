---
descripton: A list of commands to help you set up your programming space
documentation: 
---

## prerequisites

you must have:
- Windows 10 or Ubuntu 22.04 (see [installing ubuntu 22.04](./installing_ubuntu.md))
	- all the instructions below are made for ubuntu 22.04
- at least 16 gigabytes of ram

## installation
1. install and set up docker [(intsructions here)](https://github.com/MHSeals/ROS2-Docker-Crash-Course)
2. install [slam_toolbox](./slam_toolbox) and [kiss_icp](./kiss_icp)

## workspace setup
1. run [gazebo](./gazebo) using the command `ros2 launch vrx_gazebo rviz.launch.py`
2. run 