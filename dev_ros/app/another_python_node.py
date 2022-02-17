#!/usr/bin/env python3
import rospy
from std_msgs.msg import String
from dev_ros_pkg.add import add

def talker():
    pub = rospy.Publisher('chatter', String, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10)
    i=0
    while not rospy.is_shutdown():
        
        hello_str = "increment add %s" % add(i,i+1)
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        rate.sleep()
        i=i+1
if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
