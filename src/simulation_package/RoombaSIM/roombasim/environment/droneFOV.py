import numpy as np

class DroneFOV(object):

	LINE_HEIGHT = 2.5

	LINE_WIDTH = 0.25

	MAX_VIEW_LENGTH = 1.0

	def __init__(self):

		self.drone_x = None

		self.drone_y = None

		self.ptA = None

		self.ptB = None

		self.ptC = None

	def get_coors(self, drone):

		self.drone_x, self.drone_y = drone.xy_pos

		self.ptA = np.array((self.drone_x, self.drone_y))

		self.ptB = np.array(self.drone_x + self.LINE_WIDTH, self.drone_y + self.LINE_HEIGHT)

		self.ptC = np.array(self.drone_x - self.LINE_WIDTH, self.drone_y + self.LINE_HEIGHT)

	def isInFOV(self, pD):

		v0 = np.array(self.ptC - self.ptA)

		v1 = np.array(self.ptB - self.ptA)

		v2 = np.array(np.array(pD) - self.ptA)

		dot00 = np.dot(v0, v0)

		dot01 = np.dot(v0, v1)

		dot02 = np.dot(v0, v2)

		dot11 = np.dot(v1, v1)

		dot12 = np.dot(v1, v2)

		invDenom = 1 / (dot00 * dot11 - dot01 * dot01)

		u = (dot11 * dot02 - dot01 * dot12) * invDenom

		v = (dot00 * dot12 - dot01 * dot02) * invDenom

		return np.any(u <= 0) and np.any(v <= 0) and np.any((u + v) < 1)
