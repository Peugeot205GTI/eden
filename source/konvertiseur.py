# sert a converire les sorties de tiled vers la matrice de la position dees bonhomes  
a=[[],[]]
mog=""
posx_en_cour_=False
posy_en_cour_=False
amogus=False
with open("pos_bonhomme_polution.txt") as f:
    for line in f:
        for i in line :
            
            if i=="x":
                posx_en_cour_=True
                posy_en_cour_=False
                amogus=False
            if i=="y":
                posy_en_cour_=True
                posx_en_cour_=False
                amogus=False
                
            if posx_en_cour_ or posy_en_cour_:
                if amogus and i!='\"':
                    #print(i)
                    mog+=i
                    print(i)
                if i=='\"':
                    if amogus==True:
                        print(mog)
                        print(posy_en_cour_)
                        print(posy_en_cour_)
                        
                        amogus=False
                        if posx_en_cour_:
                            a[0].append(mog)
                        if posy_en_cour_:
                            a[1].append(mog)
                        posy_en_cour_=False
                        posx_en_cour_=False
                        mog=""
                    
                    else:
                        amogus=True
            elif i=='=':
                #print(i)
                pass
            else:
                #print(i)
                posy_en_cour_=False
                posx_en_cour_=False
    a[1].remove('2')
print(a)