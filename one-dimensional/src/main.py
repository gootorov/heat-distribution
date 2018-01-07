import matplotlib as mpl
mpl.use('TkAgg')
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib import rc
rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
rc('text', usetex=True)

def gaussian(x, time, conductivity):
    x = np.multiply(conductivity, np.square(x))
    exp = np.negative(np.divide(x, time))
    num = np.power(np.e, exp)
    den = np.sqrt(time)
    return np.divide(num, den)

def animate(time, x, conductivity):
    # animation function passes 0 at the very beginning
    if time < 0.02:
        time = 0.0001
    y = gaussian(x, time, conductivity)

    graph.set_ydata(y)
    plt.title(r'$Time$ $=$ ${0}$ $(s)$'.format(np.round(time, decimals=1)), fontsize=20)

    return graph, ax

def main():
    plt.style.use('ggplot')

    # Thermal conductivity of air
    conductivity = 0.024

    resolution = 250
    max_plot_boundary = 100
    x = np.linspace(-max_plot_boundary, max_plot_boundary, num=resolution)

    # has to be global for the animation to work
    global fig, ax, graph
    fig, ax = plt.subplots()

    # initial distribution
    y = gaussian(x, time=0.1, conductivity=conductivity)

    ax.set_xlabel(r'$Direction$ $(cm)$', fontsize=20)
    ax.set_ylabel(r'$Temperature$ $(^\circ C)$', fontsize=20)
    graph, = ax.plot(x, y)

    # 60 frames per second
    anim = FuncAnimation(fig, animate, fargs=(x, conductivity,),
            frames=np.arange(0, 100, 0.02), interval=20)

    plt.ylim(0, 3)
    plt.show()

if __name__ == '__main__':
    main()
