import pygame
from Sprite import *

class World:
    def __init__(self,d):
        self.lastFrame = 0
        self.d=d
        self.reset()


    def reset(self):
        self.sprites=[]
        self.floating=None
        self.offset = [0,0]


    def update(self,dtime):
        self.d.update(dtime)
        if self.lastFrame == 0 and self.im.buttons[1] == 1:
            #mouse pressed down
            self.floating = self.d.click(self.im.getMouseX(),self.im.getMouseY())
            if self.floating:
                self.offset[0] = self.im.getMouseX() - self.floating.position[0]
                self.offset[1] = self.im.getMouseY() - self.floating.position[1]
        elif self.floating != None and self.lastFrame == 1 and self.im.buttons[1] == 1:
            #mouse held down and moved
            self.floating.position[0] = self.im.mouse[0] - self.offset[0]
            self.floating.position[1] = self.im.mouse[1] - self.offset[1]
        elif self.floating != None and self.lastFrame == 1 and self.im.buttons[1] == 0:
            #mouse released, place item
            if self.d.containsPoint(self.im.getMouseX(), self.im.getMouseY()):
                self.floating = None
            else:
                self.sprites.append(self.floating)
                self.floating = None

        for s in self.sprites:
            s.update(dtime)
        self.lastFrame=self.im.buttons[1]


    def draw(self,screen):
        for s in self.sprites:
            s.draw(screen)
        self.d.draw(screen)
        if self.floating != None:
            self.floating.draw(screen)
    
        



