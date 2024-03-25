import pygame,sys,os,random,math
import pygame.freetype
from pygame.locals import *
from niveau import Niveau
from menu import Menu_princ
from fin import FinL

"""
en realitée la boucle du jeux au quelle on joue (endehors des menue et de quelques autre truc) se trouve dans niveau  
"""

class Jeux:
    def __init__(self):
        self.SPACE_presse=False
        self.dialogue_début_niveau=1
        self.ecranX=853
        self.ecranY=480
        self.pos_bouton_echap=pygame.Rect(0,0,50,50)
        self.bouton1=pygame.image.load(os.path.join(os.path.dirname(__file__), 'img','position1.png')).convert_alpha()
        self.bouton1=pygame.transform.scale(self.bouton1,(75,75))
        self.pos_bouton_lvl1=pygame.Rect(488, 363,75+25,75+100)
        self.bouton2=pygame.image.load(os.path.join(os.path.dirname(__file__), 'img','position2.png')).convert_alpha()
        self.bouton2=pygame.transform.scale(self.bouton2,(75,75))
        self.texte1=pygame.image.load(os.path.join(os.path.dirname(__file__), 'img','texte1.png')).convert_alpha()
        self.texte2=pygame.image.load(os.path.join(os.path.dirname(__file__), 'img','texte2.png')).convert_alpha()
        
        self.etat_carte="Ferme"
        self.carte=pygame.image.load(os.path.join(os.path.dirname(__file__), 'img','carte.png')).convert_alpha()
        self.carte=pygame.transform.scale(self.carte,(self.ecranX,self.ecranY))
        self.bouton_pause=pygame.image.load(os.path.join(os.path.dirname(__file__), 'img','Bouton_echap.png')).convert_alpha()
        self.bouton_pause=pygame.transform.scale(self.bouton_pause,(50,50))
        self.clic=False
        self.pause=0
        self.fin = FinL()
        self.touche_bas=0
        self.touche_haut=0
        self.touche_gauche=0
        self.touche_droite=0
        self.ecran=pygame.display.set_mode((self.ecranX,self.ecranY),0,0,0,1)
        pygame.display.set_caption("Eden's spirit")
        pygame.init()
        pygame.mixer.init()
        pygame.font.init()
        
        
        self.menu_prin=Menu_princ(self.ecran)
        
        self.calibri = pygame.freetype.SysFont('Calibri', 32) 
        self.songs = [os.path.join(os.path.dirname(__file__), 'img','musique projet.mp3')]
        self.niv=Niveau(self.ecranX,self.ecranY,self.ecran)
        self.etat="Menu_principal" # sert a sacoir dans quelle etat est le jeux
        self.echap_presse=False #pour menu_pause() 
        
        
        
          
          
          
        
        self.has_run = False # pour playBGM()
        
        
        
        
        
        
        
        #attention
        # au dessus c'est la "playlist" de musique
        self.currently_playing_song = None # pour play_random_song()
        self.music_state = 'normal' # enregistre si la musique est en aleatoire ou non
        self.event_list = pygame.event.get() # remplacer tous les "pygame.event.get()" par ca, ou certains event ne seront pas pris
        self.clock=pygame.time.Clock()
        self.SONG_END = pygame.USEREVENT + 1
        pygame.mixer.music.set_endevent(self.SONG_END) # event pygame custom pour savoir si la musique en cours est finie
        # enorme section que charge les images du menu
        
        
        # enorme section que charge les images du menu (voir Menu.py)
        self.cred0, rect = self.calibri.render("Merci d'avoir joué !!!",(0,0,0),(145,40,59))
        self.cred1, rect = self.calibri.render("Programmation de la carte et de l'architecture du jeu : Baptiste",(0,0,0),(0,128,255))
        self.cred2, rect = self.calibri.render('Programmation de la physique du jeu : Esteban', (0,0,0),(0,128,255))
        self.cred3, rect = self.calibri.render('Programmation du menu principal : Gaia',(0,0,0),(0,128,255))
        self.cred4, rect = self.calibri.render('Programmation de la fin du jeu et des crédits : Samara',(0,0,0),(0,128,255))
        self.cred5, rect = self.calibri.render('Programmation de la musique : Clovis',(0,0,0),(0,128,255))
         
    
    
    
    def playBGM(self): # lance la musique, ne s'execute qu'une seule fois
        if self.has_run:
           return
        self.has_run= True
        self.play_song(0)
        
    
    
    def random_normal_choice(self): # selectionne quelle fonction utiliser pour changer de musique en fonction de l'option dans le menu
        if self.music_state == 'random' :
            self.play_random_song()
        elif self.music_state == 'normal':
            self.play_next_song()
    def play_random_song(self): # choisit une musique aleatoire
        next_song = random.choice(self.songs)
        while next_song == self.currently_playing_song:
            next_song = random.choice(self.songs)
        self.currently_playing_song = next_song
        pygame.mixer.music.load(next_song)
        pygame.mixer.music.play()
        print("random")
    def play_next_song(self): # met la musique suivante
        self.songs = self.songs[1:] + [self.songs[0]] 
        pygame.mixer.music.load(self.songs[0])
        pygame.mixer.music.play()
        print("next")
    def play_song(self,number): # joue une musique selectionée, prend un argument qui est un int avec le numero de la musique
            pygame.mixer.music.load(self.songs[number])
            pygame.mixer.music.play()
    def logique_du_jeux(self):
        pass
        
    def rafraichire_le_jeux(self):
        pygame.display.flip()
    def toggle_music_state(self): # change entre aleatoire ou a la suite
        if self.music_state == 'normal':
            self.music_state = 'random'
        else : 
            self.music_state = 'normal'
        print(self.music_state)
    
        
    def Carte(self):
        #A faire par 
        
        if self.clic and self.pos_bouton_echap.collidepoint((self.x,self.y)):
            self.etat="Menu_principal"
            self.etat_carte="Fermée"
        if self.etat_carte=="En_ouverture" and not self.clic:
            self.etat_carte="Ouverte"
        elif self.etat_carte=="Ouverte" and self.clic and self.pos_bouton_lvl1.collidepoint((self.x,self.y)):
                self.niv.niveau_actuel=1
                self.lancer_niveau()
        self.ecran.blit(self.carte,(0,0))
        self.ecran.blit(self.bouton1,(500,400))
        self.ecran.blit(self.texte1,(475,360))
        self.ecran.blit(self.bouton2,(400,200))
        self.ecran.blit(self.texte2,(370,170))
        self.ecran.blit(self.bouton_pause,(0,0))
    def lancer_niveau(self):
        self.ecran.fill((0,0,0))
        pygame.display.flip()
        self.dialogue_début_niveau=1
        self.etat="Niveau"
        self.niv.__init__(self.ecranX,self.ecranY,self.ecran)
        if self.niv.niveau_actuel==1:
            print("Level 1, launched")
        else:
            print("RED ALERT!")
    def Niveau(self):
        #Baptiste
        self.niv.niveau(self.ecranX,self.ecranY,self.ecran,self.touche_bas,self.touche_droite,self.touche_haut,self.touche_gauche,self.SPACE_presse)
        #pygame.draw.rect(surface,pygame.Rect(30, 30, 60, 60))
    def menu(self):
        self.quoi_faire=self.menu_prin.menu(True,self.clic,self.echap_presse)
        
    def Fin(self):
        #Samrasamraramogus la pompière
        self.fin.fin(self.ecran,self.cred1,self.cred2,self.cred3,self.cred4,self.cred5,self.clic,self.cred0)
        if self.fin.retour_menu==1:
            self.fin.retour_menu=0
            self.etat="Menu_principal"
        if self.echap_presse:
            self.fin.retour_menu=0
            self.etat="Menu_principal"
    
    
    
    def boucle(self): #c'est pas que lancer() Clovitano ! #maiz dit le alors
        #self.ecran.fill((0,0,0))
        while True:
            self.SPACE_presse=False
            self.event_list = pygame.event.get()
            for event in self.event_list: #Seul endroit où on peut détecter l'état des touches
                if event.type==KEYDOWN:
                    if event.key==K_DOWN:
                        self.touche_bas=1
                    elif event.key==K_UP:
                        self.touche_haut=1
                    elif event.key==K_LEFT:
                        self.touche_gauche=1
                    elif event.key==K_RIGHT:
                        self.touche_droite=1
                    elif event.key==K_ESCAPE:
                        self.echap_presse=True
                    elif event.key==K_SPACE:
                        self.SPACE_presse=True
                        
                if event.type==KEYUP:
                    if event.key==K_DOWN:
                        self.touche_bas=0
                    elif event.key==K_UP:
                        self.touche_haut=0
                    elif event.key==K_LEFT:
                        self.touche_gauche=0
                    elif event.key==K_RIGHT:
                        self.touche_droite=0
                    elif event.key==K_ESCAPE:
                        self.echap_presse=False
                    
                    
                if event.type==MOUSEBUTTONDOWN:
                    self.clic=True
                if event.type==MOUSEBUTTONUP:
                    self.clic=False
                if event.type==pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == self.SONG_END: # si la musique est finie, passer a la prochaine ou a une au hasard suivant le choix
                    self.random_normal_choice()
                    print("the song ended!")
                    
                    
                    
            if self.echap_presse==True and self.pause==0:#Les 10 prochaines lignes sont pour menu_pause
                self.pause=1
                print("Game paused !")
            elif self.pause==2 and self.echap_presse==False:
                self.pause=0
            if self.etat=="Niveau":
                if self.pause==1 or self.pause==3:
                    self.pause=self.niv.menu_pause(self.echap_presse,self.pause,self.clic)#si on est dans le niveau et qu'on appuie sur echap, le jeu se met en pause
                    if self.niv.revenir_carte==True:
                        self.niv.revenir_carte=False
                        self.etat_carte="En_ouverture"
                        self.etat="Carte"
                        self.pause=0
                    if self.niv.reinitialiser==1:
                        self.niv.reinitialiser=0
                        self.lancer_niveau()
                else:
                    if self.clic and self.pos_bouton_echap.collidepoint((self.x,self.y)):
                        self.pause=1
                    if self.pause==0:

                        if self.dialogue_début_niveau==1:
                            self.dialogue_début_niveau=self.niv.dialogue_debut(self.clic)
                        else:
                            self.Niveau()
                            self.ecran.blit(self.bouton_pause,(0,0))#afficher le bouton de pause quand on est dans Niveau (doit être blit en dernier)
            elif self.etat=="Menu_principal":
                self.menu()
                if self.quoi_faire=="lancer_carte":  
                    self.etat_carte="En_ouverture"
                    self.etat="Carte"
                    self.pause=0
            elif self.etat=="Carte":
                self.Carte()
            elif self.etat=="Fin":
                
                self.Fin()
                
            else:
                print("erreur")
            
            self.niv.costume_perso(self.touche_droite,self.touche_gauche,self.touche_haut,self.touche_bas)
            #affiche le fps 
            """
            font = pygame.font.SysFont('Calibri',40)
            fps_text = font.render("FPS: " +str(round(self.clock.get_fps(),2)), False, (255,255,255))
            self.ecran.blit(fps_text, (0, 50))
            """
            #print(self.niv.len_base*0.1)
            if self.niv.len_pas_de_base<self.niv.len_base*0.1:
                self.etat="Fin"
            #Pour avoir la position de la souris partout
            self.x, self.y = pygame.mouse.get_pos()
            #print(self.niv.liste_des_mure_groupe)
            self.playBGM()
            self.rafraichire_le_jeux()
            #######################
            self.clock.tick(60)
            
            

