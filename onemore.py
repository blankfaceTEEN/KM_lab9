import math
import random
from tkinter import *


class GraphPlot():
    x = 0
    y = 0
    mod = 3  # 3 равных части
    points = 10000000000  # количество точек

    def __init__(self, master):
        self.window = master
        self.gate = False
        self.canvas = Canvas(self.window, height=700, width=808, bg="#FFFFFF")
        self.canvas.grid()
        self.window.update()
        self.w = self.canvas.winfo_width()
        self.h = self.canvas.winfo_height()
        self.canvas.focus_set()
        self.drawData()
        self.canvas.bind('<KeyPress-space>', self.toggle_play_pause)
        self.pause = True
        self._update_call_handle = None

    def drawData(self):
        while True:
            a = random.randint(0, self.mod - 1)  # x
            b = random.randint(0, self.mod - 1)  # y
            if a + b < self.mod:
                break
        self.x = self.x / self.mod + a / self.mod + b / 2 / self.mod
        self.y = self.y / self.mod + b / self.mod
        pixel_x = math.floor(self.x * 808)
        pixel_y = math.floor((1 - self.y) * 700)
        self.draw_point(pixel_x, pixel_y)

    def draw_point(self, x, y):
        self.canvas.create_oval(x, y, x, y, fill="#000000", outline="#000000")

    def toggle_play_pause(self, dummy_event):
        self.pause = not self.pause
        if not self.pause:
            self.updateData()

    def updateData(self):
        self.drawData()
        if not self.pause:
            self._update_call_handle = root.after(10, self.updateData)
        else:
            root.after_cancel(self._update_call_handle)
            self._update_call_handle = None


root = Tk()
GraphPlot(root)
root.mainloop()
