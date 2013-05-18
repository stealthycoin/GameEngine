#mouse movement unimplemented, only clicking and key presses so far
#TODO: Add mouse movement stuff

import pygame
import numpy as np

class InputManager:
    def __init__(self):
        #dictionaries of actions
        self.keyActions = {}
        self.mouseActions = {}
        self.buttons = {1:0}
        self.mouse = [0,0]

    def getMouseX(self):
        return self.mouse[0]

    def getMouseY(self):
        return self.mouse[1]

    def process(self, event):
        """this takes in raw pygame events and figures out what to do with them"""
        print(self.buttons)
        if event.type == pygame.KEYDOWN:
            self.keyPressed(event.key)
        elif event.type == pygame.KEYUP:
            self.keyReleased(event.key)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            self.buttons[event.button] = 1
            self.mousePressed(event.button)
        elif event.type == pygame.MOUSEBUTTONUP:
            self.mouseReleased(event.button)
            self.buttons[event.button] = 0
        elif event.type == pygame.MOUSEMOTION:
            self.mouse =  event.pos
            
        
    def mapToKey(self, gameAction, keyCode):
        """adds a key -> gameAction mapping"""
        self.keyActions[keyCode] = gameAction

    def mapToMouse(self, gameAction, mouseCode):
        """adds a mouse -> gameAction mapping"""
        self.mouseActions[mouseCode] = gameAction

        
    def clearMap(self, gameAction):
        """removes this game action from all maps"""
        self.keyActions = filter(lambda x:x != gameAction, self.keyActions)
        self.mouseActions = filter(lambda x:x != gameAction, self.mouseActions)
        gameAction.reset()

    def resetGameActions(self):
        """Reset every game action to the unpressed state"""
        for action in self.keyActions:
            action.reset()
        for action in self.mouseActions:
            action.reset()

    def keyPressed(self, code):
        """Press the gameAction associated with the given key code"""
        try:
            self.keyActions[code].press()
        except KeyError:
            pass
        
    def keyReleased(self, code):
        """Release the gameAction associated with the given key code"""
        try:
            self.keyActions[code].release()
        except KeyError:
            pass

    def mousePressed(self, code):
        """Press the gameAction associated with the given key code"""
        try:
            self.mouseActions[code].press()
        except KeyError:
            pass
        
    def mouseReleased(self, code):
        """Release the gameAction associated with the given key code"""
        try:
            self.mouseActions[code].release()
        except KeyError:
            pass




    
