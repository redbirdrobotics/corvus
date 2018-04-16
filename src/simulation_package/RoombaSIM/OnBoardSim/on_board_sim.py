#!/usr/bin/python

from roomba import roomba
from ROSExtension import ROSExtension
import util
from simulation_package.msg import Num
import rospy

class On_Board_Sim():

    def __init__(self):
        self.list_of_active_roombas = []

        self.ros = ROSExtension()

        self.ros.init_ros_node('On_Board_Simulation')

        self.ros.create_listener('Differentiate_Roombas', self.listener_for_roombas, Num)

    def listener_for_roombas(self, ros_msg):
        ground_roomba = roomba()

        ground_roomba.pos = ros_msg.x, ros_msg.y

        ground_roomba.id = ros_msg.id

        self.update_active_roombas(ground_roomba)

    def update_active_roombas(self, roomba):

        for target in self.list_of_active_roombas:

            if util.circle_intersects_circle(target.pos, roomba.pos, roomba.max_radius):

                self.collided(roomba, target)

            if(util.circle_intersects_goal(roomba.pos, roomba.max_radius)):
                roomba.exceeds_boundary['goal_line'] = True
  		roomba.time_to_look = util.min_time(roomba.pos, 0)

            if(util.circle_intersects_rboundary(roomba.pos, roomba.max_radius)):
                roomba.exceeds_boundary['right_boundary'] = True
    		roomba.time_to_look = util.min_time(roomba.pos, 1)

            if(util.circle_intersects_bboundary(roomba.pos, roomba.max_radius)):
                roomba.exceeds_boundary['bottom_boundary'] = True
    		roomba.time_to_look = util.min_time(roomba.pos, 2)

            if(util.circle_intersects_lboundary(roomba.pos, roomba.max_radius)):
                roomba.exceeds_boundary['left_boundary'] = True
    		roomba.time_to_look = util.min_time(roomba.pos, 3)

            self.list_of_active_roombas.append(roomba)

    def collided(self, roomba_a, roomba_b):

        roomba_a.ids_of_collision.append(roomba_b.id)

        roomba_b.ids_of_collision.append(roomba_a.id)

    def start_sim(self):

        while not rospy.is_shutdown():

            for roomba in self.list_of_active_roombas:

                roomba.update()

            rospy.sleep(1)

if __name__ == '__main__':

    Sim = On_Board_Sim()

    Sim.start_sim()
