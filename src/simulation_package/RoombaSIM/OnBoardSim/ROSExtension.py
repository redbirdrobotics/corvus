import rospy

class ROSExtension(object):
    def __init__(self):
        self._pub = None
        self._listen = None

    def init_ros_node(self, node_name):

        '''
        Method to create a ros node as a publisher. This is a one call-only method. 
        Upon calling a node will be created and then that is all that needs to be done.
        '''

        rospy.init_node(node_name, anonymous=True)

    def create_listener(self, topic_name, callback_method, ros_msg_type):
        rospy.Subscriber(topic_name, ros_msg_type, callback_method)

    def create_publisher(self, topic_name, ros_msg_type):
        self._pub = rospy.Publisher(topic_name, ros_msg_type, queue_size=10000)

    def send_msg(self, data):
        self._pub.publish(data)
