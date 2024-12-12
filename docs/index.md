# index

if you're new here and don't know where to start, check out the [ros2](./starting/ros2.md) and [setting up your workspace](./setup/setting_up_your_workspace.md) pages.

## problems (and hopefully, solutions)
from [bryan's issue](https://github.com/MHSeals/mhsboat_ctrl/issues/45):

1. Use LIDAR to cluster pointclouds into buoys and positions
2. Use (lidar/cubeorange imu) odometry to backtrack in case of error
3. Use camera to identify buoy types

note: NO PWM signals, already covered by /cmd_vel topic  
note 2: no slam either

### challenges

1. challenge 1: set midpoint between 2 pairs of red/green buoys, use laser in direct path of boat to guide tuppy to midpoint
2. challenge 2: challenge 1, but find the largest gap and go to its midpoint instead
