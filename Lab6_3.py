import sys
import pygame as pg
pg.init()

class InputBox:

    def __init__(self, x, y, w, h, text=''):
        self.rect = pg.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        
        if event.type == pg.MOUSEBUTTONDOWN:# ทำการเช็คว่ามีการคลิก Mouse หรือไม่
            if self.rect.collidepoint(event.pos): #ทำการเช็คว่าตำแหน่งของ Mouse อยู่บน InputBox นี้หรือไม่
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE # เปลี่ยนสีของ InputBox
            
        if event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_RETURN:
                    self.data = self.text
                    self.text = ''
                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = FONT.render(self.text, True, self.color)

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, Screen):
        # Blit the text.
        Screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pg.draw.rect(Screen, self.color, self.rect, 2)
    
    def output(self):
        return self.data

class InputBoxForAge:

    def __init__(self, x, y, w, h, text=''):
        self.rect = pg.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False
        self.error = False

    def handle_event(self, event):
        
        if event.type == pg.MOUSEBUTTONDOWN:# ทำการเช็คว่ามีการคลิก Mouse หรือไม่
            if self.rect.collidepoint(event.pos): #ทำการเช็คว่าตำแหน่งของ Mouse อยู่บน InputBox นี้หรือไม่
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE # เปลี่ยนสีของ InputBox
            
        if event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_RETURN:
                    self.data = self.text
                    self.text = ''
                    if not self.data.isnumeric():
                        self.error = True 
                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = FONT.render(self.text, True, self.color)

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, Screen):
        # Blit the text.
        Screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pg.draw.rect(Screen, self.color, self.rect, 2)
        if self.error == True:
            error = font.render('Enter number only!',True, (0,0,0), (255,255,255))
            errorRect = error.get_rect() # text size
            errorRect.center = (530, 320)
            screen.blit(error, errorRect)
    
    def output(self):
        return self.data
    
class Rectangle:
    def __init__(self,x=0,y=0,w=0,h=0):
        self.x = x # Position X
        self.y = y # Position Y
        self.w = w # Width
        self.h = h # Height
        self.colorR = 0
        self.colorG = 150
        self.colorB = 255
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

win_x, win_y = 800, 480
screen = pg.display.set_mode((win_x, win_y))

font = pg.font.Font('freesansbold.ttf', 32) # font and fontsize
text = font.render('First name', True, (0,0,0), (255,255,255)) # (text,is smooth?,letter color,background color)
textRect = text.get_rect() # text size
textRect.center = (100, 100)

text2 = font.render('Last name', True, (0,0,0), (255,255,255)) # (text,is smooth?,letter color,background color)
text2Rect = text2.get_rect() # text size
text2Rect.center = (100, 220)

text3 = font.render('age', True, (0,0,0), (255,255,255)) # (text,is smooth?,letter color,background color)
text3Rect = text3.get_rect() # text size
text3Rect.center = (50, 340)

text4 = font.render('summit', True, (255,255,255), (0,150,255)) # (text,is smooth?,letter color,background color)
text4Rect = text4.get_rect() # text size
text4Rect.center = (525, 375)

summit = Button(450,350,150,50)

COLOR_INACTIVE = pg.Color('lightskyblue3') # ตั้งตัวแปรให้เก็บค่าสี เพื่อนำไปใช้เติมสีให้กับกล่องข้อความตอนที่คลิกที่กล่องนั้นๆอยู่
COLOR_ACTIVE = pg.Color('dodgerblue2')     # ^^^
FONT = pg.font.Font(None, 32)
input_box1 = InputBox(20, 120, 140, 32) # สร้าง InputBox1
input_box2 = InputBox(20, 240, 140, 32) # สร้าง InputBox2
input_box3 = InputBoxForAge(20, 360, 140, 32)
input_boxes = [input_box1, input_box2, input_box3] # เก็บ InputBox ไว้ใน list เพื่อที่จะสามารถนำไปเรียกใช้ได้ง่าย
status = 0
run = True

while run:
    screen.fill((255, 255, 255))
    screen.blit(text, textRect)
    screen.blit(text2, text2Rect)
    screen.blit(text3, text3Rect)
    
    if status == 1:
        data = font.render('Hello ' + input_box1.output()+ ' ' + input_box2.output() + '! You are ' + input_box3.output() + ' years old.', True, (0,0,0), (255,255,255))
        dataRect = data.get_rect() # text size
        dataRect.center = (400, 430)
        screen.blit(data, dataRect)
    if summit.isMousePressed() and summit.isMouseOn():
        summit.changColor(0,0,0)
        status = 1
    else:
        summit.changColor(0,150,255)
    
    for box in input_boxes: # ทำการเรียก InputBox ทุกๆตัว โดยการ Loop เข้าไปยัง list ที่เราเก็บค่า InputBox ไว้
        box.update() # เรียกใช้ฟังก์ชัน update() ของ InputBox
        box.draw(screen) # เรียกใช้ฟังก์ชัน draw() ของ InputBox เพื่อทำการสร้างรูปบน Screen
        
    for event in pg.event.get():
        for box in input_boxes:
            box.handle_event(event)
        if event.type == pg.QUIT:
            pg.quit()
            run = False

    summit.draw(screen)
    screen.blit(text4, text4Rect)
    pg.time.delay(1)
    pg.display.update()