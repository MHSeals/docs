# Roboboat Workspace Setup

Set up your ROS2 development workspace on Ubuntu for Roboboat projects.

---

## Prerequisites

- **Ubuntu 22.04** ([installation guide](installing_ubuntu.md))  
  *Do not use WSL! It will not work!*
- **8GB RAM** (minimum)

---

## Step-by-Step Setup

### 1. Install ROS2
Follow the official instructions for [ROS2 Humble](https://docs.ros.org/en/humble/Installation.html).

### 2. Create Your Workspace
Open a terminal and run:
```bash
mkdir -p ~/roboboat_ws/src
cd ~/roboboat_ws
```

### 3. Clone Required Packages
Inside the `src` folder, clone the main control package and interfaces:
```bash
cd src
git clone https://github.com/MHSeals/mhsboat_ctrl
git clone https://github.com/MHSeals/boat_interfaces
```

### 4. Build the Workspace
Return to the workspace root and build:
```bash
cd ~/roboboat_ws
colcon build --symlink-install
```

### 5. Source the Workspace
After building, run:
```bash
source install/setup.bash
```

Edit your `.bashrc` and add the following line to source automatically:
```bash
source ~/roboboat_ws/install/setup.bash
```

---

## Workspace Structure Example

Your workspace should look like this:
```text
roboboat_ws/
├── build/
├── install/
├── log/
└── src/
    ├── mhsboat_ctrl/
    └── boat_interfaces/
```

---

## Tips & Troubleshooting

- If you see build errors, check that all ROS2 dependencies are installed.
- Always run `source install/setup.bash` in each new terminal before using ROS2 commands. (You can add this to your `.bashrc` to automate it.)
- To add more packages, clone them into `src` and rebuild with `colcon build`.
- For help, see the [ROS2 documentation](https://docs.ros.org/en/humble/index.html) or ask a team member.

---
