#!/usr/bin/env python

from ROSExtension import ROSExtension
from simulation_package.msg import Sim
import numpy as np
import rospy

# TODO: Configure message to have a boolean variable for: Int for the id of the other robot(s) collision.

class robot(object):
    
    def update(self):
        
        raise NotImplementedError()

class roomba(robot):
    def __init__(self):

       self.pos = None

       self.header = None

       self.id = None

       self.ros = ROSExtension()

       self.ros_msg_type = Sim()

       self.ros.create_publisher('Roomba',Sim)

       self._probability = 100

       self._vel = 0.33 #m/s
       self._max_t = 20

       self.max_radius = 6.6 #m

       self._min_distance = 0.99 #m

       self.ids_of_collision = []

       self.exceeds_boundary = {
               'goal_line'         : False,
               'left_boundary'     : False,
               'bottom_boundary'   : False,
               'right_boundary'    : False
           }

       self._d_radius = self._vel * 1

       self._radius = 0

       self._points_of_interest = []

       self.time_to_look = 0
    
       self.am_i_seen = False

    def generate_props(self):

       return { 'id' : self.id,
                 'pos' : self.pos
              }

    def populate_publish_roomba_msg(self):

        self.ros_msg_type.x, self.ros_msg_type.y = self.pos

        self.ros_msg_type.id = self.id

        self.ros_msg_type.prob = self._probability

        self.ros_msg_type.gl = self.exceeds_boundary['goal_line']

        self.ros_msg_type.lb = self.exceeds_boundary['left_boundary']

        self.ros_msg_type.bb = self.exceeds_boundary['bottom_boundary']

        self.ros_msg_type.rb = self.exceeds_boundary['right_boundary']
		
	self.ros_msg_type.time = self.time_to_look

        rospy.loginfo(self.ros_msg_type)

        self.ros._pub.publish(self.ros_msg_type)

    def update(self):

      if self._max_t > 0 and self._radius <= 6.6:

            self._max_t = self._max_t - 1
			
            self.time_to_look -= 1

            self._radius = self._radius + self._d_radius

            self._probability = self._probability - 5

            self.populate_publish_roomba_msg()

class target_roomba(robot):
    def __init__(self):

      self.pos 

      self.heading

      self.vel = 0.33 #m/s

      self.id

    def update(self):
      
      self.pos[0] += self.vel * np.cos(self.heading) * delta
      self.pos[1] += self.vel * np.sin(self.heading) * delta

      # reorient so we tangent to a circle centered at the origin
      ang = np.arctan2(10 - self.pos[1], 10 - self.pos[0])
      self.heading = ang + (np.pi / 2)
