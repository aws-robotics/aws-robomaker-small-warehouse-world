cmake_minimum_required(VERSION 3.5)
project(aws_robomaker_small_warehouse_world)

find_package(ament_cmake_auto REQUIRED)

ament_environment_hooks("${CMAKE_CURRENT_SOURCE_DIR}/env-hooks/aws_robomaker_small_warehouse_world.dsv.in")

ament_auto_package(INSTALL_TO_SHARE launch maps models rviz worlds)
