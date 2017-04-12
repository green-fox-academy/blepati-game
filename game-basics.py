from tkinter import *

root = Tk()
canvas = Canvas(root, width=720, height=720, background = "black")
canvas.pack()

map1 = [
      [0, 0, 1, 1, 0, 0, 1, 0, 0, 0],
      [0, 0, 1, 0, 0, 0, 1, 0, 1, 1],
      [0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
      [1, 0, 1, 1, 1, 0, 1, 1, 0, 0],
      [0, 0, 0, 0, 1, 0, 0, 1, 0, 1],
      [1, 1, 0, 0, 1, 0, 0, 1, 0, 0],
      [0, 0, 0, 0, 1, 0, 1, 1, 0, 0],
      [0, 0, 0, 0, 1, 0, 1, 0, 0, 1],
      [1, 1, 1, 0, 0, 0, 0, 0, 1, 1],
      [0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
      ]

class FloorMap(object):
    def __init__(self):
        self.background_tile_floor = PhotoImage(file="assets/floor.png")
        self.background_tile_wall = PhotoImage(file="assets/wall.png")
        self.tile = 72

    def map_display(self, map): #a valtozokat csinald meg csinosabbra
        for row in range(len(map)):
            for cell in range(len(map[row])):
                if map[cell][row] == 0:
                    canvas.create_image(row*self.tile, cell*self.tile, anchor = "nw", image = self.background_tile_floor)
                else:
                    canvas.create_image(row*self.tile, cell*self.tile, anchor = "nw", image = self.background_tile_wall)

class Character(object):
    def __init__(self, char_pic):
        self.char_pic = PhotoImage(file="assets/" + char_pic)

    def draw_character(self):
        canvas.create_image(0, 0, anchor = "nw", image = self.char_pic)

floor = FloorMap()
floor.map_display(map1)
hero = Character("hero-down.png")
hero.draw_character()

root.mainloop()
