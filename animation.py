import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib

matplotlib.use('TkAgg')

class Display:
    def __init__(self, play, start_paused=True):
        self.play = play
        self.fig, self.ax = plt.subplots()
        self.ax.set_xticks([])
        self.ax.set_yticks([])
        self.img = self.ax.imshow(self.play.matrix, cmap='binary', vmin=0, vmax=1)
        self.fig.tight_layout()
        self.pause = start_paused
        self.fig.canvas.mpl_connect('button_press_event', self.on_click)
        self.fig.canvas.mpl_connect('key_press_event', self.on_key)
        self.fig.canvas.manager.set_window_title("Space - Start/Pause")

    def on_click(self, event):
        if event.inaxes != self.ax:
            return
        i = int(round(event.ydata))
        j = int(round(event.xdata))
        if self.play.matrix[i, j] == 1:
            self.play.matrix[i, j] = 0
        else:
            self.play.matrix[i, j] = 1
        self.img.set_data(self.play.matrix)
        self.fig.canvas.draw()

    def on_key(self, event):
        if event.key == ' ':
            self.pause = not self.pause

    def new_play(self, f):
        if not self.pause:
            self.play.update()
            self.img.set_data(self.play.matrix)
        return [self.img]

    def run(self):
        anim = animation.FuncAnimation(self.fig, self.new_play, interval=40, blit=True)
        plt.show()