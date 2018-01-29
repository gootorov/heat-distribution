import matplotlib as mpl
mpl.use('TkAgg')
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.axes_grid1 import make_axes_locatable
from matplotlib import rc
rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
rc('text', usetex=True)

def gaussian(x, y, time, conductivity):
    xysum = np.multiply(conductivity, np.add(np.square(x), np.square(y)))
    exp = np.negative(np.divide(xysum, time))
    top = np.power(np.e, exp)
    bot = np.sqrt(time)
    return np.divide(top, bot)


def animate(time, X, Y, conductivity, max_color_norm):
    if time < 0.02:
        time = 0.01
    Z = gaussian(X, Y, time, conductivity)
    ax.clear()
    graph = ax.plot_surface(X, Y, Z, cmap='plasma', vmin=0, vmax=max_color_norm,
            cstride=2, rstride=2, antialiased=True)
    plt.suptitle(r'$Time$ $=$ ${0}$ $(s)$'.format(time), fontsize=26)
    ax.set_zlabel(r'$Temperature$ $(^\circ C)$', fontsize=24)
    ax.set_ylabel(r'$Y$ $direction$ $(cm)$', fontsize=24)
    ax.set_xlabel(r'$X$ $direction$ $(cm)$', fontsize=24)
    ax.set_zlim(0,1)
    return graph,


def main():
    # Thermal conductivity of air
    conductivity = 0.026

    resulution = 150
    max_plot_boundary = 100
    max_color_norm = 0.2

    x = np.linspace(-max_plot_boundary, max_plot_boundary, num=resulution)
    y = np.linspace(-max_plot_boundary, max_plot_boundary, num=resulution)
    X, Y = np.meshgrid(x, y)
    # initial distribution
    Z = gaussian(X, Y, time=0.001, conductivity=conductivity)

    # matplotlib requires these objects to be global:
    # https://matplotlib.org/api/animation_api.html#funcanimation
    global fig, ax, graph
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    graph = ax.plot_surface(X, Y, Z, cmap='plasma', vmin=0, vmax=max_color_norm,
            animated=True, cstride=2, rstride=2)
    plt.colorbar(graph, shrink=0.35, fraction=0.046, pad=0.04)

    # 50 frames per second
    #anim = FuncAnimation(fig, animate, frames=np.arange(0, 100, 0.02), interval=20)

    # 1 frame per second
    anim = FuncAnimation(fig, animate, fargs=(X, Y, conductivity, max_color_norm,),
            frames=1000, interval=1000)

    # make the window full screen
    mng = plt.get_current_fig_manager()
    mng.resize(*mng.window.maxsize())

    plt.show()

if __name__ == '__main__':
    main()
