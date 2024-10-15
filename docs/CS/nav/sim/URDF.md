---
descripton: Information about URDF
documentation: definitely not a paywalled resource online
---

URDF = Unified Robot Description Format
- used to generate [TFs](tf2.md)

## making a urdf file
urdf files end with .urdf and are in XML format
```xml
< ?xml version="1.0?">
<robot name="myrobot"> 
	<!-- your links and joints go here! -->
</robot>
```
### link
```xml
<link name="base_link">
	<visual> <!-- physical properties -->
		<geometry>
			<box size=".2 .4 .6"/> <!-- in meters -->
		</geometry>
		<origin xyz="0 0 0" rpy="0 0 0"/>
		<material name="orange">
	</visual>
</link>
```
- visual = visual propertries of a link
	- you will need to include a geometry tag to create shapes
		- box size property: measured in meters, size in XYZ
		- material name property: defines color
	- origin: defines the offset of the visual (geometry)
		- use joints to move a link relative to another instead
		- XYZ - determines position
		- RPY = Roll (X axis), Pitch (Y axis), Yaw (Z axis) - determines rotation
### joint
```xml
<joint name="my_cool_joint" type="fixed">
	<parent link="mom"/>
	<child link="son"/>
	<origin xyz="0 0 0.5" rpy="0 0 0"/>
</joint>
```
* join property type:
* the origin tag here represents the child's offset relative to the parent