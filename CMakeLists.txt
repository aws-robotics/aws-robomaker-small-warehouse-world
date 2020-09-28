cmake_minimum_required(VERSION 3.5)
project(aws_robomaker_small_warehouse_world)

find_package(ament_cmake REQUIRED)

find_package(gazebo_ros_pkgs REQUIRED)

set(dependencies
  gazebo_ros_pkgs
)

install(DIRECTORY launch models worlds maps rviz
  DESTINATION share/${PROJECT_NAME}
)

ament_package()