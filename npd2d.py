import numpy as np

"""
Ellipse
https://en.wikipedia.org/wiki/Ellipse
Ellipse equation
(x ** 2 / rx ** 2) +
(y ** 2 / ry ** 2)
= 1
or
(x / rx) ** 2 +
(y / ry) ** 2
= 1

width = 2*rx
height = 2*ry

Ellipse equation with rotation
2D rotation matrix
[[cos(alpha), -sin(alpha)],
[sin(alpha), cos(alpha)]]
*
Vector
[x, y]
=
((x * cos(a) - y * sin(a)) / rx) ** 2 +
((x * sin(a) + y * cos(a)) / ry) ** 2
= 1
"""


def ellipse_coordinate(shape, center, radius, rotation=None):
    """
    return coordinates of point in the ellipse.
    warning: rotation is not a perfectly verified feature, use at risk.
    """
    x_lim, y_lim = np.ogrid[0:float(shape[0]), 0:float(shape[1])]
    x_org, y_org = center
    x_rad, y_rad = radius
    x, y = (x_lim - x_org), (y_lim - y_org)

    if rotation is None:
        d = (x / x_rad) ** 2 + (y / y_rad) ** 2
    else:
        rot = rotation % np.pi
        cos_a = np.cos(rot)
        sin_a = np.sin(rot)

        d = ((x * cos_a - y * sin_a) / x_rad) ** 2 + ((x * sin_a + y * cos_a) / y_rad) ** 2

    return np.nonzero(d < 1)


def ellipse(array, fill, center, radius, rotation=None):
    """
    return the given array with a filled ellipse.
    warning: using the returned value is not mandatory.
             the array is passed by reference, if you want to avoid modification on the original array, use np.copy
    """
    array[ellipse_coordinate(array.shape, center, radius, rotation)] = fill
    return array
