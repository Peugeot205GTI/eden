import pygame,sys,os, time, math
from pygame.locals import *
import random
from n1 import Niveau1
from objet.obstacle import Obstacle
from objet.sol import sol
from objet.enemie import bohomme_polution
from joueur import Joueur


class Niveau:
    def initialisermur(self,ecranX):
            dessinX=-self.posPerso["x"]+ecranX
            dessinY=-self.posPerso["y"]
            dessinY_Base=-self.posPerso["y"]
            
            autre_variable=0
            for i in range(len(self.Niveau1.matrice.variable_de_la_mort)):
                for j in self.Niveau1.matrice.variable_de_la_mort[i]:#reversed(self.Niveau1.matrice.variable_de_la_mort[i]):
                    
                    if j=='5':
                        
                        self.sol= sol(self.trait_milieu_route,dessinX,dessinY,False,self.ecranX,self.ecranY,self.ground1_avec_herbe)
                        self.liste_tt_les_sol_groupe.add(self.sol)
                        
                        self.sol= sol(self.polution,dessinX+1,dessinY+2,False,self.ecranX,self.ecranY,self.polution)
                        self.groupe_1er_plan.add(self.sol) 
                       
                    elif j=='2':
                        #self.tailleY_visu+=1
                        self.sol= sol(self.trotoir,dessinX,dessinY,False,self.ecranX,self.ecranY,self.trotoir_gerbe)
                        self.liste_tt_les_sol_groupe.add(self.sol)    
                        self.sol= sol(self.polution,dessinX+1,dessinY+2,False,self.ecranX,self.ecranY,self.polution)
                        self.groupe_1er_plan.add(self.sol)    
                    elif j=='8':
                        #self.tailleY_visu+=1
                        if bool(random.randint(0,1)):
                            self.sol= sol(self.herbe,dessinX,dessinY,True,self.ecranX,self.ecranY,self.herbe)
                            self.liste_tt_les_sol_groupe.add(self.sol)    
                        else:
                            self.sol= sol(self.herbe2,dessinX,dessinY,True,self.ecranX,self.ecranY,self.herbe2)
                            self.liste_tt_les_sol_groupe.add(self.sol)
                        
                       
                    elif j=='6':
                        #self.tailleY_visu+=1
                        self.imebleenluimeme= sol(self.imauble,dessinX,dessinY,False,self.ecranX,self.ecranY,self.imauble)
                        self.grp_imruble.add(self.imebleenluimeme)  
                          
                    if j=='7':
                        self.obstacles= Obstacle(self.murinvisible,dessinX,dessinY)
                        
                        self.liste_des_mure_groupe.add(self.obstacles)

                        
                    elif j=='1':
                        self.sol= sol(self.ground1,dessinX,dessinY,False,self.ecranX,self.ecranY,self.ground1_avec_herbe)
                        self.liste_tt_les_sol_groupe.add(self.sol)
                        
                        self.sol= sol(self.polution,dessinX+1,dessinY+2,False,self.ecranX,self.ecranY,self.polution)
                        self.groupe_1er_plan.add(self.sol) 
                    else:
                        pass
                    dessinX+=self.tailleX_visu/2
                    dessinY+=self.tailleY_visu/2
                    
                autre_variable+=self.tailleX_visu/2
                dessinX=ecranX-self.posPerso["x"]-autre_variable
                #print(dessinX)
                dessinY_Base+=self.tailleY_visu/2
                dessinY=dessinY_Base
    
    def __init__(self,ecranX,ecranY,ecran):
        self.perso_pour_dialogue=pygame.image.load(os.path.join(os.path.dirname(__file__), 'img',"0.png")).convert_alpha()
        self.unclic=1
        self.point_de_magie=5
        self.dialogues=["Eden",
                        "$ $            Hein ?",
                        "Tu es l'Elue, tu as été choisie par la forêt.",
                        "Ton esprit n'est pas comme les autres.",
                        "Tu as vu les habitants. Ils ont été corrompus par la pollution.",
                        'Mais, comment ont-ils pû être "corrompu par la pollution" ?',
                        "La pollution a acquit une conscience... Et tu dois la détruire.",
                        "Tu dois purifier la ville, où est concentrée toute la pollution.",
                        "Mais comment suis-je censée la purifier ?",
                        "Pour utiliser ton Don de la Nature, récolte des orbes et appuie sur Espace.",
                        "Cela déploiera ta magie naturelle autour de toi, repoussera le brouillard, et quand il y en aura assez la ville sera purifiée."] # Insérer le texte du cerf magique (une phrase par indice)
        self.qui_parle=[1,2,1,1,1,2,1,1,2,1,1] # 1 pour le cerf magique, 2 pour Eden
        self.compt=0
        self.image_dialogue=pygame.image.load(os.path.join(os.path.dirname(__file__), 'img',"dialogue.jpg")).convert_alpha()
        self.image_dialogue=pygame.transform.scale(self.image_dialogue,(ecranX,ecranY))
        self.font = pygame.font.SysFont('Calibri',40,True)
        pygame.mixer.init
        self.son_pas=[pygame.mixer.Sound(os.path.join(os.path.dirname(__file__), 'img','pas1.wav')),pygame.mixer.Sound(os.path.join(os.path.dirname(__file__), 'img','pas2.wav')),pygame.mixer.Sound(os.path.join(os.path.dirname(__file__), 'img','pas3.wav')),pygame.mixer.Sound(os.path.join(os.path.dirname(__file__), 'img','pas4.wav'))]
        self.paspas=0
        self.quel_pas=0
        self.reinitialiser=0
        self.compteur=0
        self.costume=10
        self.changer_costume=0
        self.dico_des_costumes={}
        for i in range(4):#pour importer les images des costumes #gg baptiste 
            for l in range(3):
                self.dico_des_costumes[str(i*10+l)]=pygame.image.load(os.path.join(os.path.dirname(__file__), 'img',str(i*10+l)+".png")).convert_alpha()
        #print(self.dico_des_costumes)
        self.ecranX=ecranX
        self.ecranY=ecranY
        self.revenir_carte=False
        self.ecran=ecran
        self.pause=0
        #self.jeux=Jeux()
        self.vitesse_de_deplacement=2 # entiier et fait des lag spike
        self.now = time.time()
        self.dt,self.prev_time = 0,0
        
        self.couleur_bare=(0,150,0)
        self.couleur_bare_fond=(0,30,0)
        
        self.fund_bare=pygame.Rect(25,75,7,300)
        self.avant_bare=pygame.Rect(25,75,7,0)
        self.longeur_bare=300
        
        
        
        self.vitesse=3
        self.vitesse_base=3
        self.vitesse_x_base=self.vitesse
        self.vitesse_y_base=self.vitesse
        self.vitesse_x=self.vitesse
        self.vitesse_y=self.vitesse
        self.vitesse_diag=round(math.sqrt((self.vitesse**2)/2), 5) # pk un round? --> tkt, les performance tout ca tout ca 
        self.dx=self.vitesse_diag
        self.dy=self.vitesse_diag
        self.niveau_actuel=1
        self.has_run = False # pour playBGM()
        self.tailleX=130
        self.tailleY=99
        self.tailleX_visu=131
        self.tailleY_visu=66
        
        self.orbe = pygame.image.load(os.path.join(os.path.dirname(__file__), 'img','Orb_03.png')).convert_alpha()
        self.orbe=pygame.transform.scale(self.orbe,(40,40))
        
        
        self.orbe_compteur = pygame.image.load(os.path.join(os.path.dirname(__file__), 'img','Orb_10.png')).convert_alpha()
        self.orbe_compteur=pygame.transform.scale(self.orbe_compteur,(40,40))
        
        
        self.ground1 = pygame.image.load(os.path.join(os.path.dirname(__file__), 'img/city','sol_goudron.png')).convert_alpha()
        self.ground1=pygame.transform.scale(self.ground1,(self.tailleX,self.tailleY))
        
        self.ground1_avec_herbe = pygame.image.load(os.path.join(os.path.dirname(__file__), 'img/Valides',"sol_base_qui_die_goudron.png")).convert_alpha()
        self.ground1_avec_herbe=pygame.transform.scale(self.ground1_avec_herbe,(self.tailleX,self.tailleY))
        
        
        self.bord = pygame.image.load(os.path.join(os.path.dirname(__file__), 'img/city','bord_goudron.png')).convert_alpha()
        self.bord=pygame.transform.scale(self.bord,(self.tailleX,self.tailleY))
        
        self.water = pygame.image.load(os.path.join(os.path.dirname(__file__), 'img','water.png')).convert_alpha()
        self.water=pygame.transform.scale(self.water,(self.tailleX,self.tailleY))
        
        self.murinvisible = pygame.image.load(os.path.join(os.path.dirname(__file__), 'img','mur_invisible.png')).convert_alpha()
        self.murinvisible=pygame.transform.scale(self.murinvisible,(self.tailleX,self.tailleY))
        
        self.trotoir = pygame.image.load(os.path.join(os.path.dirname(__file__), 'img/city','sol_base.png')).convert_alpha()
        self.trotoir=pygame.transform.scale(self.trotoir,(self.tailleX,self.tailleY))
        
        self.trotoir_gerbe = pygame.image.load(os.path.join(os.path.dirname(__file__), 'img/Valides','sol_base_qui_die2+.png')).convert_alpha()
        self.trotoir_gerbe =pygame.transform.scale(self.trotoir_gerbe,(self.tailleX,self.tailleY))
        
        
        self.herbe = pygame.image.load(os.path.join(os.path.dirname(__file__), 'img/Valides',"sol_base_touffes_d'herbes+DESFLEURS+.png")).convert_alpha()
        self.herbe=pygame.transform.scale(self.herbe,(self.tailleX,self.tailleY))
        
        self.herbe2 = pygame.image.load(os.path.join(os.path.dirname(__file__), 'img/Valides',"sol_base_touffes_d'herbes2+.png")).convert_alpha()
        self.herbe2=pygame.transform.scale(self.herbe2,(self.tailleX,self.tailleY))
        
        
        self.polution = pygame.image.load(os.path.join(os.path.dirname(__file__), 'img/city','brouillard.png')).convert_alpha()
        self.polution=pygame.transform.scale(self.polution,(self.tailleX*2+7,self.tailleY*2+7))
        
        
        self.trait_milieu_route = pygame.image.load(os.path.join(os.path.dirname(__file__), 'img/city','lignie_du_milieu.png')).convert_alpha()
        self.trait_milieu_route=pygame.transform.scale(self.trait_milieu_route,(self.tailleX,self.tailleY))
        
        self.imauble = pygame.image.load(os.path.join(os.path.dirname(__file__), 'img','imeuble.png')).convert_alpha()
        self.imauble=pygame.transform.scale(self.imauble,(self.tailleX*8,self.tailleY*8))
        
        self.Niveau1=Niveau1()
        self.liste_des_mure_groupe=pygame.sprite.Group()
        self.liste_tt_les_sol_groupe=pygame.sprite.Group()
        self.groupe_perso=pygame.sprite.Group()
        self.groupe_1er_plan=pygame.sprite.Group()
        self.grp_imruble=pygame.sprite.Group()
        self.grp_orbe=pygame.sprite.Group()
        
        self.le_joueur=Joueur(ecranX/2,ecranY/2,pygame.image.load(os.path.join(os.path.dirname(__file__), 'img',"10.png")).convert_alpha())
        self.groupe_perso.add(self.le_joueur)
        #self.posPerso={"x":0,"y":0}
        posPerso_x=4895#{"x":0,"y":0}
        posPerso_y=3000
        self.posPerso={"x":posPerso_x,"y":posPerso_y}
        self.CONST_posPerso_origine={"x":posPerso_x,"y":posPerso_y}
        
        
        #self.imebleenluimeme= sol(self.imauble,4830,3100,False)
        #self.groupe_1er_plan.add(self.imebleenluimeme)
        pospolution=[['0','5133', '5063', '4905', '4925', '4499', '4600', '4710', '4719', '4927', '4489', '3871', '4407', '4179', '4023', '4007', '4437.12', '4081.06', '3878.03', '3902.27', '3903.79', '3890.18', '3641.67', '3696.21', '3291.67', '3361.36', '3388.64', '3459.85', '3159.85', '3338.64', '3568.94', '3665.91', '2793', '2693', '3029', '2949', '2541', '2349'],
                     ['0','1435', '1265', '831',  '603',  '869',  '1173', '1173', '979',  '681',  '535',  '833',  '1361', '941',  '569',  '1073', '1059.85', '1276.52', '1206.82', '1279.55', '1284.09', '1100.76', '788.636', '637.121', '568.939', '862.879', '902.273', '1109.85', '634.091', '721.97',  '1097.73', '1346.21', '743',  '363',  '1067', '1179', '643',  '499']]
        pospolutionfloat=[[],[]]
        compter=0
        for i in pospolution:
            for j in i :
                pospolutionfloat[compter].append(float(j))
            compter+=1    
        self.list_pos_bohomme_polutionX=pospolutionfloat[0]#[0,4640,4830,4550]
        self.list_pos_bohomme_polutionY=pospolutionfloat[1]#[0,2900,3100,3050]
        
        self.groupe_bohomme_polution=pygame.sprite.Group()
        for i in range(len(self.list_pos_bohomme_polutionX)):
            self.groupe_bohomme_polution.add(bohomme_polution(self.list_pos_bohomme_polutionX[i],self.list_pos_bohomme_polutionY[i],ecranX,ecranY,ecran))#self.list_pos_bohomme_polutionX[i]-self.posPerso["x"]+ecranX,self.list_pos_bohomme_polutionY[i]-self.posPerso["y"],ecran))
        self.groupe_bohomme_polution.update(-posPerso_x,-posPerso_y,self.posPerso,False,False,self.groupe_bohomme_polution)
        
        
        pospolutionfloat=[[882, 434, 271, -3, -132, 552, -104, -466, -937, -715, -1207, -1732, -2176, -2037, -2643, -2999, -2826, -3277, -3750, -3430, -3465, -3401, -3733, -3674, -4120, -4504, -4155, -4072, -3785, -4299, -4647, -4755, -4893, -4563, -4299, -2329, -2528, -1991, -1574, -1398, -1379, -1753, -929, -277],
                          [-153, -84, -462, -386, -192, -298, -639, -432, -545, -1003, -1067, -1093, -1018, -1485, -1614, -1614, -1941, -1963, -1829, -1632, -1861, -2320, -2277, -2040, -2040, -2168, -2464, -2228, -2553, -2693, -2708, -2557, -2492, -2344, -2378, -1575, -1302, -1283, -1465, -832, -507, -705, -247, -65]]
        for i in range(len(pospolutionfloat[0])):
            self.grp_orbe.add(sol(self.orbe,pospolutionfloat[0][i]-250,pospolutionfloat[1][i]+200,False,self.ecranX,self.ecranY,self.orbe))#self.list_pos_bohomme_polutionX[i]-self.posPerso["x"]+ecranX,self.list_pos_bohomme_polutionY[i]-self.posPerso["y"],ecran))
        #self.grp_orbe.update(-posPerso_x/2-self.ecranX,-posPerso_y+self.ecranY/2)
        
        self.initialisermur(ecranX)
        self.len_base=len(self.groupe_1er_plan)
        self.len_pas_de_base=len(self.groupe_1er_plan)
    
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
                print("Oh oh... Erreur non prévue :", e) # whaou jolie code baptiste
            if ex==0:
                if word_t.get_width() + x <= x_end:
                    surface.blit(word_t, (x, y))
                    x += word_t.get_width()+10
                else:
                    y += word_t.get_height() * 1.1
                    x = x_start
                    surface.blit(word_t, (x, y))
                    x += word_t.get_width()+10
    
    
    def costume_perso(self,touche_droite,touche_gauche,touche_haut,touche_bas):
        self.compteur+=1
        if self.compteur>6:#temps avant de changer de costume
            self.compteur=0
            self.changer_costume=1
        if touche_haut or touche_gauche or touche_droite or touche_bas:
            if self.paspas>=20:
                self.paspas=0
                if self.quel_pas>=4:
                    self.quel_pas=0
                else:
                    self.quel_pas+=1
                pygame.mixer.Sound.play(self.son_pas[self.quel_pas-1])
            else:
                self.paspas+=1
        if touche_haut and self.changer_costume:
            self.changer_costume=0
            if self.costume<2 and self.costume>=0:#les numéros des images de costumes sont en rapport avec la variable
                self.costume+=1#entre 0 et 2: vers le haut -> possibilité d'améliration de la qualité de l'animation
            else:
                self.costume=0
        elif touche_bas and self.changer_costume:
            
            self.changer_costume=0
            if self.costume<12 and self.costume>=10:#entre 10 et 12: vers le bas
                self.costume+=1
            else:
                self.costume=10
        elif touche_droite and self.changer_costume:
            self.changer_costume=0
            if self.costume<22 and self.costume>=20:#20 à 30 : droite
                self.costume+=1
            else:
                self.costume=20
        elif touche_gauche and self.changer_costume:
            self.changer_costume=0
            if self.costume<32 and self.costume>=30:#30 à 40 : gauche
                self.costume+=1
            else:
                self.costume=30
        self.costum_perso=self.dico_des_costumes[str(self.costume)]
        self.groupe_perso=pygame.sprite.Group()
        self.le_joueur=Joueur(self.ecranX/2,self.ecranY/2,self.costum_perso)
        self.groupe_perso.add(self.le_joueur)   
    
    def dessiner_compteur_orbe_magie(self,ecran,ecranX):
        for i in range(self.point_de_magie):
            ecran.blit(self.orbe_compteur,(ecranX-40*(i+1),0))
    def norme_de_vcteur(self,x,y):
        return (math.sqrt(x**2+y**2))
    
    def deplacements_monde(self,v_x,v_y):
        self.liste_des_mure_groupe.update(v_x,v_y)
        self.groupe_1er_plan.update(v_x,v_y)
        self.grp_imruble.update(v_x,v_y)
        self.grp_orbe.update(v_x,v_y)
        
        self.liste_tt_les_sol_groupe.update(v_x,v_y)
        self.groupe_bohomme_polution.update(v_x,v_y,self.posPerso,False,False,[self.groupe_bohomme_polution,self.groupe_perso])
        self.posPerso["y"]+=-v_y
        self.posPerso["x"]+=-v_x
        #print(self.posPerso)
        #print(self.posPerso["x"]-self.CONST_posPerso_origine["x"],self.posPerso["y"]-self.CONST_posPerso_origine["y"])
        #print(self.posPerso["x"],self.CONST_posPerso_origine["x"],self.posPerso["y"],self.CONST_posPerso_origine["y"])
        
    def rectifovation_deltatime(self):
        self.now = time.time()
        self.dt = self.now - self.prev_time
        self.prev_time = self.now
        
        self.vitesse=self.vitesse_base*self.dt*100
        
        self.vitesse_x_base=self.vitesse
        self.vitesse_y_base=self.vitesse
        self.vitesse_x=self.vitesse
        self.vitesse_y=self.vitesse
        self.vitesse_diag=round(math.sqrt((self.vitesse**2)/2), 5) # non ca fait pas lager je vous jure j'ai testé
        #print(self.dt)
    
    def deplacement_et_colision(self,ecran,touche_bas,touche_droite,touche_haut,touche_gauche,ecranX,ecranY):
        if (touche_bas and touche_droite) or (touche_bas and touche_gauche) or (touche_haut and touche_droite) or (touche_haut and touche_gauche):
            # Calculer le mouvement diagonal
            
            self.vitesse_y = self.vitesse_x = self.vitesse_diag
            
            if touche_haut and touche_bas: # oui j'avait la flemme de rajouter ca dans le if 
                self.vitesse_x=self.vitesse_x_base
                self.vitesse_y=self.vitesse_y_base
            if touche_droite and touche_gauche:
                self.vitesse_x=self.vitesse_x_base
                self.vitesse_y=self.vitesse_y_base
            # Appliquer le mouvement diagonal
            #self.liste_des_mure_groupe.update(-dx, -dy)
            #self.liste_tt_les_sol_groupe.update(-dx, -dy)
            
            # Vérifier les collisions après le mouvement diagonal
            '''
            if pygame.sprite.spritecollide(self.le_joueur, self.liste_des_mure_groupe, False, pygame.sprite.collide_mask):
                self.liste_des_mure_groupe.update(dx, dy)
                self.liste_tt_les_sol_groupe.update(dx, dy)
            return
            '''
        else:
            self.vitesse_x=self.vitesse_x_base
            self.vitesse_y=self.vitesse_y_base
        #print(pygame.sprite.spritecollide(self.le_joueur, self.liste_des_mure_groupe, False) != [],pygame.sprite.spritecollide(self.le_joueur,self.groupe_bohomme_polution,False) != [] )
        if touche_bas==1:
            self.deplacements_monde(0,-self.vitesse_y)
            
            if pygame.sprite.spritecollide(self.le_joueur, self.liste_des_mure_groupe, False) != [] or pygame.sprite.spritecollide(self.le_joueur,self.groupe_bohomme_polution,False) != [] :
                if pygame.sprite.spritecollide(self.le_joueur, self.liste_des_mure_groupe, False, pygame.sprite.collide_mask)!=[]  :
                    self.deplacements_monde(0,self.vitesse_y)
                    
                if pygame.sprite.spritecollide(self.le_joueur,self.groupe_bohomme_polution,False) != [] :
                    self.deplacements_monde(0,self.vitesse_y)
                    
            #return

        if touche_haut==1:
            
            self.deplacements_monde(0,self.vitesse_y)
            
            if pygame.sprite.spritecollide(self.le_joueur, self.liste_des_mure_groupe, False) != [] or pygame.sprite.spritecollide(self.le_joueur,self.groupe_bohomme_polution,False) != [] :
                if pygame.sprite.spritecollide(self.le_joueur, self.liste_des_mure_groupe, False, pygame.sprite.collide_mask)!=[] :
                    self.deplacements_monde(0,-self.vitesse_y)
                    
                if pygame.sprite.spritecollide(self.le_joueur,self.groupe_bohomme_polution,False) != [] :
                    self.deplacements_monde(0,-self.vitesse_y)
                    
            #return
                    

        if touche_droite==1:
            
            self.deplacements_monde(-self.vitesse_x,0)
            
            if pygame.sprite.spritecollide(self.le_joueur, self.liste_des_mure_groupe, False) != [] or pygame.sprite.spritecollide(self.le_joueur,self.groupe_bohomme_polution,False) != [] :
                if pygame.sprite.spritecollide(self.le_joueur, self.liste_des_mure_groupe, False, pygame.sprite.collide_mask)!=[] :
                    self.deplacements_monde(self.vitesse_x,0)
                     
                if pygame.sprite.spritecollide(self.le_joueur,self.groupe_bohomme_polution,False) != [] :
                    self.deplacements_monde(self.vitesse_x,0)
                    
            #return
               
        if touche_gauche==1:
            self.deplacements_monde(self.vitesse_x,0)
            
            if pygame.sprite.spritecollide(self.le_joueur, self.liste_des_mure_groupe, False) != [] or pygame.sprite.spritecollide(self.le_joueur,self.groupe_bohomme_polution,False) != [] :
                if pygame.sprite.spritecollide(self.le_joueur, self.liste_des_mure_groupe, False, pygame.sprite.collide_mask)!=[] :
                    self.deplacements_monde(-self.vitesse_x,0)
                    
                if pygame.sprite.spritecollide(self.le_joueur,self.groupe_bohomme_polution,False) != [] :
                    self.deplacements_monde(-self.vitesse_x,0)
                    
            #return
        
    def dialogue_debut(self,clic):
        self.ecran.blit(self.image_dialogue,(0,0))
        self.ecran.blit(self.perso_pour_dialogue,(320,425))
        if self.unclic and not clic:
            #print("clic dispo")
            self.unclic=0
        if clic and not self.unclic and self.compt+1==len(self.dialogues):
            #print("fin du dialogue")
            self.compt=0
            return 0
        if self.compt+1<=len(self.dialogues):
            if self.qui_parle[self.compt]==1:
                self.box_text(self.ecran,self.font,326.5,self.ecranX,45,self.dialogues[self.compt],(255,255,255))
            elif self.qui_parle[self.compt]==2:
                self.box_text(self.ecran,self.font,10,300,280,self.dialogues[self.compt],(200,100,0))
        if clic and not self.unclic:
            #print("dialogue suivant")
            self.compt+=1
            self.unclic=1
            return 1
        else:
            return 1
    def menu_pause(self,echap_presse,pause,clic):
        x, y = pygame.mouse.get_pos()
        bouton_rependre=pygame.Rect(300,54,220,73)
        bouton_quitter=pygame.Rect(300,317,248,71)
        bouton_reinitialiser=pygame.Rect(300,184,248,73)
        self.pause=pause
        affichage=pygame.image.load(os.path.join(os.path.dirname(__file__), 'img','Affichage_menu_pause.png')).convert_alpha()
        self.ecran.blit(affichage,(0,0))
        if clic and bouton_reinitialiser.collidepoint((x,y)):
            self.reinitialiser=1
        elif clic and bouton_quitter.collidepoint((x,y)):
            self.revenir_carte=True
        if self.pause==3 and echap_presse or clic and self.pause==3 and bouton_rependre.collidepoint((x,y)) or self.reinitialiser==1:
            print("Return to level")
            return 2
        elif not echap_presse and self.pause==1:
            return 3
        else:
            return self.pause
    
    def niveau(self,ecranX,ecranY,ecran,touche_bas,touche_droite,touche_haut,touche_gauche,espase_presser):
        ecran.fill((0, 0, 0))
        
        #print(espase_presser)
        if espase_presser and (self.point_de_magie>0) :
            #print(self.point_de_magie)
            #self.grp_orbe.add(sol(self.orbe,0+self.ecranX/2,0+self.ecranY/2,False,self.ecranX,self.ecranY,self.orbe))
            for i in pygame.sprite.spritecollide(self.le_joueur,self.liste_tt_les_sol_groupe,False):
                i.tranformation=True
                pygame.sprite.spritecollide(i,self.groupe_1er_plan,True)
            self.point_de_magie-=1
        
                
        if pygame.sprite.spritecollide(self.le_joueur, self.grp_orbe, False) != []:
            for i in pygame.sprite.spritecollide(self.le_joueur, self.grp_orbe, True):
                self.point_de_magie+=1
        
        #deplacement et colision
        
        self.rectifovation_deltatime()
        
        self.deplacement_et_colision(ecran,touche_bas,touche_droite,touche_haut,touche_gauche,ecranX,ecranY)
        
        self.liste_tt_les_sol_groupe.update(0,0)
        
        self.liste_tt_les_sol_groupe.draw(ecran)
        
        self.groupe_perso.draw(ecran)
        
        self.groupe_bohomme_polution.update(0,0,self.posPerso,True,True,[self.groupe_bohomme_polution,self.groupe_perso])
        repouser= False
        for i in self.groupe_bohomme_polution:
            if i.pousse_le_joueur: 
                repouser= True
                mvmt:list=i.mouvemet
                #print(mvmt)
        if repouser:
            self.deplacements_monde(mvmt[0]*2,mvmt[1]*2)
            if pygame.sprite.spritecollide(self.le_joueur, self.liste_des_mure_groupe, False) != [] or pygame.sprite.spritecollide(self.le_joueur,self.groupe_bohomme_polution,False) != [] :
                if pygame.sprite.spritecollide(self.le_joueur, self.liste_des_mure_groupe, False, pygame.sprite.collide_mask)!=[] :
                    self.deplacements_monde(-mvmt[0]*2,-mvmt[1]*2)
                
                if pygame.sprite.spritecollide(self.le_joueur,self.groupe_bohomme_polution,False) != [] :
                    self.deplacements_monde(-mvmt[0]*2,-mvmt[1]*2)
        
        """
        for i in pygame.sprite.spritecollide(self.le_joueur,self.groupe_bohomme_polution,False):
            print("colision")
            #i.update(0,0,self.posPerso,True,False,self.groupe_bohomme_polution)
        """
        #pygame.sprite.spritecollide(self.le_joueur,self.groupe_1er_plan,True) 
        '''
        print(self.grp_orbe)
        
        print([i for i in self.grp_orbe])
        
        print([i.rect.x for i in self.grp_orbe])
        print([i.rect.y for i in self.grp_orbe])
        '''
        #print(len(self.groupe_1er_plan))
        self.len_pas_de_base=len(self.groupe_1er_plan)
        self.groupe_bohomme_polution.draw(ecran)
        
        
        self.liste_des_mure_groupe.draw(ecran)
        self.grp_orbe.draw(ecran)
        self.grp_imruble.draw(ecran)
        
        self.groupe_1er_plan.draw(ecran)
        
        self.dessiner_compteur_orbe_magie(ecran,ecranX)
        
        self.avant_bare=pygame.Rect(25,75,7,self.longeur_bare-((self.len_pas_de_base-self.longeur_bare*0.1)*self.longeur_bare)/(self.len_base-self.longeur_bare*0.1))#potit peoduit en croix
        pygame.draw.rect(ecran,self.couleur_bare_fond,self.fund_bare)
        pygame.draw.rect(ecran,self.couleur_bare,self.avant_bare)
        ### test
        #self.grp_orbe.draw(ecran)
        
        #print(pygame.time.get_ticks())
        
        #ecran.blit(self.imauble, self.imauble.get_rect())
        #print(self.posPerso)
        if self.niveau_actuel==1:
            self.Niveau1.run(ecranX,ecranY,ecran)
        #print(self.vitesse_x,self.vitesse_y)
        #self.liste_des_mure_groupe.draw(ecran)
        