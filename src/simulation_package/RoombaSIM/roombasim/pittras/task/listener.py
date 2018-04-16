#!/usr/bin/env python

import rospy
from beginner_tutorials.msg import Num 

# def callback(data):
#     rospy.loginfo(rospy.get_caller_id() + 'I heard %s, %s', str(data.x), str(data.y))

# def listener():

#     # In ROS, nodes are uniquely named. If two nodes with the same
#     # name are launched, the previous one is kicked off. The
#     # anonymous=True flag means that rospy will choose a unique
#     # name for our 'listener' node so that multiple listeners can
#     # run simultaneously.
#     rospy.init_node('listener', anonymous=True)

#     rospy.Subscriber('chatter', Num, callback)

#     # spin() simply keeps python from exiting until this node is stopped
#     rospy.spin()

# if __name__ == '__main__':
#     listener()

class ROSListener():

    def __init__(self):
        self.msg = None

    def callback(self, msg):
        rospy.loginfo(rospy.get_caller_id() + 'I head %s, %s', str(msg.x), str(msg.y))

    def listen(self):
        rospy.init_node('listener', anonymous=True)

        rospy.Subscriber('chatter', Num, self.callback)

        rospy.spin()


def main():
    rosextension = ROSListener()

    rosextension.listen()

if __name__ == '__main__':
    main()