import pygame
from Animation import *
import copy
import World
import HUD
import Sprite
import re
import copy

class ResourceManager:
    def __init__(self):
        """constructor, makes empty dictionaries, and then calls functions to fill them"""
        self.images={}
        self.animations={}

        self.loadImages()
        self.loadAnimations()

    def loadAnimations(self):
        """Loads all animations for game given the images are already loaded"""
        
    def loadImages(self):
        """Loads all images for game"""
        self.loadImage("or","./resources/images/or.png")
        self.loadImage("and","./resources/images/and.png")
        self.loadImage("not","./resources/images/not.png")
        self.loadImage("xor","./resources/images/xor.png")
        self.loadImage("nand","./resources/images/nand.png")
        self.loadImage("nor","./resources/images/nor.png")
        self.loadImage("xnor","./resources/images/xnor.png")
        self.loadImage("offbulb","./resources/images/offbulb.jpg")
        self.loadImage("onbulb","./resources/images/onbulb.jpg")
        self.loadImage("Source","./resources/images/Source.png")

    def loadImage(self, name, path, key=None):
        """Loads an image with a name at a given path, and gives it a colorkey"""

        if key != None:
            t = pygame.image.load(path).convert()
            t.set_colorkey(key)
        else:
            t = pygame.image.load(path).convert_alpha()
        self.images[name]=t

    def getImage(self,name,copy=True):
        """Gets an image from the resource manager with a given name, can make a copy of it"""
        if copy:
        #if just copy it will will be true already since copy is already a true statement
            return self.images[name].copy()
        return self.images[name]

    def getAnimation (self,name):
        """Returns an animation with a given name, all frames data is shared amongst copies"""
        return copy.deepcopy(self.animations[name])

    def loadMap (self,m):
        filename = "./Resources/Maps/" + m
        f = open(filename,'r')
        text = f.read()
        f.close()
        d = HUD.Dispensor()
        #gates
        d.AND=Sprite.And(self.getImage("and"))
        d.OR=Sprite.Or(self.getImage("or"))
        d.NOT=Sprite.Not(self.getImage("not"))
        d.XOR=Sprite.Xor(self.getImage("xor"))
        d.NOR=Sprite.Nor(self.getImage("nor"))
        d.NAND=Sprite.Nand(self.getImage("nand"))
        d.XNOR=Sprite.Xnor(self.getImage("xnor"))

        m = re.search('(T|t)ransistors: ?(\d+)',text)
        d.transistors = int(m.group(2))
        m = re.search('(?:S|s)tock: ?\[(.+)\]',text)
        gates = m.group(1)
        gates = gates.split(",")
        gates = list(map(lambda x:re.sub('\s','',x),gates))
        gates = list(map(lambda x:x.lower(),gates))
        
        def stringToGate(x):
            if (x=="and"):
                return d.AND
            elif (x=="or"):
                return d.OR
            elif (x=="not"):
                return d.NOT
            elif (x=="xor"):
                return d.XOR
            elif (x=="nor"):
                return d.NOR
            elif (x=="xnor"):
                return d.XNOR
            elif (x=="nand"):
                return d.NAND
            else:
                raise Exception("Bad gate",x)

        gates = list(map(stringToGate,gates))

        d.setGates(gates)

        w=World.World(d)

        p = re.compile('[Ss](ink|ource) ?\( ?(\d+), ?(\d+) ?\)')
        i = p.finditer(text)
        for match in i:
            x = int(match.group(2))
            y = int(match.group(3))
            if (match.group(1)=="ink"):
                s = Sprite.Sink(self.getImage("offbulb"))
                s.off = self.getImage("offbulb")
                s.on = self.getImage("onbulb")
                
            elif (match.group(1)=="ource"):
                s = Sprite.Source(self.getImage("Source"))
            s.position[0] = x
            s.position[1] = y
        
            w.sprites.append(s)

        p = re.compile ("[Gg]ate ?\((.*), ?(\d+), ?(\d+)\)")
        i = p.finditer(text)
        for match in i:
            x = int(match.group(2))
            y = int(match.group(3))
            g = copy.deepcopy(stringToGate(match.group(1)))
            g.position[0] = x
            g.position[1] = y
            w.sprites.append(g)
        return w

        
    
    
