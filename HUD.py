import pygame
import Sprite
import copy

class Dispensor:
    def __init__(self):
        self.bounds = (10,10,200,600)
        self.transistors = 0
        self.gates = None
        self.font = pygame.font.SysFont("Verdana", 16)
        self.padding = 5

    def setGates(self,gates):
        self.gates = gates
        x = self.padding
        y = self.padding + 20
        for s in self.gates:
            s.position[0] = self.bounds[0] + x
            s.position[1] = self.bounds[1] + y
            y += s.anim.getFrame().img.get_height() + self.padding 
            
    def containsPoint(self, x, y):
        if x < self.bounds[0] or y < self.bounds[1] or x > self.bounds[0] + self.bounds[2] or y > self.bounds[1] + self.bounds[3]:
            return False
        return True

    def update(self,dtime):
        pass

    def draw(self,s):
        pygame.draw.rect(s,(0,0,200),self.bounds)
        s.blit(self.font.render("Transistors: " + str(self.transistors), 1, (255,255,0)), (self.bounds[0]+self.padding,self.bounds[1]))
        for g in self.gates:
            g.draw(s)
            s.blit(self.font.render(str(g.trans()), 1, (255,255,0)), g.position)

    def click(self,x,y):
        for g in self.gates:
            if g.containsPoint(x,y):
                #deduct cost
                if self.transistors >= g.trans():
                    self.transistors -= g.trans()
                    r = copy.deepcopy(g)
                    r.fixed = False
                    return r

            

    
        
    
