from tkinter import *

map1 = [
      [0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
      [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      ]

root = Tk()
canvas = Canvas(root, width=720, height=720, background = "black")
canvas.pack()


class FloorTile(object):
    def __init__(self, x = 0, y = 0, walk_on = True):
        self.x = x
        self.y = y
        self.walk_on = walk_on
        self.background_floor = PhotoImage(file="assets/floor.png")
        self.background_wall = PhotoImage(file="assets/wall.png")

    def draw_floor(self):
        canvas.create_image(self.x, self.y, anchor = "nw", image = self.background_floor)
    def draw_wall(self):
        canvas.create_image(self.x, self.y, anchor = "nw", image = self.background_wall)

    def display(self):
        for row in range(len(map1)):
            for cell in range(len(map1[row])):
                if map1[cell][row] == 0:
                    self.draw_floor()
                    self.x += 72
                elif cell == 1:
                    self.draw_wall()

floor = FloorTile()
floor.display()
root.mainloop()
