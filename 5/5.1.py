import numpy as np

import matplotlib.pyplot as plt

# Параметры спирали
a = float(input('Введите значение параметра a: '))
b = float(input('Введите значение параметра b: '))
theta_max = 4 * np.pi
theta = np.linspace(0, theta_max, 1000)

# Вычисление координат точек на спирали
r = a + b * theta
x = r * np.cos(theta)
y = r * np.sin(theta)

# Создание графической визуализации
plt.figure(figsize=(6, 6))
plt.plot(x, y)
plt.title('Спираль')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
plt.axis('equal')
plt.show()