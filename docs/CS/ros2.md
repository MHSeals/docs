---
descripton: documentation about ros2
documentation: https://docs.ros.org/en/humble/index.html
---
ros, short for Robot Operating System, is not an operating system.
ros is a set of software libraries and tools built to help people like us make software for robots! ros2 is an improvement on ros1.
at the time of writing (October 2024), we are using ros2 humble. this should come preinstalled with your docker setup

## how does ros2 work?
### the ros2 graph
![The ROS2 node graph.](https://docs.ros.org/en/humble/_images/Nodes-TopicandService.gif)
### nodes
ros2 is built on a structure of nodes: a node is an executeable program that can perform tasks and operations. these nodes can communicate with each other using topics or services.
for more information on nodes, [check here](https://docs.ros.org/en/humble/Tutorials/Beginner-CLI-Tools/Understanding-ROS2-Nodes/Understanding-ROS2-Nodes.html).
### [topics, publishers and subscribers](https://docs.ros.org/en/humble/Tutorials/Beginner-CLI-Tools/Understanding-ROS2-Topics/Understanding-ROS2-Topics.html)
a publisher sends a message to a topic, and subscribers listening to that topic will receive that information.
there is no limit on how many topics you can publish and subscribe to (or make!)
### [services, servers, and clients](https://docs.ros.org/en/humble/Tutorials/Beginner-CLI-Tools/Understanding-ROS2-Services/Understanding-ROS2-Services.html)
a service client sends a request to a server, and the server returns a response to the client.
### [actions](https://docs.ros.org/en/humble/Tutorials/Beginner-CLI-Tools/Understanding-ROS2-Actions/Understanding-ROS2-Actions.html)
![A visual breakdown of an action.](https://docs.ros.org/en/humble/_images/Action-SingleActionClient.gif)
3 parts of an action:
- goal
- feedback
- result
### packages
a package is just a synonym for a piece of software. they're composed of folders containing scripts, launch files, and configuration files.
to update all your packages, run `colcon build` in your root directory. this command will create folders such as `build`, `install`, and `log`.

## where do i go from here?
now that you understand how ros2 works, you can learn how to use some software that we use along with ros2.
* [gazebo](gazebo.md) - a robot simulation program
* [vrx](vrx.md) - 
* [slam_toolbox](slam_toolbox.md) - tools to combat the slam problem
* [kiss_icp](kiss_icp.md) - an odometry pipeline
if you're not ready to get started with programming, you can also help expand this documentation by making pull requests!