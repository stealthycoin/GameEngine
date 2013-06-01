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
            #mouse pressed down, try to grab something from dispensor
            self.floating = self.d.click(self.im.getMouseX(),self.im.getMouseY())
            if self.floating == None:
                #try to get a sprite from the game world
                for s in self.sprites:
                    if s.containsPoint(self.im.getMouseX(), self.im.getMouseY()):
                        self.floating = s
                        break
                if self.floating != None:
                    self.floating.imprint()
                    self.sprites.remove(self.floating)
                        
                        
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
                if self.floating.fixed == False:
                    self.d.transistors += self.floating.trans()
                    self.floating = None
                else:
                    self.floating.snap()
                    self.sprites.append(self.floating)
                    self.floating = None
                
            else:
                self.sprites.append(self.floating)
                self.floating = None




        for i in len(Sprites):
            for j in range(i)
            self.repel(i,j)

        for s in self.sprites:
            s.update(dtime)

        self.lastFrame=self.im.buttons[1]


    def draw(self,screen):
        for s in self.sprites:
            s.draw(screen)
        self.d.draw(screen)
        if self.floating != None:
            self.floating.draw(screen)

    def repel(self.i,j):
        i = self.sprites[i]
        j = self.sprites[j]
        if i cornerCollide(j) or i.cornerCollide(i):
            ic = np.array(i.center())
            jc = np.array(j.center())
            ji = ic - jc
            ji = -1.0/np.linalg.norm(ji) * ji

        else:
            i.velocity[0]=0
            i.velocity[1]=0
            j.velocity[0]=0
            j.velocity[1]=0
    
        



