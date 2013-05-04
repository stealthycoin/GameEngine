import pygame
import Sprite


class Dispensor:
    def __init__(self):
        self.bounds = (10,10,200,600)
        self.transistors = 0
        self.gates = None

    def setGates(self,gates):
        self.gates = gates
        padding = 5
        x=y=padding
        for s in self.gates:
            s.position[0]=self.bounds[0]+x
            s.position[1]=self.bounds[1]+y
            y += s.anim.getFrame().img.get_height()+padding 
            

    def update(self,dtime):
        pass

    def draw(self,s):
        pygame.draw.rect(s,(0,0,200),self.bounds)
        for g in self.gates:
            g.draw(s)
            

    
        
    
