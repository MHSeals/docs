# MAVROS
## SetMode
- create a `mavros_msgs.srv.SetMode` client for the `/mavros/set_mode` topic
	- Mode options: `MANUAL`, `GUIDED`, `HOL`

## thrusters
- publish a `geometry_msgs.msg.TwistStamped` message to the `/mavros/setpoint_velocity/cmd_vel` to control speed

### TwistStamped messages
ie. twist message named 'mymessage':
- Linear velocity can be modified with `mymessage.twist.linear.[x(forwards)/y(backwards)]`
	- measured in m/s
- Angular velocity (rotating the boat) can be modified with `mymessage.twist.angular.z`
	- mesured in rad/s

