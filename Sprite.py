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
            self.convert(ioa)

        #acceleration vector
        self.acceleration = np.array([0.0,0.0])
        #velocity vector
        self.velocity = np.array([0.0,0.0])
        #position vector
        self.position = np.array([0.0,0.0])

        self.fixed = True

    def convert(self,img):
        self.anim=Animation.Animation()
        self.anim.addFrame(img,10)


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
        if hasattr(self,'a'):
            self.a.draw(self.position[0],self.position[1],screen)
        if hasattr(self,'b'):
            self.b.draw(self.position[0],self.position[1],screen)


    def containsPoint(self,x,y):
        if x < self.position[0] or x > self.position[0] + self.anim.getFrame().img.get_width() or y < self.position[1] or y > self.position[1] + self.anim.getFrame().img.get_height():
            return False
        return True

    def connector(self,x,y):
        try:
            if self.a.containsPoint(self.position[0], self.position[1],x,y):
                return self.a
            if self.b.containsPoint(self.position[0], self.position[1],x,y):
                return self.b
        except:
            return None
        return None

    def cornerCollide(self,s):
        P1 = (self.position[0],self.position[1])
        if s.containsPoint(P1[0],P1[1]):
            return True
        P2 = (self.position[0] + self.anim.getFrame().img.get_width(),self.position[1])
        if s.containsPoint(P2[0],P2[1]):
            return True
        P3 = (self.position[0],self.position[1] + self.anim.getFrame().img.get_height())
        if s.containsPoint(P3[0],P3[1]):
            return True
        P4 = (self.position[0] + self.anim.getFrame().img.get_width(),self.position[1] + self.anim.getFrame().img.get_height())
        if s.containsPoint(P4[0],P4[1]):
            return True

        return False

    def center(self):
        return (self.position[0]+self.anim.getFrame().img.get_width()/2.0,self.position[1]+self.anim.getFrame().img.get_height()/2.0)
    

    def imprint(self):
        self.backup = np.copy(self.position)

    def snap(self):
        self.position = np.copy(self.backup)

    
        #Logic gates
class Gate(Sprite):
    def __init__(self,ioa):
        super(Gate,self).__init__(ioa)
    def trigger():
        pass

class SingleIn(Gate):
    def __init__(self,a):
        super(SingleIn,self).__init__(a)
        self.a = Connector(0,15)

class DualIn(Gate):
    def __init__(self,a):
        super(DualIn,self).__init__(a)
        self.a = Connector(0,5)
        self.b = Connector(0,25)

class And(DualIn):
    def __init__(self,a):
        super(And,self).__init__(a)
    def trans(self):
        return 6
    def signal(self):
        try:
            a = self.a.link.signal()
            b = self.b.link.signal()
            if a == None or b == None:
                return None
            if a and b:
                return True
            return False
        except:
            return None

class Or(DualIn):
    def __init__(self,a):
        super(Or,self).__init__(a)
    def trans(self):
        return 6
    def signal(self):
        try:
            a = self.a.link.signal()
            b = self.b.link.signal()
            if a == None or b == None:
                return None
            if a or b:
                return True
            return False
        except:
            return None

class Not(SingleIn):
    def __init__(self,a):
        super(Not,self).__init__(a)
    def trans(self):
        return 2
    def signal(self):
        try:
            s = self.a.link.signal()
            if s == True:
                return False
            if s == None:
                return None
            return True
        except:
            return None

class Xor(DualIn):
    def __init__(self,a):
        super(Xor,self).__init__(a)
    def trans(self):
        return 6
    def signal(self):
        try:
            a = self.a.link.signal()
            b = self.b.link.signal()
            if a == None or b == None:
                return None
            if a != b:
                return True
            return False
        except:
            return None

class Nand(DualIn):
    def __init__(self,a):
        super(Nand,self).__init__(a)
    def trans(self):
        return 4
    def signal(self):
        try:
            a = self.a.link.signal()
            b = self.b.link.signal()
            if a == None or b == None:
                return None
            if not a or not b:
                return True
            return False
        except:
            return None

class Nor(DualIn):
    def __init__(self,a):
        super(Nor,self).__init__(a)
    def trans(self):
        return 4
    def signal(self):
        try:
            a = self.a.link.signal()
            b = self.b.link.signal()
            if a == None or b == None:
                return None
            if not a and not b:
                return True
            return False
        except:
            return None

class Xnor(DualIn):
    def __init__(self,a):
        super(Xnor,self).__init__(a)
    def trans(self):
        return 6
    def signal(self):
        try:
            a = self.a.link.signal()
            b = self.b.link.signal()
            if a == None or b == None:
                return None
            if a == b:
                return True
            return False
        except:
            return None
    

class Sink(Sprite):
    def __init__(self,a):
        super(Sink,self).__init__(a)
        self.a = Connector(14, 31)
    def check(self):
        if self.a.link != None:
            if self.a.link.signal() == True:
                self.convert(self.on)
            else:
                self.convert(self.off)
        else:
            self.convert(self.off)
    def update(self,dt):
        self.check()
        Sprite.update(self,dt)
            
        

class Source(Sprite):
    def __init__(self,a):
        super(Source,self).__init__(a)
    def signal(self):
        return True

class Connector:
    def containsPoint(self,sx,sy,x,y):
        if sx+self.x<=x and x <= sx+self.x+self.w:
            if sy+self.y<=y and y<= sy+self.y + self.h:
                return True
        else:
            return False
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.w = 21
        self.h = 20
        self.link = None
        
    def center(self, sx, sy):
        return [self.x + sx + self.w / 2.0, self.y + sy + self.h / 2.0]

    def draw(self,sx,sy,s):
        #pygame.draw.rect(s,[255,0,0],[sx+self.x,sy+self.y,self.w,self.h],1)
        if self.link != None:
            pygame.draw.line(s,[0,100,255],self.link.center(), self.center(sx, sy))





