---
descripton: A list of commands to help you set up your programming space
documentation: 
---

## prerequisites

you must have:
- Windows 10 or Ubuntu 22.04 (see [installing ubuntu 22.04](installing_ubuntu.md))
	- all the instructions below are made for and only ubuntu 22.04
- at least 16 gigabytes of ram

## installation
1. install and set up docker [(intsructions here)](https://github.com/MHSeals/ROS2-Docker-Crash-Course)
2. install [slam_toolbox](slam_toolbox.md) and [kiss_icp](./kiss_icp.d)

## workspace setup
1. run [gazebo](gazebo.md) using the command `ros2 launch vrx_gz competition.launch.py`
2. run [vrx](vrx.md) using the command `ros2 launch vrx_gazebo rviz.launch.py`
3. run [slam_toolbox](slam_toolbox.md) using the command `ros2 launch slam_toolbox online_async_launch.py use_sim_time:=True`
4. run [kiss_icp](kiss_icp.md) using the command `ros2 launch kiss_icp odometry.launch.py topic:=/wamv/sensors/lidars/lidar_wamv_sensor/points`