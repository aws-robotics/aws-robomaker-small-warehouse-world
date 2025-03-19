# Copyright (c) 2018 Intel Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, ExecuteProcess
from launch.substitutions import LaunchConfiguration
from launch.actions import SetEnvironmentVariable


def generate_launch_description():
    # Get the launch directory
    aws_small_warehouse_dir = get_package_share_directory('aws_robomaker_small_warehouse_world')
    
    # Launch configuration variables specific to simulation

    world = LaunchConfiguration('world')

    declare_use_sim_time_cmd = DeclareLaunchArgument(
        'use_sim_time',
        default_value='True',
        description='Use simulation (Gazebo) clock if true')

    declare_simulator_cmd = DeclareLaunchArgument(
        'headless',
        default_value='False',
        description='Whether to execute gzclient)')

    declare_world_cmd = DeclareLaunchArgument(
        'world',
        default_value=os.path.join(aws_small_warehouse_dir, 'worlds', 'small_warehouse', 'small_warehouse.world'),
        description='Full path to world model file to load')

    model_path = os.path.join(aws_small_warehouse_dir, 'models')

    gazebo_server_cmd_line = [
        'gz', 'sim', '-r', '-v4', world]

    gazebo = ExecuteProcess(
        cmd=gazebo_server_cmd_line, output='screen')

    # Create the launch description and populate
    ld = LaunchDescription()

    # Declare the launch options
    ld.add_action(declare_use_sim_time_cmd)
    ld.add_action(declare_simulator_cmd)
    ld.add_action(declare_world_cmd)
    ld.add_action(SetEnvironmentVariable('GZ_SIM_RESOURCE_PATH', model_path))
    # Add any conditioned actions
    ld.add_action(gazebo)

    return ld
