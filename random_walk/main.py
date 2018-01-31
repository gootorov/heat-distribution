import matplotlib as mpl
mpl.use('TkAgg')
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
import seaborn as sns
import numpy as np
import random


def animate(frame, v_lines, x):
    ax.clear()
    for index, _ in enumerate(v_lines):
        decision = random.choice((-1, 1))
        increment = 0.02
        # if at the right boundary, go to the left boundary
        if index + decision == len(v_lines):
            v_lines[0] += increment
            v_lines[index] -= increment
        else:
            v_lines[index + decision] += increment
            v_lines[index] -= increment
    plt.ylim(0, 1)
    plt.xlim(0, np.pi)
    graph = plt.vlines(x, ymin=0, ymax=v_lines)
    return graph, ax


def main():
    # matplotlib requires these objects to be global:
    # https://matplotlib.org/api/animation_api.html#funcanimation
    global fig, ax, graph

    fig, ax = plt.subplots()

    # x axis
    x = np.linspace(0, np.pi, num=500)

    # initial distribution
    v_lines = np.square(np.sin(x))
    plt.vlines(x, ymin=0, ymax=v_lines)
    plt.style.use('ggplot')
    plt.ylim(0, 1)
    plt.xlim(0, np.pi)

    # 60 frames per seconds animation
    anim = FuncAnimation(fig, animate, fargs=(v_lines, x,),
            frames=np.arange(0, 100, 0.02), interval=20)
    plt.show()

if __name__ == '__main__':
    main()
