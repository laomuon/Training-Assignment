#!/usr/bin/env python3
from __future__ import print_function
import rospy
from dev_ros_pkg.add import add
from std_msgs.msg import String
from another_dev_ros_pkg.srv import calc_service,calc_serviceResponse,publish_service,publish_serviceResponse

def handle_calc(req):
    gain=rospy.get_param('/gain')
    print("Parameter gain is %s"%gain)
    print("Returning [(%s + %s) * %s = %s]"%(req.x, req.y, gain, (req.x+req.y)*gain))
    return calc_serviceResponse((req.x+req.y)*gain)

def handle_publish(req):
    try:
        pub=rospy.Publisher('chatter',String,queue_size=10)
        rate=rospy.Rate(100)
        if req.num > 0 :
            i=0
            print("Publish %s messages to topic"%req.num)
            while not (rospy.is_shutdown() or i == req.num):
                pub_str="hello world %s" %rospy.get_time()
                pub.publish(pub_str)
                i=i+1
                rate.sleep()
            return publish_serviceResponse("Ok")
        else:
            print("Number invalid, must be positive")
            return publish_serviceResponse("Failed")
    except rospy.ROSInterruptException:
        return publish_serviceResponse("Failed")
def calc_service_server():
    pub=rospy.Publisher('chatter',String,queue_size=10)
    rospy.init_node('calc_service_server')
    
    s=rospy.Service('calc_service',calc_service,handle_calc)
    s2=rospy.Service('publish_service',publish_service,handle_publish)
    print("Ready")
    rospy.spin()

if __name__ == "__main__":
    calc_service_server()
