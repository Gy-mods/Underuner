import pygame
import sys
pygame.init()

#képernyő mérete
screen = pygame.display.set_mode((1408, 856))

#név és ikon
pygame.display.set_caption("Underformer")
icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)

#Változók
clock = pygame.time.Clock()


######################################################################################################

#IMPORT ASSETS

menu_background_surface = pygame.image.load("menu.png")
snowdin_background_surface = pygame.image.load("background.png")
snowdin_wall_tile = pygame.image.load("wall.png")
snowdin_wallup_tile = pygame.image.load("wall_up.png")
snowdin_floor_tile = pygame.image.load("floor.png")
snowdin_floorup_tile = pygame.image.load("floor_up.png")
sans_left = pygame.image.load("sans_left.png")
sans_left_a = pygame.image.load("sans_left_A.png")
sans_left_b = pygame.image.load("sans_left_B.png")
sans_base = pygame.image.load("sans.png")
sans_base_wink = pygame.image.load("sans_wink.png")
small_b = pygame.image.load('small_bone.png')
avarage_b =pygame.image.load('avarage_bone.png')
big_b =pygame.image.load('big_bone.png')
giant_b =pygame.image.load('giant_bone.png')
heart = pygame.image.load('heart.png')

########################################################################################################






def menu():
    screen.blit(menu_background_surface, (0,0))
    pygame.display.flip()
    pygame.mixer.music.load("menu.ogg")
    pygame.mixer.music.play(-1)


    start_button = pygame.Rect(626,307,172,184)

    fut = True
    while fut == True:
        
        
        for event in pygame.event.get():
            
            
            
    #Kilépő (nem bír magától kilépni Bruh)        
            
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
                
                
                
    #gomb            
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if start_button.collidepoint(x, y):
                    print("bruh")
                    return
                
        #tick és update        
        pygame.display.update()
        clock.tick(60)
        






def snowdin():
    screen = pygame.display.set_mode((1306, 856))
    pygame.mixer.music.load("phase_1.ogg")
    pygame.mixer.music.play(-1)      
        

#FG változók
    fut = True
    szint = 540
    
    
    #Karakter irányítási változók:
    ugras = 0
    ugrasi_magassag = szint + 72 #(Alapból ez "0"-nak felel meg)
    ugrasi_speed = 0
    gravity = 0.7
    ukezdo_speed = -11
    back = 0
    forwardding = 32
    
    #Csontik:
    csont_properties = [[14*60,small_b]]
    csont_rush = 1
    
    #cutscene váktozók:
    sans_pos=17*80
    sans_ab = 0
    cutscene = 0
    
#####################################################################################
    while fut == True:
        
#Math

        ugrasi_magassag += ugrasi_speed
        ugrasi_speed += gravity
        if ugrasi_magassag >= szint+72:
            ugrasi_speed = 0
            ugrasi_magassag = szint + 72
            ugras = 0  

        if cutscene == 1:
            if back == 1:
                forwardding -= 1.2
                #back = 0
            else:
                forwardding += 0.6
                
        if forwardding < 32:
            forwardding = 32
        #for csont in csont_properties:
        #    csont[0] -= csont_rush
        #if csont_properties[0][0] < 10:
        #   csont_properties.pop(0)

#####################################################################################
        
        screen.blit(snowdin_background_surface, (0,0))
        
        for x in range(17):
            screen.blit(snowdin_floorup_tile, (0+x*80,400))
            screen.blit(snowdin_floor_tile,(0+x*80,480))
            screen.blit(snowdin_floor_tile,(0+x*80,560))
            screen.blit(snowdin_wallup_tile,(0+x*80,640))
            screen.blit(snowdin_wall_tile,(0+x*80,720))
            screen.blit(snowdin_wall_tile,(0+x*80,800))
            screen.blit(snowdin_wall_tile,(0+x*80,880))
            
        #screen.blit(small_b,(60, szint))
        #screen.blit(avarage_b,(90, szint))
        #screen.blit(big_b,(120, szint))
        #screen.blit(giant_b,(150, szint))
######################################################################################            
            
        if cutscene == 0:

            if sans_ab == 52:
                sans_ab = 0
                
            if sans_ab < 13:
                screen.blit(sans_left, (sans_pos, szint))
                sans_ab += 1
                
            elif sans_ab < 26:
                screen.blit(sans_left_a, (sans_pos, szint))
                sans_ab += 1
                
            elif sans_ab < 39:
                screen.blit(sans_left, (sans_pos, szint))
                sans_ab += 1    
                
            elif sans_ab < 52:
                screen.blit(sans_left_b, (sans_pos, szint))
                sans_ab += 1   
        else:
            screen.blit(sans_left, (14*80, szint))    
#######################################################################################
        
        #Játék rajzolás:
        #for csont in csont_properties:
        #    screen.blit(csont[1],(csont[0],szint+57))
        
        screen.blit(heart, (forwardding,ugrasi_magassag))
            
            
            
####################################           
####################################
                                 ###
        pygame.display.flip()    ###
                                 ###
####################################       
####################################  

     
        #Cutscene:
        sans_pos -= 2    
        if sans_pos == 14*80:
            cutscene = cutscene + 1
                
#################################################################################################
     
#Eventek (detection)        
        for event in pygame.event.get():   

#Billentyűzet eventek:
            if event.type == pygame.KEYDOWN:
                
                
                if event.key == pygame.K_LALT:
                    back = 1
                
                              
                if event.key == pygame.K_SPACE:
                    if ugras == 0:
                        ugras = 1
                        ugrasi_speed = ukezdo_speed               
                    elif ugras == 1:
                        ugras = 2
                        ugrasi_speed = ukezdo_speed
            
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LALT:
                    back = 0             
                
#Kilépő (nem bír magától kilépni Bruh)
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()       
        #tick és update        
        #pygame.display.update()
        clock.tick(60)

###################################################################################################
        
menu()
snowdin()
