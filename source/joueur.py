import pygame,sys,os
from pygame.locals import *


class Joueur(pygame.sprite.Sprite):
    def __init__(self,posX,posY,costume):
        self.image=costume
        pygame.sprite.Sprite.__init__(self)
        #self.image =pygame.transform.scale(self.image,(20,40)) # taille du perso 
        #costume.set_colorkey((187, 141, 93))
        self.rect=self.image.get_rect()
        self.rect.center = (posX,posY)
        self.mask=pygame.mask.from_surface(self.image) 
        pygame.draw.rect(self.image,(255,255,255),self.rect)

        
