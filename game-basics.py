from tkinter import *
from boards import *
root = Tk()
canvas = Canvas(root, width=720, height=720, background = "black")
canvas.pack()

class FloorMap(object):
    def __init__(self):
        self.background_tile_floor = PhotoImage(file="assets/floor.png")
        self.background_tile_wall = PhotoImage(file="assets/wall.png")
        self.tile = 72

    def map_display(self, board): #a valtozokat csinald meg csinosabbra
        for row in range(len(board)):
            for cell in range(len(board[row])):
                if board[cell][row] == 0:
                    canvas.create_image(row*self.tile, cell*self.tile, anchor = NW, image = self.background_tile_floor)
                else:
                    canvas.create_image(row*self.tile, cell*self.tile, anchor = NW, image = self.background_tile_wall)

class Character(object):
    def __init__(self):
        #self.char_pic = PhotoImage(file="assets/" + char_pic)
        self.pos_x = 0
        self.pos_y = 0
        #self.tile = 72

    def draw_character(self, pos_x, pos_y, char_pic):
        canvas.create_image(pos_x*72, pos_y*72, anchor = NW, image = char_pic)

class Hero(Character):
    def __init__(self):
        self.char_pic_down =  PhotoImage(file="assets/hero-down.png")
        self.char_pic_up=  PhotoImage(file="assets/hero-up.png")
        self.char_pic_left =  PhotoImage(file="assets/hero-left.png")
        self.char_pic_right =  PhotoImage(file="assets/hero-right.png")
        self.draw_character(3, 4, self.char_pic_right)

floor = FloorMap()
floor.map_display(map1)
hero = Hero()

root.mainloop()
