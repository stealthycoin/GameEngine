import pygame
import random as r
import Animation
import numpy as np #now using numpy library

class Sprite:
    def __init__(self,ioa):
        if isinstance(ioa, Animation.Animation): #if it is an animation, load it as such
            self.anim=ioa
        else:#otherwise, it must be an image, make an animation with 1 frame and put the image in that.
            self.anim=Animation.Animation()
            self.anim.addFrame(ioa,10)

        #acceleration vector
        self.acceleration = np.array([0.0,0.0])
        #velocity vector
        self.velocity = np.array([0.0,0.0])
        #position vector
        self.position = np.array([0,0])
        
        
    def update(self,dtime):
        self.anim.update(dtime)

        dtimeSeconds = dtime / 1000.0
        self.velocity += self.acceleration * dtimeSeconds
        self.position += self.velocity * dtimeSeconds
        
    def draw(self,screen):
        print(self.position.tolist())
        screen.blit(self.anim.getFrame().img,self.position.tolist())
        #() tuple a list that can't be modified

    
        #Logic gates
class Gate(Sprite):
    def __init__(self,ioa):
        super(Gate,self).__init__(ioa)
    def trigger():
        pass

class And(Gate):
    def __init__(self,a):
        super(And,self).__init__(a)

class Or(Gate):
    def __init__(self,a):
        super(Or,self).__init__(a)

class Not(Gate):
    def __init__(self,a):
        super(Not,self).__init__(a)

class Xor(Gate):
    def __init__(self,a):
        super(Xor,self).__init__(a)

class Nand(Gate):
    def __init__(self,a):
        super(Nand,self).__init__(a)

class Nor(Gate):
    def __init__(self,a):
        super(Nor,self).__init__(a)

class Xnor(Gate):
    def __init__(self,a):
        super(Xnor,self).__init__(a)

class Bulb(Sprite):
    def __init__(self,a):
        pass
        
