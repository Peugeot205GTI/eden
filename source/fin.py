import pygame,sys,os
from pygame.locals import *
import random


class FinL:
    def __init__(self):
        self.retour_menu=0
        self.pos_bouton_echap=pygame.Rect(0,0,50,50)
        self.bouton_pause=pygame.image.load(os.path.join(os.path.dirname(__file__), 'img','Bouton_echap.png')).convert_alpha()
        self.bouton_pause=pygame.transform.scale(self.bouton_pause,(50,50))
        self.posCred0 = (250,400)
        self.posCred1 = (20,130)
        self.posCred2 = (20,170)
        self.posCred3 = (20,210)
        self.posCred4 = (20,250)
        self.posCred5 = (20,290)
        self.fond=pygame.image.load(os.path.join(os.path.dirname(__file__), 'img','foret_magic.jpg')).convert_alpha()
        self.fond=pygame.transform.scale(self.fond,(853,480))
        
    def fin(self,ecran,cred1,cred2,cred3,cred4,cred5,clic,cred0):
        x, y = pygame.mouse.get_pos()
        ecran.blit(self.fond,(0,0))
        ecran.blit(cred0, self.posCred0)
        ecran.blit(cred1, self.posCred1)
        ecran.blit(cred2, self.posCred2)
        ecran.blit(cred3, self.posCred3)
        ecran.blit(cred4, self.posCred4)
        ecran.blit(cred5, self.posCred5)
        ecran.blit(self.bouton_pause,(self.pos_bouton_echap))
        if self.pos_bouton_echap.collidepoint((x,y)) and clic:
            self.retour_menu=1
        