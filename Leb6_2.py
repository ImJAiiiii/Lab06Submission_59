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

run = True
win_x, win_y = 800, 480
screen = pg.display.set_mode((win_x, win_y))
rec = Rectangle(20,20,100,100)
while(run):
    screen.fill((255, 255, 255))
    rec.draw(screen)
    pg.display.update()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            run = False
        if event.type == pg.KEYDOWN and event.key == pg.K_d: #ปุ่มถูกกดลงและเป็นปุ่ม D
            rec.x += 1
        if event.type == pg.KEYDOWN and event.key == pg.K_a: #ปุ่มถูกปล่อยและเป็นปุ่ม A
            rec.x -= 1
        if event.type == pg.KEYDOWN and event.key == pg.K_w: #ปุ่มถูกกดลงและเป็นปุ่ม D
            rec.y -= 1
        if event.type == pg.KEYDOWN and event.key == pg.K_s: #ปุ่มถูกปล่อยและเป็นปุ่ม A
            rec.y += 1