# Master Launch package
Acts as the main launch file for the warehousebot. It would launch the following programs: 
- labview goal manager
- main nav2 stack
- lidar auto docking
- map to base link publisher
- lidar polar points publisher

## Launch without sensor fusion
~~~
ros2 launch master_launch master.launch.py
~~~

## Launch with sensor fusion
~~~
ros2 launch master_launch master_fusion.launch.py
~~~
