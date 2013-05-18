import pygame
import random as r
import Animation
import numpy as np #now using numpy library
import copy

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


    def __deepcopy__(self,memo):
        newone = type(self)(copy.deepcopy(self.anim))
        newone.acceleration = copy.deepcopy(self.acceleration)
        newone.velocity = copy.deepcopy(self.velocity)
        newone.position = copy.deepcopy(self.position)
        return newone
        
    def update(self,dtime):
        self.anim.update(dtime)

        dtimeSeconds = dtime / 1000.0
        self.velocity += self.acceleration * dtimeSeconds
        self.position += self.velocity * dtimeSeconds
        
    def draw(self,screen):
        screen.blit(self.anim.getFrame().img,self.position.tolist())
        #() tuple a list that can't be modified


    def containsPoint(self,x,y):
        if x < self.position[0] or x > self.position[0] + self.anim.getFrame().img.get_width() or y < self.position[1] or y > self.position[1] + self.anim.getFrame().img.get_height():
            return False
        return True

    
        #Logic gates
class Gate(Sprite):
    def __init__(self,ioa):
        super(Gate,self).__init__(ioa)
    def trigger():
        pass

class And(Gate):
    def __init__(self,a):
        super(And,self).__init__(a)
    def trans(self):
        return 6

class Or(Gate):
    def __init__(self,a):
        super(Or,self).__init__(a)
    def trans(self):
        return 6

class Not(Gate):
    def __init__(self,a):
        super(Not,self).__init__(a)
    def trans(self):
        return 2

class Xor(Gate):
    def __init__(self,a):
        super(Xor,self).__init__(a)
    def trans(self):
        return 6

class Nand(Gate):
    def __init__(self,a):
        super(Nand,self).__init__(a)
    def trans(self):
        return 4

class Nor(Gate):
    def __init__(self,a):
        super(Nor,self).__init__(a)
    def trans(self):
        return 4

class Xnor(Gate):
    def __init__(self,a):
        super(Xnor,self).__init__(a)
    def trans(self):
        return 6

class Bulb(Sprite):
    def __init__(self,a):
        pass
        
