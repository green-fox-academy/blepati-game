from tkinter import *
from boards import *
root = Tk()
canvas = Canvas(root, width=720, height=720, background = "black")

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
        self.tile = 72

    def draw_character(self, pos_x, pos_y, char_pic):
        canvas.create_image(pos_x*self.tile, pos_y*self.tile, anchor = NW, image = char_pic)

class Hero(Character):
    def __init__(self):
        super().__init__()
        self.char_pic_down =  PhotoImage(file="assets/zodiac-rabbit-front.png")
        self.char_pic_up=  PhotoImage(file="assets/zodiac-rabbit-back.png")
        self.char_pic_left =  PhotoImage(file="assets/zodiac-rabbit-left-side.png")
        self.char_pic_right =  PhotoImage(file="assets/zodiac-rabbit-side.png")
        self.draw_character(self.pos_x, self.pos_y, self.char_pic_down)

    def move_character(self, e):
        #if (self.pos_x > 0 and self.pos_y > 0) or (self.pos_x < 9 and self.pos_y < 9):not working
            if e.keycode == 111:
                self.pos_y -= 1
                self.draw_character(self.pos_x, self.pos_y, self.char_pic_up)
            elif e.keycode == 116:
                self.pos_y += 1
                self.draw_character(self.pos_x, self.pos_y, self.char_pic_down)
            elif e.keycode == 114:
                self.pos_x += 1
                self.draw_character(self.pos_x, self.pos_y, self.char_pic_right)
            elif e.keycode == 113:
                self.pos_x -= 1
                self.draw_character(self.pos_x, self.pos_y, self.char_pic_left)

floor = FloorMap()
floor.map_display(map1)
hero = Hero()
canvas.bind("<KeyPress>", hero.move_character)

canvas.focus_set()

canvas.pack()
root.mainloop()
