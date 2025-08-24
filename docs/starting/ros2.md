[](){ #ros2 }
# ROS 2 Overview

Welcome to ROS 2! ROS (Robot Operating System), is not actually an operating system, but is a powerful set of libraries and tools for building robot software. ROS 2 is the modern, improved version of ROS 1, and our team uses the **Humble** distribution (as of October 2024).

---

## What is ROS 2?

ROS 2 helps you create modular, scalable, and robust robotics applications. It provides a flexible framework for writing robot code, connecting sensors, actuators, and algorithms.

---

## How Does ROS 2 Work?

![ROS2 node graph](./ros2_nodegraph.gif)
ROS 2 applications are built from interconnected nodes that communicate with each other.

### Nodes
A **node** is an executable program that performs a specific task. Nodes can communicate using topics, services, and actions.
- [Learn more about nodes](https://docs.ros.org/en/humble/Tutorials/Beginner-CLI-Tools/Understanding-ROS2-Nodes/Understanding-ROS2-Nodes.html)

### Topics, Publishers, and Subscribers
- A **publisher** sends messages to a topic.
- **Subscribers** listen for messages on topics.
- You can create as many topics as you need!
- [Topics tutorial](https://docs.ros.org/en/humble/Tutorials/Beginner-CLI-Tools/Understanding-ROS2-Topics/Understanding-ROS2-Topics.html)

### Services, Servers, and Clients
- A **service client** sends a request to a server, which returns a response.
- [Services tutorial](https://docs.ros.org/en/humble/Tutorials/Beginner-CLI-Tools/Understanding-ROS2-Services/Understanding-ROS2-Services.html)

### Actions
![ROS2 action breakdown](./ros2_nodeactions.gif)
Actions allow for long-running tasks with feedback. They have three parts:
1. **Goal**
2. **Feedback**
3. **Result**
- [Actions tutorial](https://docs.ros.org/en/humble/Tutorials/Beginner-CLI-Tools/Understanding-ROS2-Actions/Understanding-ROS2-Actions.html)

### Packages
A **package** is a collection of code, launch files, and configuration for a specific functionality. To build or update all packages, run:

```sh
colcon build
```

This creates `build`, `install`, and `log` folders in your workspace.

---

## Next Steps

- Ready to start programming? Explore our [Basic Commands](./basic_commands.md) and [Workspace Setup](../setup/workspace_setup.md) guides.
- Want to help improve these docs? Submit a pull request on [GitHub](https://github.com/MHSeals/docs)!

---
