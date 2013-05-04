import pygame
from Sprite import *



class World:
    def __init__(self,d):
        self.d=d
        self.reset()
    def reset(self):
        self.sprites=[]
    def update(self,dtime):
        self.d.update(dtime)
        for s in self.sprites:
            s.update(dtime)
    def draw(self,screen):
        for s in self.sprites:
            s.draw(screen)
        self.d.draw(screen)
            
        



