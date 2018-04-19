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

		'''

		curr_count = 0
		
		index_to_remove = 0

		skipped = 0
		
		if len(active_roombas) > 0:
		
			rospy.loginfo('There were roombas')
		
			for i_roomba in input_roombas:

				#i_roomba = input_roombas[i]

				if not i_roomba.x == -1 and i_roomba.y == -1 and i_roomba.id == -1:

					for a_roomba in active_roombas:

						#a_roomba = active_roombas[j]

						if a_roomba.x - i_roomba.x < 0.01 and a_roomba.y - i_roomba.y < 0.01:

							curr_count+=1
							
							rospy.loginfo('We already found that one! We have found: %s' % str(curr_count))
							
							if(curr_count + (len(active_roombas) - 1) > input_roombas):
								
								rospy.loginfo('Something went wrong, there are too many seen roombas')
							
							a_roomba.x, a_roomba.y = i_roomba.x, i_roomba.y

							self.active_roombas.append(a_roomba)

							#del a_roomba[i]

				else:

					skipped+=1

					rospy.loginfo("We skipped this many times: ")

					rospy.loginfo(str(skipped))

					#continue
						
			if len(active_roombas) >= 1:

				self.non_active_roombas = active_roombas
				
				rospy.loginfo(" We have no more active roombas, this means that we SHOULD be calling populat_ros_msg() ")
						
		else:
			
			rospy.loginfo('No roombas')

			for i_roomba in input_roombas:

				rospy.loginfo(i_roomba)

				rospy.loginfo(i_roomba.x == -1 and i_roomba.y == -1 and i_roomba.id == -1)

				if not i_roomba.x == -1 and i_roomba.y == -1 and i_roomba.id == -1:

					self.active_roombas.append(i_roomba)

					rospy.loginfo(str(len(self.active_roombas)))
			
		if len(self.non_active_roombas) > 0:
			
			self.populate_ros_msg()

		
		inactive_index = []

		active_index = []

		i, j = 0, 0

		rospy.loginfo(len(active_roombas))

		if len(active_roombas) > 0:

			rospy.loginfo('There were roombas')

			for a_rba in active_roombas:

				for i_rba in input_roombas:

					if i_rba.x == -1 and i_rba.y == -1 and i_rba.id == -1:

						rospy.loginfo('Bad robot')

						rospy.loginfo(i)

						rospy.loginfo(i_rba)

						rospy.loginfo('Ending logging if the robot is bad')

						i+=1

					else:

						if a_rba.x - i_rba.x <= 0.01 and a_rba.y - i_rba.y <= 0.01:

							rospy.loginfo('We already found that one!')

							self.active_roombas.append(i_rba)

							active_index.append(j)

							rospy.loginfo(i)

							rospy.loginfo(i_rba)

							rospy.loginfo('Ending logging if the robot is good')

							i+=1

					rospy.loginfo('second loop %s' % str(i == len(input_roombas)))

					if i >= len(input_roombas):

						rospy.loginfo('Breaking out of input loop because of itr')

						i = 0

						break

				rospy.loginfo('Breaking out of the input loop')

				j+=1

				rospy.loginfo('first loop %s' % str(j >= len(active_roombas)))

				rospy.loginfo(j)

				rospy.loginfo(len(active_roombas))

				rospy.loginfo(len(self.active_roombas))

				if j >= len(active_roombas):

					j = 0

					break

			rospy.loginfo('Breaking out of the active_roombas')

			for i in active_index:

				del active_roombas[i]

			del active_index[:]

		else:

			for rba in input_roombas:

				if rba.x == -1 or rba.y == -1 or rba.id == -1:

					rospy.loginfo('Bad robot')

					continue

				else:

					rospy.loginfo('Good robot')

					self.active_roombas.append(rba)

		if len(active_roombas) > 0:

			self.populate_ros_msg(active_roombas)

		else:

			rospy.loginfo('nothing is inactive at the moment')

		'''

					
	def callback_for_localization(self, seen_roomba):

		#rospy.loginfo('I got called')
		
		#self.differentate_roombas(seen_roomba.numMap, self.active_roombas)

		input_roombas = seen_roomba.numMap

		inactive_index = []

		active_index = []

		active_roombas = []

		i, j = 0, 0

		if len(self.active_roombas) > 0:

			rospy.loginfo('There were roombas')

			for a_rba in self.active_roombas:

				for i_rba in input_roombas:

					if i_rba.x == -1 and i_rba.y == -1 and i_rba.id == -1:

						rospy.loginfo('Bad robot')

						rospy.loginfo(i)

						rospy.loginfo(i_rba)

						rospy.loginfo('Ending logging if the robot is bad')

						i+=1

					else:

						if a_rba.x - i_rba.x <= 0.01 and a_rba.y - i_rba.y <= 0.01:

							rospy.loginfo('We already found that one!')

							active_roombas.append(i_rba)

							active_index.append(j)

							rospy.loginfo(i)

							rospy.loginfo(i_rba)

							rospy.loginfo('Ending logging if the robot is good')

							i+=1

					rospy.loginfo('second loop %s' % str(i == len(input_roombas)))

					if i >= len(input_roombas):

						rospy.loginfo('Breaking out of input loop because of itr')

						i = 0

						break

				rospy.loginfo('Breaking out of the input loop')

				j+=1

				rospy.loginfo('first loop %s' % str(j >= len(self.active_roombas)))

				rospy.loginfo(j)

				rospy.loginfo(len(self.active_roombas))

				if j >= len(self.active_roombas):

					j = 0

					break

			rospy.loginfo('Breaking out of the active_roombas')

			for i in active_index:

				del self.active_roombas[i]

			del active_index[:]

			self.active_roombas = active_roombas

		else:

			for rba in input_roombas:

				if rba.x == -1 or rba.y == -1 or rba.id == -1:

					rospy.loginfo('Bad robot')

					continue

				else:

					rospy.loginfo('Good robot')

					self.active_roombas.append(rba)

		if len(active_roombas) > 0:

			self.populate_ros_msg(active_roombas)

		else:

			rospy.loginfo('nothing is inactive at the moment')
		
	def loop_till_ros_ends(self):
		
		rospy.spin()
		
	def populate_ros_msg(self, input_roombas):
		
		rospy.loginfo( "Good, we got called! This means that the contents for non_active_roombas will be sent to the other sim! " )
		
		for robot in input_roombas:

			rospy.loginfo(robot)
			
			#self.drone_coors = self.droneLoc.get_coors()

			if not robot.x == -1 and robot.y == -1 and robot.tag == -1:
			
				self.msg_for_sim.x, self.msg_for_sim.y = robot.x , robot.y 
				
				self.msg_for_sim.id = robot.id
				
				self.ros.send_msg(self.msg_for_sim)

				rospy.loginfo('sent the message!')
		
if __name__ == '__main__':
	
	Diff = Differentiate_Roombas()
	
	rospy.spin()
