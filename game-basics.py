from tkinter import *

root = Tk()
canvas = Canvas(root, width=720, height=720, background = "black")
canvas.pack()

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

class FloorMap(object):
    def __init__(self):
        self.background_floor = PhotoImage(file="assets/floor.png")
        self.background_wall = PhotoImage(file="assets/wall.png")

    def display(self): #a valtozokat csinald meg csinosabbra
        for row in range(len(map1)):
            for cell in range(len(map1[row])):
                if map1[cell][row] == 0:
                    canvas.create_image(row*72, cell*72, anchor = "nw", image = self.background_floor)
                else:
                    canvas.create_image(row*72, cell*72, anchor = "nw", image = self.background_wall)

floor = FloorMap()
floor.display()

root.mainloop()
