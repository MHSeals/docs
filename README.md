if you're new here and don't know where to start, check out the [[ros2]] and [[setting up your workspace]] pages.

## problems (and hopefully, solutions)
1. we want to connect all of our hardware together have have a platform for all of them to communication to each other!
	* solution: [[ros2]].
2. taking out our boat every time we want to test code is such a pain!
	* solution: [[gazebo]] and [[vrx]].
### the navigation issue
1. use relative coordinates to build a map relative to our boat -- [[slam_toolbox]]
2. use our lidar to calculate odometry -- [[kiss_icp]]
3. profit?