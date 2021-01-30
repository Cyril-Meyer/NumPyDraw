import numpy as np

"""
Spheroid
https://en.wikipedia.org/wiki/Spheroid
Spheroid equation
(x ** 2 / rx ** 2) +
(y ** 2 / ry ** 2) +
(z ** 2 / rz ** 2)
= 1
or
(x / rx) ** 2 +
(y / ry) ** 2 +
(z / rz) ** 2
= 1

width = 2*rx
height = 2*ry
depth = 2*rz
"""


def spheroid_coordinate(shape, center, radius, rotation_xy=None):
    """
    return coordinates of point in the spheroid.
    rotation on the xy plan around the z axis.
    warning: rotation is not a perfectly verified feature, use at risk.
    """
    x_lim, y_lim, z_lim = np.ogrid[0:float(shape[0]), 0:float(shape[1]), 0:float(shape[2])]
    x_org, y_org, z_org = center
    x_rad, y_rad, z_rad = radius
    x, y, z = (x_lim - x_org), (y_lim - y_org), (z_lim - z_org)

    if rotation_xy is None:
        d = (x / x_rad) ** 2 + (y / y_rad) ** 2 + (z / z_rad) ** 2
    else:
        rot = rotation_xy % np.pi
        cos_a = np.cos(rot)
        sin_a = np.sin(rot)

        d = ((x * cos_a - y * sin_a) / x_rad) ** 2 + ((x * sin_a + y * cos_a) / y_rad) ** 2 + (z / z_rad) ** 2

    return np.nonzero(d < 1)


def spheroid(array, fill, center, radius, rotation_xy=None):
    """
    return the given array with a filled spheroid.
    warning: using the returned value is not mandatory.
             the array is passed by reference, if you want to avoid modification on the original array, use np.copy
    """
    array[spheroid_coordinate(array.shape, center, radius, rotation_xy)] = fill
    return array


def spheroid_array(radius):
    """
    return a numpy array containing a spheroid filled with 1.0.
    not to be used, but easiest way to understand the equation.
    """

    rx, ry, rz = radius

    shape = np.zeros((2*rx, 2*ry, 2*rz), dtype=np.float32)

    for x_ in range(shape.shape[0]):
        for y_ in range(shape.shape[1]):
            for z_ in range(shape.shape[2]):
                x = x_ - rx
                y = y_ - ry
                z = z_ - rz

                if (x / rx) ** 2 + (y / ry) ** 2 + (z / rz) ** 2 <= 1:
                    shape[x_, y_, z_] = 1.0

    return shape
