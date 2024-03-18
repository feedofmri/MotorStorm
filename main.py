import pygame
import os

HOME_PAGE = pygame.transform.scale(pygame.image.load(os.path.join("images", "home.png")), (1280, 720))

PLAY_PAGE_1 = pygame.transform.scale(pygame.image.load(os.path.join("images", "map1.png")), (1280, 720))
PLAY_PAGE_2 = pygame.transform.scale(pygame.image.load(os.path.join("images", "map2.png")), (1280, 720))
PLAY_PAGE_3 = pygame.transform.scale(pygame.image.load(os.path.join("images", "map3.png")), (1280, 720))
PLAY_PAGE_4 = pygame.transform.scale(pygame.image.load(os.path.join("images", "map4.png")), (1280, 720))

MAP_PAGE_1 = pygame.transform.scale(pygame.image.load(os.path.join("images", "map_menu1.png")), (1280, 720))
MAP_PAGE_2 = pygame.transform.scale(pygame.image.load(os.path.join("images", "map_menu2.png")), (1280, 720))
MAP_PAGE_3 = pygame.transform.scale(pygame.image.load(os.path.join("images", "map_menu3.png")), (1280, 720))
MAP_PAGE_4 = pygame.transform.scale(pygame.image.load(os.path.join("images", "map_menu4.png")), (1280, 720))

CAR_PAGE_1 = pygame.transform.scale(pygame.image.load(os.path.join("images", "car_menu1.png")), (1280, 720))
CAR_PAGE_2 = pygame.transform.scale(pygame.image.load(os.path.join("images", "car_menu2.png")), (1280, 720))
CAR_PAGE_3 = pygame.transform.scale(pygame.image.load(os.path.join("images", "car_menu3.png")), (1280, 720))
CAR_PAGE_4 = pygame.transform.scale(pygame.image.load(os.path.join("images", "car_menu4.png")), (1280, 720))


WIDTH, HEIGHT = 1280, 720
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("MotorStorm")

def draw_home():
    SCREEN.blit(HOME_PAGE, (0, 0))
    pygame.display.update()
    

def draw_play(play_page, play_page_1, play_page_2, play_page_3, play_page_4):
        
        if (play_page == True and play_page_1 == True and play_page_2 == False and play_page_3 == False and play_page_4 == False):
            SCREEN.blit(PLAY_PAGE_1, (0, 0))
            pygame.display.update()
            
        elif (play_page == True and play_page_1 == False and play_page_2 == True and play_page_3 == False and play_page_4 == False):
            SCREEN.blit(PLAY_PAGE_2, (0, 0))
            pygame.display.update()
        
        elif (play_page == True and play_page_1 == False and play_page_2 == False and play_page_3 == True and play_page_4 == False):
            SCREEN.blit(PLAY_PAGE_3, (0, 0))
            pygame.display.update()
            
        elif (play_page == True and play_page_1 == False and play_page_2 == False and play_page_3 == False and play_page_4 == True):
            SCREEN.blit(PLAY_PAGE_4, (0, 0))
            pygame.display.update()
            

    
def draw_map(map_page, map_page_1, map_page_2, map_page_3, map_page_4):
    
    if (map_page == True and map_page_1 == True and map_page_2 == False and map_page_3 == False and map_page_4 == False):
        SCREEN.blit(MAP_PAGE_1, (0, 0))
        pygame.display.update()
        
    elif (map_page == True and map_page_1 == False and map_page_2 == True and map_page_3 == False and map_page_4 == False):
        SCREEN.blit(MAP_PAGE_2, (0, 0))
        pygame.display.update()
    
    elif (map_page == True and map_page_1 == False and map_page_2 == False and map_page_3 == True and map_page_4 == False):
        SCREEN.blit(MAP_PAGE_3, (0, 0))
        pygame.display.update()
        
    elif (map_page == True and map_page_1 == False and map_page_2 == False and map_page_3 == False and map_page_4 == True):
        SCREEN.blit(MAP_PAGE_4, (0, 0))
        pygame.display.update()
    

