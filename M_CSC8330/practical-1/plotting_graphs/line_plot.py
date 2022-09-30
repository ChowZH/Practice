import sys
import platform
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

class LinePlot():
    def __init__(self, no_repeat=False, red=False):
        self.fig, self.ax = plt.subplots()
        self.x = np.arange(0, 2*np.pi, 0.01)
        self.line, = self.ax.plot(self.x, np.sin(self.x))

    def animate(self, i):
        self.line.set_ydata(np.sin(self.x + i / 50))  # update the data.
        return self.line,

    def plot(self, no_repeat, red):
        if no_repeat == True:
            ani = animation.FuncAnimation(
                self.fig, self.animate, frames=320, interval=20, blit=True, save_count=50, repeat=False)
        else:
            ani = animation.FuncAnimation(
                self.fig, self.animate, frames=320, interval=20, blit=True, save_count=50, repeat=True)
        if red == True:
            self.line.set_color('red')
        plt.show()