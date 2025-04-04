# VLP-16 (LIDAR)
We are using the VLP-16 lidar puck.

The VLP-16 lidar will be unused from roboboat years 2026 forward.

## how to set up
The lidar outputs `sensor_msgs.msg.PointCloud2` messages to the `/wamv/sensors/lidars/lidar_wamv_sensor/points` topic

## PointCloud2 messages
The (relevant) contents of a PointCloud2 message:
- point_step - # of bytes in a point (msg type: uint32)
- row_step - # of bytes in a row of points (msg type: uint32)
	- calculated by (# of points in a row * point_step)
- fields[] - this is similar to a structure in C++ (msg type `sensor_msgs/PointField`)

### [PointField](http://docs.ros.org/en/noetic/api/sensor_msgs/html/msg/PointField.html)
A fields[] message looks something like this:
```
mypointcloud.fields = [
PointField('x',0,PointField.FLOAT32,1)
PointField('y',4,PointField.FLOAT32,1)
PointField('z',8,PointField.FLOAT32,1)
PointField('intensity',12,PointField.FLOAT32,1)
```
- attribute: a name (such as x,y,z,intensity) 
- offset: the start index
- datatype: 
- count:
