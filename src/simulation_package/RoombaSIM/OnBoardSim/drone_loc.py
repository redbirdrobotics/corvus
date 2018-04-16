'''
from ROSExtension import ROSExtension
import rospy
import tf

class DroneLoc(object):
	"""docstring for DroneLoc"""
	def __init__(self):

		self.ros = ROSExtension()
	
		self.ros.init_ros_node('DroneLoc_Simulation')

        	self.ros.create_listener('/mavros/local_position/pose', PoseStamped, self.local_position_callback)

		self.quadX = None
		self.quadY = None
		self.quadZ = None
		self.quadW = None

		self.angleOfAttack = None

	def populate_drone_info(self, msg):
        	self.quadX = msg.pose.position.x
		self.quadY = msg.pose.position.y

		self.quadZ = msg.pose.position.z

		quaternion = (msg.pose.orientation.x, msg.pose.orientation.y, msg.pose.orientation.z, msg.pose.orientation.w)

		self.angleOfAttack = tf.transformations.euler_from_quaternion(quaternion)


	def get_coors():

		return self.quadX, self.quadY

	def getPoseOfDrone():

		return self.quadX, self.quadY, self.quadZ

	def getYaw(self):

		return self.angleOfAttack[2]

if __name__ == '__main__':
	
	droneLoc = DroneLoc()
	
	rospy.spin()
'''