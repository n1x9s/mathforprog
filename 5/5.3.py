import numpy as np

import matplotlib.pyplot as plt

mosaic = np.array([
    [0, 1, 2, 3],
    [3, 2, 1, 0],
    [1, 2, 3, 0],
    [0, 3, 2, 1]
])

plt.imshow(mosaic, cmap='viridis')
plt.colorbar()
plt.title('Мозаичное изображение')
plt.show()