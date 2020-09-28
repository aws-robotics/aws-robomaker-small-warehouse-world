import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.conditions import IfCondition
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration


def generate_launch_description():
    # Launch configuration variables
    use_gui = LaunchConfiguration('gui')

    # Declare launch arguments
    declare_use_gui_cmd = DeclareLaunchArgument(
        'gui',
        default_value='false',
        description='Whether to launch gazebo client')

    # Path variable for included launch files
    gazebo_launch_path = os.path.join(get_package_share_directory('gazebo_ros'), 'launch')
    
    # Path to world file
    aws_warehouse_pkg_dir = get_package_share_directory('aws_robomaker_small_warehouse_world')
    
    # Gzserver launch
    gazebo_server_cmd = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            [gazebo_launch_path, '/gzserver.launch.py']),
        launch_arguments={'world': os.path.join(
            aws_warehouse_pkg_dir, 'worlds', 'small_warehouse.world')}.items()
    )

    # Gzclient launch
    gazebo_client_cmd = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([gazebo_launch_path, '/gzclient.launch.py']),
        condition=IfCondition(use_gui),
        launch_arguments={}.items()
    )

    ld = LaunchDescription()

    # Declare launch options 
    ld.add_action(declare_use_gui_cmd)

    # Declare gazebo action
    ld.add_action(gazebo_server_cmd)
    ld.add_action(gazebo_client_cmd)

    return ld
