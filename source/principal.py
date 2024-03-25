
toute_les_librairies=True
try:
    import pygame,sys,os,random
    from pygame.locals import *
    from jeux import Jeux

except ImportError as error:
    print("une des librairie n'est pas instalée")
    print(error)
    toute_les_librairies=False
    

if __name__ == '__main__' and toute_les_librairies:
    # j'ai deplacé l'initialisation de pygame dans jeux.py, ca causait des problemes ici

    jeux=Jeux()
    jeux.boucle()