def draw_car(car_page, car_page_1, car_page_2, car_page_3, car_page_4):
    
    if (car_page == True and car_page_1 == True and car_page_2 == False and car_page_3 == False and car_page_4 == False):
        SCREEN.blit(CAR_PAGE_1, (0, 0))
        pygame.display.update()
        
    elif (car_page == True and car_page_1 == False and car_page_2 == True and car_page_3 == False and car_page_4 == False):
        SCREEN.blit(CAR_PAGE_2, (0, 0))
        pygame.display.update()
    
    elif (car_page == True and car_page_1 == False and car_page_2 == False and car_page_3 == True and car_page_4 == False):
        SCREEN.blit(CAR_PAGE_3, (0, 0))
        pygame.display.update()
        
    elif (car_page == True and car_page_1 == False and car_page_2 == False and car_page_3 == False and car_page_4 == True):
        SCREEN.blit(CAR_PAGE_4, (0, 0))
        pygame.display.update()   
       

    
def main():
    
    run = True
    
    home_page = True
    play_page = False
    map_page = False
    car_page = False
    quit_btn = False
    
    play_page_1 = False
    play_page_2 = False
    play_page_3 = False
    play_page_4 = False
    
    map_page_1 = False
    map_page_2 = False
    map_page_3 = False
    map_page_4 = False
    
    car_page_1 = False
    car_page_2 = False
    car_page_3 = False
    car_page_4 = False
    
    while run:
        
        
        if (home_page == True and play_page == False and map_page == False and car_page == False):
            draw_home()
            
        elif (home_page == False and play_page == True and map_page == False and car_page == False):
            play_page_1 = True
            draw_play(play_page, play_page_1, play_page_2, play_page_3, play_page_4)
            
        elif (home_page == False and play_page == False and map_page == True and car_page == False):
            map_page_1 = True
            draw_map(map_page, map_page_1, map_page_2, map_page_3, map_page_4)
        
        elif (home_page == False and play_page == False and map_page == False and car_page == True):
            car_page_1 = True
            draw_car(car_page, car_page_1, car_page_2, car_page_3, car_page_4)
        
        elif (home_page == False and play_page == False and map_page == False and car_page == False and quit_btn == True):
            run = False
            pygame.quit()
            quit()
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()
                
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                print(pos)
                
                if(home_page == True):
                    if (pos[0] > 530 and pos[0] < 750 and pos[1] > 260 and pos[1] < 330):
                        home_page = False
                        play_page = True
                        map_page = False
                        car_page = False
                        quit_btn = False
                        
                    elif (pos[0] > 530 and pos[0] < 750 and pos[1] > 365 and pos[1] < 440):
                        home_page = False
                        play_page = False
                        map_page = True
                        car_page = False
                        quit_btn = False
                    
                    elif (pos[0] > 530 and pos[0] < 750 and pos[1] > 470 and pos[1] < 540):
                        home_page = False
                        play_page = False
                        map_page = False
                        car_page = True
                        quit_btn = False
                        
                    elif (pos[0] > 530 and pos[0] < 750 and pos[1] > 575 and pos[1] < 640):
                        home_page = False
                        play_page = False
                        map_page = False
                        car_page = False
                        quit_btn = True
                
                elif (play_page == True):
                    if (pos[0] > 50 and pos[0] < 230 and pos[1] > 50 and pos[1] < 110):
                        home_page = True
                        play_page = False
                
                elif (map_page == True):
                    if (pos[0] > 860 and pos[0] < 1100 and pos[1] > 400 and pos[1] < 465):
                        home_page = True
                        map_page = False
                    
                    elif (pos[0] > 860 and pos[0] < 1100 and pos[1] > 260 and pos[1] < 335):
                        play_page = True
                        map_page = False
                        
                    elif (pos[0] > 90 and pos[0] < 390 and pos[1] > 335 and pos[1] < 390):
                        print("map left")
                    
                    elif (pos[0] > 645 and pos[0] < 695 and pos[1] > 335 and pos[1] < 390):
                        print("map right")
                    
                elif (car_page == True):
                    if (pos[0] > 860 and pos[0] < 1100 and pos[1] > 400 and pos[1] < 465):
                        home_page = True
                        car_page = False
                    
                    elif (pos[0] > 860 and pos[0] < 1100 and pos[1] > 260 and pos[1] < 335):
                        play_page = True
                        car_page = False
                        
                    elif (pos[0] > 90 and pos[0] < 390 and pos[1] > 335 and pos[1] < 390):
                        print("car left")
                    
                    elif (pos[0] > 645 and pos[0] < 695 and pos[1] > 335 and pos[1] < 390):
                        print("car right")
    main()
    
if __name__ == "__main__":
    main()