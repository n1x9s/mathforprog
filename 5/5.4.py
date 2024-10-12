import numpy as np

import matplotlib.pyplot as plt

def mandelbrot(c, max_iter):
    z = c
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = z*z + c
    return max_iter

def generate_mandelbrot(width, height, x_min, x_max, y_min, y_max, max_iter):
    r1 = np.linspace(x_min, x_max, width)
    r2 = np.linspace(y_min, y_max, height)
    n3 = np.empty((width, height))
    for i in range(width):
        for j in range(height):
            n3[i, j] = mandelbrot(r1[i] + 1j*r2[j], max_iter)
    return (r1, r2, n3)

def display_mandelbrot(x_min, x_max, y_min, y_max, width=800, height=800, max_iter=256):
    dpi = 80
    img_width = width / dpi
    img_height = height / dpi

    fig, ax = plt.subplots(figsize=(img_width, img_height), dpi=dpi)
    X, Y, Z = generate_mandelbrot(width, height, x_min, x_max, y_min, y_max, max_iter)
    ax.imshow(Z.T, origin='lower', extent=[x_min, x_max, y_min, y_max], cmap='hot')
    plt.show()

if __name__ == "__main__":
    display_mandelbrot(-2.0, 1.0, -1.5, 1.5)