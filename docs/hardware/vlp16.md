[](){ #vlp16 }
# Velodyne VLP-16 (LIDAR)

The VLP-16 is a 3D LIDAR sensor used for robotics and mapping. Note: The VLP-16 will be unused for Roboboat projects from 2026 onward.

---

## Hardware Setup

1. **Power the LIDAR** using the included adapter.
2. **Connect the LIDAR to your computer via Ethernet.**
3. Make sure your computer's Ethernet port is configured to communicate with the sensor (check your network settings).

---

## ROS Integration

- Install the official [velodyne ROS driver](http://wiki.ros.org/velodyne) or use community packages like [`velodyne_ros_tools`](https://github.com/Ikhyeon-Cho/velodyne_ros_tools).
- The VLP-16 publishes `sensor_msgs/msg/PointCloud2` messages, typically to `/wamv/sensors/lidars/lidar_wamv_sensor/points` or `/velodyne_points`.
- To view data, use RViz and add a PointCloud2 display.

---

## PointCloud2 Message Structure

Relevant fields:
- **point_step**: Number of bytes per point (`uint32`)
- **row_step**: Number of bytes per row (`uint32`)
  - Calculated as (# of points in a row × point_step)
- **fields[]**: Array describing each attribute in a point (see [PointField](http://docs.ros.org/en/noetic/api/sensor_msgs/html/msg/PointField.html))

Example:
```python
mypointcloud.fields = [
	PointField('x', 0, PointField.FLOAT32, 1),
	PointField('y', 4, PointField.FLOAT32, 1),
	PointField('z', 8, PointField.FLOAT32, 1),
	PointField('intensity', 12, PointField.FLOAT32, 1)
]
```
- **attribute**: Name (e.g., x, y, z, intensity)
- **offset**: Start index in the point structure
- **datatype**: Data type (e.g., FLOAT32)
- **count**: Number of elements

---

## Troubleshooting & Tips

- If you don't see data in RViz, check your Ethernet connection and ensure the driver is running.
    - Make sure the IP and port configuration in the Velodyne's configuration web interface are correct.
- For ROS2 Humble, you may need to convert or adapt drivers/packages.
- Refer to the [VLP-16 User Manual](https://docs.clearpathrobotics.com/assets/files/clearpath_robotics_029029-TDS2-00b7913d65b51a841cb5dc6c2b711487.pdf) for hardware details.

---
