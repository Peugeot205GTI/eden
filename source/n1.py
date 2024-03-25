import pygame
from matrice_n1 import Matrice
from pygame.locals import *
class Niveau1:
    def __init__(self):
        
        self.matrice=Matrice()
        self.matrice_monde=[]
        self.liste_des_mur=[]
        
        '''
        for i in range(len(self.matrice.variable_de_la_mort)):
            self.matrice_monde.append([])
            for j in range(len(self.matrice.variable_de_la_mort[i])):
                self.matrice_monde[i].append(self.matrice.variable_de_la_mort[i][j])
        
        self.perso=pygame.Rect(50,50,20,20)
        '''
    

    def run(self,ecranX,ecranY,ecran):
        #dessiner le perso:zzz
        #self.perso= pygame.image.load(os.path.join(os.path.dirname(__file__), 'img','machin.jpeg')).convert_alpha()
        pass
                
        #pygame.draw.rect(ecran,(255,0,0),self.perso)