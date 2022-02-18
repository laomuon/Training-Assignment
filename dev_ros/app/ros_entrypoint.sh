#!/bin/bash
set -e

source "/opt/ros/$ROS_DISTRO/setup.bash" &&
cd ~/catkin_ws/  &&
. ~/catkin_ws/devel/setup.bash &&
exec "$@"
