[](){ #slam-toolbox }
# slam_toolbox
slam_toolbox is a package we use to implement the SLAM algorithm in roboboat :)

[bryan's documentation](https://docs.google.com/document/d/1msz3Z5DdcRVLMJXQrmZ61iGfAP3T2CpFbgfcOO_6OnA/edit)
## what is slam?
slam stands for Simultaneous Localization and Mapping… but what does that mean?!
* **localization**: positioning yourself relative to a map without global positioning (like gps)
* **mapping**: exploring surroundings and using the data to form a map
* **slam** = localizing and mapping at the same time!

## how to use slam_toolbox
* slam_toolbox subscribers to data from `/tf` and `/scan`
* `/odom` and `/laser` topics need to be linked in the `/tf` tree

### installation
1. update your system
`sudo apt update && sudo apt upgrade`
2. install slam_toolbox
`sudo apt install ros-humble-slam-toolbox`
3. build your packages
`colcon build`

now you can run slam_toolbox with the code below!
`ros2 launch slam_toolbox online_async_launch.py use_sim_time:=True`
* this command runs slam_toolbox in online asynchronous mode

### configuration
slam_toolbox comes with template default config files you can copy and modify
this code below will copy one of the template files to your current working directory
`cp /opt/ros/humble/share/slam_toolbox/config/mapper_params_online_async.yaml .`

## rviz and slam_toolbox
### view slam_toolbox data
1. open rviz
`ros2 launch vrx_gazebo rviz.launch.py`
2. add a laserscan node
3. profit?
### slam_toolbox rviz plugin
1. open rviz
`ros2 launch vrx_gazebo rviz.launch.py`
2. Menu bar (top left corner) -> Panels -> Add New Panel
3. You should now see the SlamToolboxPlugin panel in the list of panels!
