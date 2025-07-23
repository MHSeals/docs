# MHSeals Boat Control Software (mhsboat_ctrl)

This page provides an in-depth overview of the MHSeals boat control software, its architecture, packages, and usage. The control system is designed for modularity, simulation support, and robust autonomous operation using ROS 2.

*This code is being actively developed and may change frequently so this documentation may not always be up-to-date. Please refer to the GitHub repository for the latest code and updates.*

---

## Overview

- **Repository:** [MHSeals/mhsboat_ctrl](https://github.com/MHSeals/mhsboat_ctrl)
- **Main Language:** Python
- **Framework:** ROS 2 Humble
- **OS:** Ubuntu 22.04

---

## Architecture & Principles

### 1. Global Coordinates
All navigation and movement are now referenced to a global coordinate system (e.g., map or GPS coordinates). This allows for easier integration with mapping, localization, and multi-vehicle scenarios.

### 2. Modularity
Tasks are implemented as separate classes inheriting from a base `Task` class. New tasks can be added without affecting existing code.

### 3. Simulation Support
The system can run in simulation mode using a simulated map, allowing for development and testing without hardware.

---

## Main Packages & Their Roles

### mhsboat_ctrl
- **Purpose:** Main control logic, task management, decision-making, actuator interfacing.
- **Key Files:**
  - `mhsboat_ctrl.py`: Main loop, task execution, sensor integration.
  - `task.py`: Base class for all tasks.
  - `tasks/`: Individual task implementations (navigation, obstacle avoidance, etc).
- **ROS Topics:**
  - Subscribes: `/mhsboat_ctrl/map`
  - Publishes: `/mavros/setpoint_velocity/cmd_vel`

### sensors
- **Purpose:** Sensor data collection, fusion, and processing (camera, LiDAR, odometry).
- **Key Files:**
  - `sensors.py`: Main sensor node.
  - `utils/lidar.py`: LiDAR data utilities.
- **ROS Topics:**
  - Subscribes: `/AiOutput`, `/center_of_clusters`, `/odometry/filtered`
  - Publishes: `/mhsboat_ctrl/map`, `/mhsboat_ctrl/buoy_clusters`

### simulated_map
- **Purpose:** Provides a virtual course for simulation and testing.
- **Key Files:**
  - `gui.py`: GUI for visualizing the simulated environment.

### display_map
- **Purpose:** Visualizes map data and detected objects.
- **Key Files:**
  - `testgui.py`: GUI for map display.

### buoy_recognition
- **Purpose:** Detects and classifies buoys/objects using camera images and YOLO model.
- **Key Files:**
  - `buoy_recognition.py`: Main node for object detection.
- **Parameters:**
  - `headless_mode` (default: True): Controls image display.
- **ROS Topics:**
  - Subscribes: `/image_raw`
  - Publishes: `/AiOutput`

### center_of_clusters
- **Purpose:** Processes LiDAR point clouds to identify clusters (buoys, obstacles).
- **Key Files:**
  - `center_of_clusters.py`: Main clustering node.
- **ROS Topics:**
  - Subscribes: `/velodyne_points`
  - Publishes: `/center_of_clusters`

### bag_recorder
- **Purpose:** Records ROS 2 bag files for data logging and analysis.
- **Key Files:**
  - `bag_recorder.py`: Main recording node.
- **ROS Topics:**
  - Subscribes: `/mhsboat_ctrl/map`

---

## Task System

- Tasks are stored in `mhsboat_ctrl/tasks/`.
- Each task is a class inheriting from `Task` (in `task.py`).
- The base `Task` class defines `run` and `search` methods.
- To add a new task: create a new file/class in `tasks/`, inherit from `Task`, and register with `BoatController.add_task`.

---

## Main Loop & Execution

- The main loop (in `mhsboat_ctrl.py`) continuously searches for and executes tasks.
- Each task receives a `Sensors` object for data and map access.
- Task completion and status are managed using enums (`TaskCompletionStatus`, `TaskStatus` in `enums.py`).

---

## Simulation Mode

*This mode does not currently work, it is being worked on.*

- Run with parameters: `use_simulated_map` and `map_file`.
- Example:
  ```bash
  ros2 run mhsboat_ctrl mhsboat_ctrl --ros-args -p use_simulated_map:=true -p map_file:=src/mhsboat_ctrl/maps/taskone.yaml
  ```

---

## Building & Running

- Build with symlink install for easy code changes:
  ```bash
  cd ~/ros_ws
  colcon build --symlink-install --packages-select mhsboat_ctrl
  ```
- See [commands_to_run_boat.md](https://github.com/MHSeals/mhsboat_ctrl/blob/main/commands_to_run_boat.md) for run instructions.

---

## Contributing & Extending

- See [CONTRIBUTING.md](https://github.com/MHSeals/mhsboat_ctrl/blob/main/CONTRIBUTING.md) for guidelines.
- Modular design makes it easy to add new sensors, tasks, or simulation features.

---

## References & Links

- [MHSeals/mhsboat_ctrl GitHub](https://github.com/MHSeals/mhsboat_ctrl)
- [Custom messages: boat_interfaces](https://github.com/MHSeals/boat_interfaces)
- [ROS 2 Documentation](https://docs.ros.org/en/humble/index.html)

---
