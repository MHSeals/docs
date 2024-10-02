---
date: 2024-10-01
descripton: documentation about ros2
documentation: https://docs.ros.org/en/humble/index.html
tags: roboboat
---
ros, short for Robot Operating System, is not an operating system.
ros is a set of software libraries and tools built to help people like us make software for robots! ros2 is an improvement on ros1.
at the time of writing (October 2024), we are using ros2 humble. this should come preinstalled with your docker setup

## how does ros2 work?
### the ros2 graph
### nodes
ros2 is built on a structure of nodes: every node represents a single process (think of them as files in a folder), and all these nodes can send and recieve messages to each other.
for more information on nodes, [check here](https://docs.ros.org/en/humble/Tutorials/Beginner-CLI-Tools/Understanding-ROS2-Nodes/Understanding-ROS2-Nodes.html).
### topics, publishers and subscribers
#### let's try it!
### servers and clients
#### let's try it!
### actions
### colcon

## where do i go from here?
now that you understand how ros2 works, you can learn how to use some software that we use along with ros2.
* [[gazebo]] - a robot simulation program
* [[vrx]] - 
* [[slam_toolbox]] - tools to combat the slam problem
* [[kiss_icp]] - an odometry pipeline
if you're not ready to get started with programming, you can also help expand this documentation by making pull requests!