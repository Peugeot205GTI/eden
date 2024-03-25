import pygame,sys,os
from pygame.locals import *
from random import *
screen = pygame.display.set_mode((853,480))



class Menu_princ:

    def __init__(self,ecran):
        self.pos_bouton_echap=pygame.Rect(0,0,50,50)
        self.bouton_pause=pygame.image.load(os.path.join(os.path.dirname(__file__), 'img','Bouton_echap.png')).convert_alpha()
        self.bouton_pause=pygame.transform.scale(self.bouton_pause,(50,50))
        self.credit_=False
        self.ecran=ecran
        self.etat="Menu_principal"
        self.fond=pygame.image.load(os.path.join(os.path.dirname(__file__), 'img','foret_magic.jpg')).convert_alpha()
        self.fond=pygame.transform.scale(self.fond,(853,480))
        self.pann=pygame.image.load(os.path.join(os.path.dirname(__file__), 'img','pancarte.png')).convert_alpha()
        self.pann=pygame.transform.scale(self.pann,(270,220))
        self.pann2=pygame.image.load(os.path.join(os.path.dirname(__file__), 'img','pancarte.png')).convert_alpha()
        self.pann2=pygame.transform.scale(self.pann2,(270,220))

    def box_text(self,surface, font, x_start, x_end, y_start, text, colour):
        x = x_start
        y = y_start
        words = text.split(' ')
        for word in words:
            ex=0
            word_t = font.render(word, True, colour)
            try:
                if len(word)>0 and word[0]=="$":
                    y += word_t.get_height() * 1.1
                    x = x_start
                    ex=1
            except IndexError:
                print("Espace en trop ! Veuillez modifier ça :\""+text+"\"")
            except Exception as e:
                print("Oh oh... Erreur non prévue :", e)
            if ex==0:
                if word_t.get_width() + x <= x_end:
                    surface.blit(word_t, (x, y))
                    x += word_t.get_width()+10
                else:
                    y += word_t.get_height() * 1.1
                    x = x_start
                    surface.blit(word_t, (x, y))
                    x += word_t.get_width()+10



    def menu(self,eventlist,clic,echap):
        self.event_list=eventlist

        if echap:
            self.credit_=False

        
        screen.blit(self.fond,(0,0))


        x, y = pygame.mouse.get_pos()



        jouer = pygame.Rect(50, 100, 200, 50)
        

        pygame.draw.rect(screen, (11, 48, 17), jouer)




        credit = pygame.Rect(300, 100, 200, 50)
        if credit.collidepoint((x, y)):
            if clic:
                self.credit_=True
                #print("mogus")
#                                if not(self.has_run):# lance la musique, ne s'execute qu'une seule fois
#                                    self.has_run= True
#                                    self.play_song(4)

        pygame.draw.rect(screen, (87, 2, 66), credit)


        
        screen.blit(self.pann,(15,-55))
        screen.blit(self.pann2,(260,-55))





        #affiche "Jouer"
        font = pygame.font.SysFont('Calibri', 40, bold=True)
        text = font.render("Jouer", True, (25, 20, 17))
        self.ecran.blit(text, (105, 105))

        #affiche "Crédits"
        
        text = font.render("Crédits", True, (25, 20, 17))
        self.ecran.blit(text, (345, 105))

        if self.credit_:
            screen.fill((0, 141, 93))

            #affiche le texte du crédit
            font = pygame.font.SysFont('Calibri', 25, bold=True)
            self.box_text(self.ecran,font,275,800, 70,"          CODE: ", (250, 250, 250))


            #affiche le texte du crédit
            font = pygame.font.SysFont('Calibri', 25)
            self.box_text(self.ecran,font,275,800,100,"Architecture du jeu : Baptiste Depuits-Moretta $ Physiques du jeu : Estéban Francillon $ Menu principal : Gaïa Jorge Coutellier $ Menu pause : Baptiste Depuits-Moretta $ Crédits et fin du jeu : Samara Alkema", (250, 250, 250))

            #affiche le texte du crédit
            font = pygame.font.SysFont('Calibri', 25, bold=True)
            self.box_text(self.ecran,font,275,800, 250,"          DESIGN: ", (250, 250, 250))


            #affiche le texte du crédit
            font = pygame.font.SysFont('Calibri', 25)
            self.box_text(self.ecran,font,275,800,280,"Monde : Estéban Francillon $ Plus : Baptiste Depuits-Moretta", (250, 250, 250))

            #affiche le texte du crédit
            font = pygame.font.SysFont('Calibri', 25, bold=True)
            self.box_text(self.ecran,font,275,800, 370,"Remerciments spéciaux : ", (250, 250, 250))

            #affiche le texte du crédit
            font = pygame.font.SysFont('Calibri', 25)
            self.box_text(self.ecran,font,275,800,410,"Musique : Clovis Dubois", (250, 250, 250))
            
            self.ecran.blit(self.bouton_pause,(self.pos_bouton_echap))
            if self.pos_bouton_echap.collidepoint((x,y)) and clic:
                self.credit_=0
        else:
            if jouer.collidepoint((x, y)):
                if clic:
                    print("maiz")
                    print(self.etat)
                    return "lancer_carte"


