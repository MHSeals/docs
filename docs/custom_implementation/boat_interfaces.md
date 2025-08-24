[](){ #boat-interfaces }
# Custom ROS2 Messages for MHSeals Boat (boat_interfaces)

This page documents the `boat_interfaces` repository, which provides custom ROS2 message definitions essential for the MHSeals boat control system and related packages.

---

## Overview

- **Repository:** [MHSeals/boat_interfaces](https://github.com/MHSeals/boat_interfaces)
- **Main Language:** ROS2 message definition (IDL)
- **Framework:** ROS 2 Humble
- **Purpose:** Defines custom messages for inter-node communication in MHSeals boat software

---

## Features & Usage

- Provides all custom message types required by the MHSeals boat control system and related packages (e.g., `mhsboat_ctrl`, `buoy_recognition`, etc).
- Enables structured communication between nodes for sensor data, task status, and control commands.
- Ensures compatibility and modularity across the MHSeals ROS2 ecosystem.

---

## How to Use

### 1. Clone the Repository
```bash
git clone https://github.com/MHSeals/boat_interfaces.git ~/ros_ws/src/boat_interfaces
```

### 2. Build the Messages
- Build your ROS2 workspace to generate message headers:
```bash
cd ~/ros_ws
colcon build --symlink-install --packages-select boat_interfaces
```

### 3. Add as a Dependency
- Add `boat_interfaces` to your package's `package.xml` and `setup.py` (if using Python).
- Import and use the custom messages in your ROS2 nodes.

---

## Example Messages

- (Refer to the repository for the full list and definitions)
- Typical messages may include:
  - Sensor data (e.g., processed LiDAR, camera detections)
  - Task status and completion
  - Control commands for actuators

---

## Integration

- Required by the MHSeals boat control system (`mhsboat_ctrl`) and other related packages.
- Ensures all nodes can communicate using a shared set of message types.

---

## References & Links

- [MHSeals/boat_interfaces GitHub](https://github.com/MHSeals/boat_interfaces)
- [ROS 2 Custom Messages Documentation](https://docs.ros.org/en/humble/How-To-Guides/Custom-ROS2-Interfaces.html)

---
