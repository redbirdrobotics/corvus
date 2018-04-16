#!/usr/bin/env python
import rospy
from simulation_package.msg import NumMap, Num

class ROSExtension(object):
    '''
    Any message population and publishing will need to be 
    called every iteration as this will be used to communicate
    with ROS. Adding this to the environment file will be fine.

    In its current state, this is an all purpose class, one instance
    for a simulation is needed. Every time you pass an instance of a drone
    or roomba to the msg, you will populate a blank message and 
    then publish it.

    Acts as a mediator between the simulation and ROS.
    '''

    def __init__(self, node_name):
        # Create map listener
        self.target_roomba_ros = None

        self.obstacle_roomba_ros = None

        self.msgMap = []

        self.msgNumMap = NumMap()

        self.msg = Num()

        #initialize node
        rospy.init_node(node_name, anonymous=True)
        
    def create_target_roomba_publisher(self):
        self.target_roomba_ros = rospy.Publisher('Target_Roomba', NumMap, queue_size=100000000)

    def create_obstacle_roomba_publisher(self):
        self.obstacle_roomba_ros = rospy.Publisher('Obstacle_Roomba', NumMap, queue_size=100000000)

    def populate_publish_tr_msg(self, roomba):

        '''
        self.msg.x, self.msg.y = roomba.pos

        self.msg.id = roomba.tag
        '''

        rospy.loginfo('populate_publish_tr_msg was called')

        for rba in roomba:

            self.msg.x, self.msg.y = rba.pos

            self.msg.id = rba.tag

            self.msgMap.append(self.msg)

            rospy.loginfo('populating msg')


        self.msgNumMap.numMap = self.msgMap

        if not rospy.is_shutdown():

            rospy.loginfo('publishing the message')

            self.target_roomba_ros.publish(self.msgNumMap)

            rospy.loginfo(self.msgNumMap)

        del self.msgMap[:]

    def populate_publish_or_msg(self, roomba):

        self.msg.x, self.msg.y = roomba.pos

        self.msg.id = roomba.tag

        if not rospy.is_shutdown():

            self.obstacle_roomba_ros.publish(self.msg)

    def logInfo(self, msg):

        rospy.loginfo(msg)
