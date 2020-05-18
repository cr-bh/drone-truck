
import numpy as np
from utils import extract
from matplotlib import pyplot as plt




# Code inspired by Google OR Tools plot:
# https://github.com/google/or-tools/blob/fb12c5ded7423d524fc6c95656a9bdc290a81d4d/examples/python/cvrptw_plot.py

def plot_tsp(xy, tour, ax1):
    """
    Plot the TSP tour on matplotlib axis ax1.
    """

    ax1.set_xlim(0, 7)
    ax1.set_ylim(0, 7)

    xs, ys = xy[tour].transpose()
    xs, ys = xy[tour].transpose()
    dx = np.roll(xs, -1) - xs
    dy = np.roll(ys, -1) - ys
    d = np.sqrt(dx * dx + dy * dy)
    lengths = d.cumsum()

    # Scatter nodes
    ax1.scatter(xs, ys, s=40, color='blue')
    # Starting node
    ax1.scatter([xs[0]], [ys[0]], s=100, color='red')

    # Arcs
    qv = ax1.quiver(
        xs, ys, dx, dy,
        scale_units='xy',
        angles='xy',
        scale=1,
    )

    ax1.set_title('{} nodes, total length {:.2f}'.format(len(tour), lengths[-1]))


fig, ax = plt.subplots(figsize=(10, 10))
#f1=extract.get_vehicle_order("tsp20-clip0_greedy")
f1=[0, 2, 12, 19, 5, 10, 18, 3, 15, 8, 16, 14, 1, 6, 11, 4, 13, 17, 9, 7]
f2=np.array(extract.get_vehicle_coor('tsp20_seed608'))
plot_tsp(f2,f1, ax)
plt.show()


