import npd2d
import npd3d
import view

import numpy as np

X = np.zeros((256, 256))
npd2d.ellipse(X, 1.0, (128, 128), (64, 8), rotation=np.deg2rad(45))
view.show_image(X)

X = np.zeros((256, 256, 256))
npd3d.spheroid(X, 1.0, (128, 224, 32), (100, 50, 20), rotation=(None, None, None))
view.show_stack(X, interval=25, axis=0)

X = np.zeros((256, 256, 256))
npd3d.spheroid(X, 1.0, (128, 224, 32), (100, 50, 20), rotation=(np.deg2rad(20), np.deg2rad(20), np.deg2rad(20)))
view.show_stack(X, interval=25, axis=0)

X = np.zeros((256, 256, 256))
npd3d.spheroid(X, 1.0, (128, 128+32, 128-32), (100, 40, 80), rotation=(np.deg2rad(20), np.deg2rad(20), np.deg2rad(20)))
view.gif_stack(X, "example/3D_spheroid.gif", interval=25, axis=2)
