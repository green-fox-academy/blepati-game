from tkinter import *

root = Tk()
canvas = Canvas(root, width=600, height=600)
canvas.pack()

class FloorTile(object):
    def __init__(self, x = 0, y = 0, size = 60, walk_on = True):
        self.x = x
        self.y = y
        self.size = size
        self.walk_on = walk_on

    def draw_floor(self):
        floor = canvas.create_rectangle(self.x, self.y, self.x + self.size, self.y + self.size, fill='green')


floor = FloorTile()
floor.draw_floor()
root.mainloop()
