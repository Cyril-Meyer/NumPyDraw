import npd2d
import npd3d
import view

import numpy as np

X = np.zeros((256, 256))
npd2d.ellipse(X, 1.0, (128, 128), (64, 8))
view.show_image(X)

X = np.zeros((256, 256, 256))
npd3d.spheroid(X, 1.0, (128, 224, 32), (100, 50, 20), rotation_xy=np.deg2rad(90//8))
view.show_stack(X, interval=25)
