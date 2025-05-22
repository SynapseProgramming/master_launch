import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, PythonExpression
from launch_ros.actions import Node
from launch.actions import SetEnvironmentVariable
from launch.conditions import IfCondition, UnlessCondition


def generate_launch_description():
    current_dir = get_package_share_directory("master_launch")
    wmr_nav2_dir = get_package_share_directory("warehousebot_navigation")
    goal_plotter_dir = get_package_share_directory("goal_plotter")
    lidar_autodock_dir = get_package_share_directory("lidar_auto_docking")
    map_to_baselink_dir = get_package_share_directory("map_to_base_link")

    ld = LaunchDescription()

    #launch warehouse bot navigation
    launch_nav2 = IncludeLaunchDescription(
    	PythonLaunchDescriptionSource(
            os.path.join(wmr_nav2_dir, "launch","master.launch.py" )
  	),
    )
    
    #launch_nav2 = IncludeLaunchDescription(
    #	PythonLaunchDescriptionSource(
    #        os.path.join(wmr_nav2_dir, "launch","master_fusion.launch.py" )
  	#),
    #)


    #launch goal manaer
    launch_goal_manager = IncludeLaunchDescription(
    	PythonLaunchDescriptionSource(
            os.path.join(goal_plotter_dir, "launch","goal_manager.launch.py" )
  	),
    )

    # launch auto docking
    launch_auto_docking = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(lidar_autodock_dir, "launch", "nav2_dock.launch.py")
        ),
    )
    # launch map to base_link
    launch_map_to_base_link = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(map_to_baselink_dir, "launch", "map_to_base_link.launch.py")
        ),
    )

    # run lidar publisher
    run_lidar_publisher = Node(
    	package = "lidar_publisher",
    	executable = "laser_reader",
    	output="screen",
    )

    ld.add_action(launch_nav2)
    ld.add_action(launch_goal_manager)
    ld.add_action(launch_auto_docking)
    ld.add_action(launch_map_to_base_link)
    ld.add_action(run_lidar_publisher)
    return ld
