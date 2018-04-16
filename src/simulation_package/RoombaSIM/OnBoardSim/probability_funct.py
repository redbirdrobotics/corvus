'''

In the form:
    x^2/a^2 + y^2/b^2 = z^2/c^2
where a is the distance from center to x-axis, b is the distance from center to y-axis and c is the max-height of z.

This is what the probability function is based on, at every delta t the probability decreases by 5 and the radius changes by 0.33.

'''

from OnBoardSim import ROSExtension

import numpy as npy

class probability_funct(object):
    '''
    The class represents a function for probability. What it will do is will take 
    in an x and y coordinate of a roomba and begin creating a gradient of probability.
    This is for the inherent chaos of the system. It will give us an idea of where the 
    roomba will be. Because we do not know the timers of one robot we can only say with 100%
    certainty that it will be in this vicinity.
    '''

    def __init__(self):

        self.ros = ROSExtension()

        self.ros_msg_type = None

        self._pub = self.ros.create_publisher(self.ros_msg_type)

        self.ros.init_ros_node_for_publishing()

        self._probability = 100
		
        self._vel = 0.33 #m/s
        self._max_t = 20
		
	self.time_to_look = 0

        self.max_radius = 6.6 #m

        self.ids_of_collision = []

        self.exceeds_boundary = {
                'goal_line'         : False,
                'left_boundary'     : False,
                'bottom_boundary'   : False,
                'right_boundary'    : False
            }

        self._d_radius = self._vel * self._max_t

        self._radius = 0

    def func(self):
        if self._max_t > 0 and self._radius <= 6.6:

            self._max_t -= 1

            self._radius += self._d_radius

            self._probability -= 5         
            
