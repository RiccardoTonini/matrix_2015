# version code 77ed2409f40d+
coursera = 1
# Please fill out this stencil and submit using the provided submission script.

# version code 05f5a0d767f0+
# Please fill out this stencil and submit using the provided submission script.

from mat import Mat
from vec import Vec
import math

## Task 1
def identity(labels = {'x','y','u'}):
    '''
    In case you have never seen this notation for a parameter before,
    it defines the default value of labels to be {'x','y','u'}.
    You should write your procedure as if
    it were defined 'def identity(labels):'.  However, if you want the labels of
    your identity matrix to be {'x','y','u'}, you can just call
    identity().  If you want {'r','g','b'}, or another set, to be the
    labels of your matrix, you can call identity({'r','g','b'}).

    >>> identity()==Mat(({'x','y','u'},{'x','y','u'}), {('x','x'):1, ('y','y'):1, ('u','u'):1})
    True
    >>> identity({'r','g','b'})==Mat(({'r','g','b'},{'r','g','b'}), {('r','r'):1, ('g','g'):1, ('b','b'):1})
    True
    '''
    return Mat((labels, labels), {(l, l): 1 for l in labels})

## Task 2
def translation(x,y):
    '''
    Input:  An x and y value by which to translate an image.
    Output:  Corresponding 3x3 translation matrix.

    >>> translation(9,10)==Mat(({'x','y','u'},{'x','y','u'}), {('x','x'):1, ('y','y'):1, ('u','u'):1, ('y','u'):10, ('x','u'):9})
    True
    '''
    id_matrix = identity()
    id_matrix[('x','u')] = x
    id_matrix[('y','u')] = y
    return id_matrix

## Task 3
def scale(a, b):
    '''
    Input:  Scaling parameters for the x and y direction.
    Output:  Corresponding 3x3 scaling matrix.

    >>> scale(3,4)*Vec({'x','y','u'}, {'x':1,'y':1,'u':1}) == Vec({'x','y','u'}, {'x':3, 'y':4, 'u':1})
    True
    >>> scale(0,0)*Vec({'x','y','u'}, {'x':1,'y':1,'u':1}) == Vec({'x','y','u'}, {'u':1})
    True
    '''
    id_matrix = identity()
    id_matrix[('x', 'x')] = a
    id_matrix[('y', 'y')] = b
    return id_matrix

## Task 4
def rotation(angle):
    '''
    Input:  An angle in radians to rotate an image.
    Output:  Corresponding 3x3 rotation matrix.
    Note that the math module is imported.

    >>> def normsq(v): return v*v
    >>> normsq(rotation(math.pi) * Vec({'u', 'x', 'y'},{'x':1,'y':2,'u':1}) - Vec({'u', 'x', 'y'},{'u': 1, 'x': -1, 'y': -2})) < 1e-15
    True
    >>> normsq(rotation(math.pi/2) * Vec({'u', 'x', 'y'},{'x':3,'y':1,'u':1}) - Vec({'u', 'x', 'y'},{'u': 1, 'x': -1, 'y': 3.0})) < 1e-15
    True
    '''
    id_matrix = identity()
    id_matrix['x', 'x'] = id_matrix['y','y'] = math.cos(angle)
    id_matrix['x', 'y'] = - math.sin(angle)
    id_matrix['y', 'x'] = math.sin(angle)
    return id_matrix

## Task 5
def rotate_about(x,y,angle):
    '''
    Input:  An x and y coordinate to rotate about, and an angle
    in radians to rotate about.
    Output:  Corresponding 3x3 rotation matrix.
    It might be helpful to use procedures you already wrote.
    '''
    return translation(x,y) * rotation(angle) * translation(-x,-y)

## Task 6
def reflect_y():
    '''
    Input:  None.
    Output:  3x3 Y-reflection matrix.

    >>> v = Vec({'x','y','u'}, {'x':1, 'y':1, 'u':1})
    >>> reflect_y()*v == Vec({'x','y','u'}, {'x':-1, 'y':1, 'u':1})
    True
    >>> w = Vec({'x','y','u'}, {'u':1})
    >>> reflect_y()*w == Vec({'x','y','u'},{'u':1})
    True
    '''
    id_matrix = identity()
    id_matrix['x','x'] = -1
    return id_matrix

## Task 7
def reflect_x():
    '''
    Inpute:  None.
    Output:  3x3 X-reflection matrix.

    >>> v = Vec({'x','y','u'}, {'x':1, 'y':1, 'u':1})
    >>> reflect_x()*v == Vec({'x','y','u'}, {'x':1, 'y':-1, 'u':1})
    True
    >>> w = Vec({'x','y','u'}, {'u':1})
    >>> reflect_x()*w == Vec({'x','y','u'},{'u':1})
    True
    '''
    id_matrix = identity()
    id_matrix['y','y'] = -1
    return id_matrix

## Task 8
def scale_color(scale_r,scale_g,scale_b):
    '''
    Input:  3 scaling parameters for the colors of the image.
    Output:  Corresponding 3x3 color scaling matrix.

    >>> scale_color(1,2,3)*Vec({'r','g','b'},{'r':1,'g':2,'b':3}) == Vec({'r','g','b'},{'r':1,'g':4,'b':9})
    True
    '''
    id_matrix = identity({'r','g','b'})
    id_matrix['r','r'] = scale_r
    id_matrix['b','b'] = scale_b
    id_matrix['g','g'] = scale_g
    return id_matrix

## Task 9
def grayscale():
    '''
    Input: None
    Output: 3x3 greyscale matrix.
    '''
    id_matrix = identity({'r','g','b'})
    id_matrix['r', 'r'] = 77/256
    id_matrix['g', 'r'] = 77/256
    id_matrix['b', 'r'] = 77/256
    id_matrix['r', 'g'] = 151/256
    id_matrix['g', 'g'] = 151/256
    id_matrix['b', 'g'] = 151/256
    id_matrix['r', 'b'] = 28/256
    id_matrix['g', 'b'] = 28/256
    id_matrix['b', 'b'] = 28/256
    return id_matrix
    labels = {'r', 'g', 'b'}
return Mat((labels, labels), {(row, col):(77.0 if col == 'r' else 151.0 if col == 'g' else 28.0) / 256.0
    for row in labels for col in labels})

## Task 10
def reflect_about(x1, y1, x2, y2):
    '''
    Input: 2 points that define a line to reflect about.
    Output:  Corresponding 3x3 reflect about matrix.

    >>> def normsq(v): return v*v
    >>> normsq(reflect_about(0,1,1,1) * Vec({'x','y','u'}, {'u':1}) - Vec({'x', 'u', 'y'},{'x': 0.0, 'u': 1, 'y': 2.0})) < 10e-15
    True
    >>> normsq(reflect_about(0,0,1,1) * Vec({'x','y','u'}, {'x':1, 'u':1}) - Vec({'x', 'u', 'y'},{'u': 1, 'y': 1})) < 1e-15
    True
    '''
    theta = math.atan(((x2 - x1) * 1.0) / (y2 - y1)) if y2 != y1 else math.pi / 2.0
    return rotate_about(x1, y1, -theta) * translation(x1, y1) * reflect_y() * translation(-x1, -y1) * rotate_about(x1, y1, theta)



