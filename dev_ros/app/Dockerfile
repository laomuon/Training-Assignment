FROM ros:noetic AS builder
SHELL ["/bin/bash","-c"]
RUN apt-get -y update  \
    && apt-get install build-essential \
    && apt-get install nano \
    && source opt/ros/$ROS_DISTRO/setup.bash \
    && mkdir -p ~/catkin_ws/src \
    && cd ~/catkin_ws/ \
    && catkin_make install\
    && source install/setup.bash \
    && cd ~/catkin_ws/src \
    && catkin_create_pkg dev_ros_pkg std_msgs rospy roscpp \
    && catkin_create_pkg another_dev_ros_pkg std_msgs rospy \
    && cd dev_ros_pkg/src/ \
    && mkdir dev_ros_pkg \
    && cd ~/catkin_ws/ \
    && cd src/another_dev_ros_pkg \
    && mkdir srv \
    && mkdir launch \
    && cd ~/catkin_ws/ \
    && catkin_make install\
    && . ~/catkin_ws/install/setup.bash \
    && echo "source ~/catkin_ws/install/setup.bash" >> /.bashrc

COPY cpp_simple_node.cpp /root/catkin_ws/src/dev_ros_pkg/src/cpp_simple_node.cpp
COPY python_simple_node.py /root/catkin_ws/src/dev_ros_pkg/src/python_simple_node.py
COPY add.py /root/catkin_ws/src/dev_ros_pkg/src/dev_ros_pkg/add.py
COPY setup.py /root/catkin_ws/src/dev_ros_pkg/setup.py
COPY another_python_node.py /root/catkin_ws/src/another_dev_ros_pkg/src/another_python_node.py
COPY calc_service.srv /root/catkin_ws/src/another_dev_ros_pkg/srv/calc_service.srv
COPY publish_service.srv /root/catkin_ws/src/another_dev_ros_pkg/srv/publish_service.srv
COPY calc_service_server.py /root/catkin_ws/src/another_dev_ros_pkg/src/calc_service_server.py
COPY calc_service_client.py /root/catkin_ws/src/another_dev_ros_pkg/src/calc_service_client.py
COPY CMakeLists.txt /root/catkin_ws/src/another_dev_ros_pkg/CMakeLists.txt
COPY package.xml /root/catkin_ws/src/another_dev_ros_pkg/package.xml
COPY ros_run.sh /ros_run.sh
COPY launch_file.launch /root/catkin_ws/src/another_dev_ros_pkg/launch/launch_file.launch

RUN source opt/ros/$ROS_DISTRO/setup.bash \
    && cd ~/catkin_ws/ \
    && . ~/catkin_ws/install/setup.bash  \
    && cd ~/catkin_ws/src/dev_ros_pkg \
    && echo "catkin_python_setup()" >> CMakeLists.txt \
    && echo "add_executable(cpp_simple_node src/cpp_simple_node.cpp)" >> CMakeLists.txt \ 
    && echo "target_link_libraries( cpp_simple_node \${catkin_LIBRARIES})" >> CMakeLists.txt \
    && chmod +x src/python_simple_node.py \
    && touch src/dev_ros_pkg/__init__.py \
    && cd ~/catkin_ws/src/another_dev_ros_pkg/ \
    && chmod +x launch/launch_file.launch \
    && chmod +x src/another_python_node.py \
    && chmod +x src/calc_service_server.py \
    && chmod +x src/calc_service_client.py \
    && cd ~/catkin_ws \
    && catkin_make install\
    && . ~/catkin_ws/install/setup.bash 

FROM ros:noetic
WORKDIR /root/
COPY ros_run.sh /ros_run.sh
COPY --from=builder root/catkin_ws/ ./catkin_ws

CMD ["/ros_run.sh"]