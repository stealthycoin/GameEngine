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


    def update(self,dtime):
        self.d.update(dtime)
        if self.lastFrame==0 and self.im.buttons[1]==1:
            self.d.click(self.im.getMouseX(),self.im.getMouseY())

            
        for s in self.sprites:
            s.update(dtime)
        self.lastFrame=self.im.buttons[1]


    def draw(self,screen):
        for s in self.sprites:
            s.draw(screen)
        self.d.draw(screen)
    
        



