FROM ros:noetic

RUN /bin/bash -c "apt-get -y update  \
    && apt-get install build-essential \
    && apt-get install nano \
    && source opt/ros/$ROS_DISTRO/setup.bash \
    && mkdir -p ~/catkin_ws/src \
    && cd ~/catkin_ws/ \
    && catkin_make install\
    && source devel/setup.bash \
    && cd ~/catkin_ws/src \
    && catkin_create_pkg dev_ros_pkg std_msgs rospy roscpp \
    && cd ~/catkin_ws/ \
    && catkin_make install\
    && . ~/catkin_ws/devel/setup.bash"

COPY cpp_simple_node.cpp /root/catkin_ws/src/dev_ros_pkg/src/cpp_simple_node.cpp
COPY python_simple_node.py /root/catkin_ws/src/dev_ros_pkg/src/python_simple_node.py


RUN /bin/bash -c "source opt/ros/$ROS_DISTRO/setup.bash \
#    && chmod +x ~/catkin_ws/src/dev_ros_pkg/src/dev_ros_pkg/add.py \
    && cd ~/catkin_ws/ \
    && catkin_make \
    && cd ~/catkin_ws/src/dev_ros_pkg \
    && echo 'add_executable(cpp_simple_node src/cpp_simple_node.cpp)' >> CMakeLists.txt \ 
    && echo 'target_link_libraries( cpp_simple_node \${catkin_LIBRARIES})' >> CMakeLists.txt \
    && chmod +x src/python_simple_node.py \
#    && echo 'add_executable(python_simple_node src/python_simple_node.py)' >> CMakeLists.txt \ 
#    && echo 'target_link_libraries( python_simple_node \${catkin_LIBRARIES})' >> CMakeLists.txt \
    && cd ~/catkin_ws \
    && catkin_make \
    && . ~/catkin_ws/devel/setup.bash "


COPY ros_entrypoint.sh /ros_entrypoint.sh
COPY ros_run.sh /ros_run.sh
RUN chmod +x ros_entrypoint.sh
RUN chmod +x ros_run.sh
#ENTRYPOINT ["/ros_entrypoint.sh"]

CMD ["/ros_run.sh"]