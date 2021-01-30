import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def show_image(image):
    if len(image.shape) != 2:
        return 1

    fig = plt.figure()
    plt.imshow(image, cmap='gray')
    plt.show()

    return 0


def show_stack(stack, interval=50, axis=0):
    if len(stack.shape) != 3:
        return 1

    if axis is not 0:
        stack = np.moveaxis(stack, axis, 0)

    fig = plt.figure()
    slices = []
    for z in range(stack.shape[0]):
        s = plt.imshow(stack[z], cmap='gray')
        slices.append([s])

    anim = animation.ArtistAnimation(fig, slices, interval=interval, repeat_delay=1000, blit=True)
    plt.show()

    return 0


def gif_stack(stack, filename, interval=50, axis=0):
    if len(stack.shape) != 3:
        return 1

    if axis is not 0:
        stack = np.moveaxis(stack, axis, 0)

    fig = plt.figure()
    slices = []
    for z in range(stack.shape[0]):
        s = plt.imshow(stack[z], cmap='gray')
        slices.append([s])

    anim = animation.ArtistAnimation(fig, slices, interval=interval, repeat_delay=1000, blit=True)
    anim.save(filename)

    return 0
