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

    
    
    # screen.blit(snowdin_background_surface, (0,0))
    
    # for x in range(17):
    #     screen.blit(snowdin_floorup_tile, (0+x*80,400))
    #     screen.blit(snowdin_floor_tile,(0+x*80,480))
    #     screen.blit(snowdin_floor_tile,(0+x*80,560))
    #     screen.blit(snowdin_wallup_tile,(0+x*80,640))
    #     screen.blit(snowdin_wall_tile,(0+x*80,720))
    #     screen.blit(snowdin_wall_tile,(0+x*80,800))
    #     screen.blit(snowdin_wall_tile,(0+x*80,880))
    # screen.blit(sans, (17*80, 540))
    # pygame.display.flip()

    # for insans in range(17*80, 14*80, -5):
    #     screen.blit(sans, (insans, 540))
        
        

    #fg változók
    sans_pos=17*80
    sans_ab = 0
    fut = True
    cutscene = 0
    while fut == True:
        
        screen.blit(snowdin_background_surface, (0,0))
        for x in range(17):
            screen.blit(snowdin_floorup_tile, (0+x*80,400))
            screen.blit(snowdin_floor_tile,(0+x*80,480))
            screen.blit(snowdin_floor_tile,(0+x*80,560))
            screen.blit(snowdin_wallup_tile,(0+x*80,640))
            screen.blit(snowdin_wall_tile,(0+x*80,720))
            screen.blit(snowdin_wall_tile,(0+x*80,800))
            screen.blit(snowdin_wall_tile,(0+x*80,880))
            
            
            
        if cutscene == 0:

            if sans_ab == 52:
                sans_ab = 0
                
            if sans_ab < 13:
                screen.blit(sans_left, (sans_pos, 540))
                sans_ab += 1
                
            elif sans_ab < 26:
                screen.blit(sans_left_a, (sans_pos, 540))
                sans_ab += 1
                
            elif sans_ab < 39:
                screen.blit(sans_left, (sans_pos, 540))
                sans_ab += 1    
                
            elif sans_ab < 52:
                screen.blit(sans_left_b, (sans_pos, 540))
                sans_ab += 1
            
        else:
            screen.blit(sans_left, (14*80, 540))    
            
            
        pygame.display.flip()
    
        sans_pos -= 2
        #FUN
        if sans_pos == 14*80:
            cutscene = cutscene + 1
            
            
            
            
            
            
            
            
            
            
        #for insans in range(17*80, 14*80, -5):
        #    screen.blit(sans, (insans, 540))
            
        
        
        for event in pygame.event.get():  
            
            
    #Kilépő (nem bír magától kilépni Bruh)        
            
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
                
                
        #tick és update        
        #pygame.display.update()
        clock.tick(60)
        
menu()
snowdin()