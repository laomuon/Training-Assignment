#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "Message: ", data.data)

def python_simple_node():
    rospy.init_node('python_simple_node',anonymous=True)
    rospy.Subscriber("chatter",String,callback)
    rospy.spin()

if __name__ == '__main__':
    python_simple_node()
