import pygame
import time
import GameManager
import InputManager
import traceback

pygame.init()
running = True
screen_width=1300
screen_height=700
screen=pygame.display.set_mode([screen_width,screen_height])
pygame.display.set_caption("Logistix")

try:
    im=InputManager.InputManager()
    gm=GameManager.GameManager((screen_width,screen_height), im)

    t=pygame.time.get_ticks()


    while running:
        oldtime=t
        t=pygame.time.get_ticks()
        
        #TODO add event processing system
        for e in pygame.event.get():
            if pygame.QUIT==e.type:
                running=False
            elif e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
                running=False
            else:
                im.process(e)
        gm.update(t-oldtime)
        gm.draw(screen)
        pygame.display.flip()       
        time.sleep(0.01)

except:
    traceback.print_exc()
    
pygame.quit()

# core-s->gm-s->worls-s->tons of sprites
