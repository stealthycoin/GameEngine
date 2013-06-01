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



        for s in self.sprites:
            s.velocity = np.array([0.0,0.0])

        for i in range(len(self.sprites)):
            for j in range(i):
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

    def repel(self, i, j):
        def d (a, b):
            return np.linalg.norm(a-b)

        i = self.sprites[i]
        j = self.sprites[j]
        if i.cornerCollide(j) or j.cornerCollide(i):
            ic = np.array(i.center()) #center of i
            jc = np.array(j.center()) #center of j
            ji = ic - jc #vector from j to i
            ji = -1.0/np.linalg.norm(ji) * ji #change ji to unit vector and reverse the direction
            ji *= max(1.0, 100.0 - d(ic,jc)) #scale ji up again based on the distance between the centers (closer is faster)
            j.velocity += ji #make one sprite go along the vector
            i.velocity += -1.0 * ji #the otehr goes in the opposite direction
    
        



