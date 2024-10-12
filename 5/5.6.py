import numpy as np

import matplotlib.pyplot as plt
import matplotlib.animation as animation

G = 6.67430e-11  
M = 1.989e30    
dt = 86400       

planets = [
    {'pos': np.array([1.496e11, 0]), 'vel': np.array([0, 29780])},  
    {'pos': np.array([2.279e11, 0]), 'vel': np.array([0, 24100])}   
]

def update_positions(planets, dt):
    for planet in planets:
        r = np.linalg.norm(planet['pos'])
        acc = -G * M / r**3 * planet['pos']
        planet['vel'] += acc * dt
        planet['pos'] += planet['vel'] * dt


fig, ax = plt.subplots()
ax.set_xlim(-3e11, 3e11)
ax.set_ylim(-3e11, 3e11)

planet_plots = [ax.plot([], [], 'o')[0] for _ in planets]

def init():
    for plot in planet_plots:
        plot.set_data([], [])
    return planet_plots

def animate(i):
    update_positions(planets, dt)
    for plot, planet in zip(planet_plots, planets):
        plot.set_data(planet['pos'][0], planet['pos'][1])
    return planet_plots

ani = animation.FuncAnimation(fig, animate, init_func=init, frames=365, interval=20, blit=True)

plt.show()