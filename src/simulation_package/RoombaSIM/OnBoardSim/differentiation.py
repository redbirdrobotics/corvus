#!/usr/bin/python
import util
from ROSExtension import ROSExtension
import rospy
#import logging
from simulation_package.msg import Num, NumMap
#from drone_loc import DroneLoc

class Differentiate_Roombas(object):
	
	def __init__(self):
		
		self.active_roombas = []
		
		self.non_active_roombas = []
		
		self.ros = ROSExtension()
		
		self.ros.init_ros_node('Differentiation_Simulation')

        	#self.ros.create_listener('localization_node', self.callback_for_localization, localization)

        	self.ros.create_listener('Target_Roomba', self.callback_for_localization, NumMap)

		#self.logger = logging.basicConfig(filename='on_board_sim.log', level=logging.DEBUG)
		
		self.ros.create_publisher('Differentiate_Roombas', Num)
		
		self.msg_for_sim = Num()

		#self.droneLoc = DroneLoc()
		
		self.drone_coors = None

		
	def differentate_roombas(self, input_roombas, active_roombas):

		curr_count = 0
		
		index_to_remove = 0
		
		if len(active_roombas) > 0:
		
			rospy.loginfo('There were roombas')
		
			for i in range(0, len(input_roombas)):

				i_roomba = input_roombas[i]

				for j in range(0, len(active_roombas)):

					a_roomba = active_roombas[j]

					if a_roomba.x - i_roomba.x < 0.01 and a_roomba.y - i_roomba.y < 0.01:

						curr_count+=1
						
						rospy.loginfo('We already found that one! We have found: %s' % str(curr_count))
						
						if(curr_count + (len(active_roomba) - 1) > input_roombas):
							
							rospy.loginfo('Something went wrong, there are too many seen roombas')
						
						a_roomba.x, a_roomba.y = i_roomba.x, i_roomba.y

						self.active_roomba.append(a_roomba)

						del a_roomba[i]
						
			if len(active_roombas) >= 1:

				self.non_active_roombas = active_roombas
				
				rospy.loginfo(" We have no more active roombas, this means that we SHOULD be calling populat_ros_msg() ")
						
		else:
			
			rospy.loginfo('No roombas')
			
			self.active_roombas = input_roombas
			
		if len(self.non_active_roombas) > 0:
			
			self.populate_ros_msg()
					
	def callback_for_localization(self, seen_roomba):

		rospy.loginfo('I got called')
		
		self.differentate_roombas(seen_roomba.numMap, self.active_roombas)
		
	def loop_till_ros_ends(self):
		
		rospy.spin()
		
	def populate_ros_msg(self):
		
		rospy.loginfo( "Good, we got called! This means that the contents for non_active_roombas will be sent to the other sim! " )
		
		for robot in self.non_active_roombas:
			
			#self.drone_coors = self.droneLoc.get_coors()
			
			self.msg_for_sim.x, self.msg_for_sim.y = robot.x , robot.y 
			
			self.msg_for_sim.id = robot.id
			
			self.ros.send_msg(self.msg_for_sim)

			rospy.loginfo('sent the message!')
		
if __name__ == '__main__':
	
	Diff = Differentiate_Roombas()
	
	rospy.spin()
