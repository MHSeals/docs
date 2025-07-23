# Roboboat Hardware Overview

This page provides a summary of the main hardware components used in the Roboboat project. For detailed setup and usage instructions, see the linked documentation for each device.

---

## Main Components

- **NVIDIA Jetson Xavier NX**  
    High-performance onboard computer for AI, vision, and ROS2 nodes.
    
    [Read more &rarr;](./jetson_xavier_nx.md)

- **Odroid**  
    Secondary processing unit for additional ROS2 nodes that do not require high GPU performance.

    [Read more &rarr;](./odroid.md)

- **Cube Orange**  
    Flight controller used for IMU and motor outputs.

    [Read more &rarr;](./cubeorange.md)

- **VLP-16 LIDAR**  
    3D laser scanner for mapping and obstacle detection.  

    [Read more &rarr;](./vlp16.md)

- **Onboard Network**  
    Managed by a router, with Ubiquiti Bullet (boat WiFi) and Rocket (shore WiFi).  

    [Read more &rarr;](./network.md)

---

## Notes

- All mission-critical computers are hardwired to the onboard network for reliability.
- Hardware may change over time; check individual pages for up-to-date info.

---
