import sys 
import pygame as pg
pg.init()

class Rectangle:
    def __init__(self,x=0,y=0,w=0,h=0):
        self.x = x # Position X
        self.y = y # Position Y
        self.w = w # Width
        self.h = h # Height
        self.colorR = 136
        self.colorG = 8
        self.colorB = 8
    def draw(self,screen):
        pg.draw.rect(screen,(self.colorR, self.colorG, self.colorB),(self.x,self.y,self.w,self.h))
    def changColor(self, colorR, colorG, colorB):
        self.colorR = colorR
        self.colorG = colorG
        self.colorB = colorB

class Button(Rectangle):
    def __init__(self, x=0, y=0, w=0, h=0):
        Rectangle.__init__(self, x, y, w, h)
    
    def isMouseOn(self):
        if(pg.mouse.get_pos()[0] >= self.x and pg.mouse.get_pos()[0] <= self.x+self.w and pg.mouse.get_pos()[1] >= self.y and pg.mouse.get_pos()[1] <= self.y+self.h):
            return True
        pass
    def isMousePressed(self):
        if(pg.mouse.get_pressed()[0]):
            return True
        pass

run = True
win_x, win_y = 800, 480
screen = pg.display.set_mode((win_x, win_y))
btn = Button(20,20,100,100) # สร้าง Object จากคลาส Button ขึ้นมา

while(run):
    screen.fill((255, 255, 255))
    if btn.isMousePressed() and btn.isMouseOn():
        btn.changColor(138,43,226)
    elif btn.isMouseOn():
        btn.changColor(220, 220, 220)
    else:
        btn.changColor(136, 8, 8)
    btn.draw(screen)
    
    pg.display.update()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            run = False