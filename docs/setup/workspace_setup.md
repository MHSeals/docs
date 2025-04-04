# Workspace setup
## prerequisites
- Ubuntu 22.04 (see [installing ubuntu 22.04](installing_ubuntu.md)) -- NO WSL!
- All the instructions below are made for both Ubuntu 22.04 and 20.04
- At least 8 gigabytes of ram

## setup
1. Follow the instructions for install ros2 on your system at the official website [docs.ros.org](https://docs.ros.org/en/humble/Installation.html)
2. create a new directory (`mkdir roboboat_ws`)
3. enter into directory, run `colcon build`
4. create a src folder (`mkdir src`)
5. install packages in the src directory
    1. [mhsboat_ctrl](https://github.com/MHSeals/mhsboat_ctrl) -- `git clone https://github.com/MHSeals/mhsboat_ctrl`

your basic workspace should have a tree similar to this when you are finished:
```
- roboboat_ws
  - build
  - install
  - log
  - src
    - mhsboat_ctrl
```
