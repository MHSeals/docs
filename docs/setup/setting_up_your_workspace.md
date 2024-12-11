## prerequisites
- Ubuntu 22.04 (see [installing ubuntu 22.04](installing_ubuntu.md)) -- NO WSL!
- all the instructions below are made for and only ubuntu 22.04
- at least 8 gigabytes of ram

## setup
1. create a new directory (`mkdir roboboat_ws`)
2. enter into directory, run `colcon build`
3. create a src folder (`mkdir src`)
4. install packages in the src directory
    1. [mhsboat_ctrl](https://github.com/MHSeals/mhsboat_ctrl) -- `git clone https://github.com/MHSeals/mhsboat_ctrl`
    2. [kiss-icp](https://github.com/PRBonn/kiss-icp) -- `git clone https://github.com/PRBonn/kiss-icp`


your basic workspace should have a tree similar to this when you are finished:
```
- roboboat_ws (root)
  - build
  - install
  - log
  - src
    - mhsboat_ctrl
    - kiss-icp
```

## basic commands
1. update your packages by running `colcon build` in your root directory
1. run [gazebo](gazebo.md) using the command `ros2 launch vrx_gz competition.launch.py`
2. run [vrx](vrx.md) using the command `ros2 launch vrx_gazebo rviz.launch.py`
