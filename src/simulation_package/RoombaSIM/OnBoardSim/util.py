import numpy as np

def get_coors(radius, radians):
    x = radius * np.cos(radians)
    y = radius * np.sin(radians)

    return x, y

def circle_intersects_circle(a_center, b_center, radius):
    '''
    Returns True if the two circles intersect.

    a_center, b_center - the center of each circle
    radius - the radius of each circle
    '''
    dist = pow(a_center[0] - b_center[0], 2) + pow(a_center[1] - b_center[1], 2)
    intersects = dist < (4 * radius * radius) 
    return intersects

def circle_intersects_line(circle, radius, p0, p1):
    '''
    Returns True if the line passes through the circle.

    circle - center of circle
    radius - radius of circle
    p0, p1 - endpoints of line
    '''
    # black magic
    
    segment = np.array([p1[0]-p0[0], p1[1]-p0[1]])
    seg_circ = np.array([circle[0]-p0[0], circle[1]-p0[1]])

    norm_seg = segment / np.linalg.norm(segment)

    dot = np.dot(norm_seg, seg_circ)
    project = norm_seg * np.dot(norm_seg, seg_circ)

    if dot < 0 or dot > np.linalg.norm(segment):
        # projected vector is in the wrong direction
        # or larger than the original segment vector
        return False

    proj_point = project + np.array(p0)

    dist = np.linalg.norm(proj_point - np.array(circle))

    return dist < radius



def circle_intersects_goal(circle, radius):
    return circle_intersects_line(circle, radius, (0, 20), (20, 20))

def circle_intersects_rboundary(circle, radius):
    return circle_intersects_line(circle, radius, (20,0), (20,20))

def circle_intersects_bboundary(circle, radius):
    return circle_intersects_line(circle, radius, (0, 0), (20, 0))

def circle_intersects_lboundary(circle, radius):
    return circle_intersects_line(circle, radius, (0, 0), (0, 20))

def point_is_in_circle(circle, radius, point):
	
	distance = np.sqrt( np.square(circle[0] - radius[0]) + np.square(circle[1] - radius[1]) )
	
	return distance == radius

#minimum distance a circle can approach a boundary
MIN_DISTANCE = 2.0 #m

def min_time(circle, boundary_flag):

    '''
    Boundary falg can take on 4 possible values:

        0 - goal line
        1 - right boundary
        2 - bottom boundary
        3 - left boundary

    '''

    if boundary_flag == 0:

        _min_distance = ( 20 - circle[1] ) - MIN_DISTANCE

        return np.absolute( ( _min_distance / 0.33 ) )

    elif boundary_flag == 1:

        _min_distance = ( 20 - circle[0] ) - MIN_DISTANCE 

        return np.absolute( ( _min_distance / 0.33 ) )

    elif boundary_flag == 2:

        _min_distance = ( circle[1] ) - MIN_DISTANCE

        return np.absolute( ( _min_distance / 0.33 ) )

    elif boundary_flag == 3:

        _min_distance =  ( circle[0] ) - MIN_DISTANCE

        return np.absolute( ( _min_distance / 0.33 ) )

