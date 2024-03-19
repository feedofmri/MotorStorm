import pygame
import os
import time
import random

pygame.init()

HOME_PAGE_1 = pygame.transform.scale(pygame.image.load(os.path.join("images", "home.png")), (1280, 720))
HOME_PAGE_2 = pygame.transform.scale(pygame.image.load(os.path.join("images", "home_off.png")), (1280, 720))
    
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

CAR_1 = pygame.transform.scale(pygame.image.load(os.path.join("images", "car1.png")), (25, 48))
CAR_2 = pygame.transform.scale(pygame.image.load(os.path.join("images", "car2.png")), (25, 48))
CAR_3 = pygame.transform.scale(pygame.image.load(os.path.join("images", "car3.png")), (25, 48))
CAR_4 = pygame.transform.scale(pygame.image.load(os.path.join("images", "car4.png")), (25, 48))

WIN = pygame.transform.scale(pygame.image.load(os.path.join("images", "win.png")), (1280, 720))
WIN_1 = pygame.transform.scale(pygame.image.load(os.path.join("images", "win1.png")), (1280, 720))
WIN_2 = pygame.transform.scale(pygame.image.load(os.path.join("images", "win2.png")), (1280, 720))
WIN_3 = pygame.transform.scale(pygame.image.load(os.path.join("images", "win3.png")), (1280, 720))

FAILED = pygame.transform.scale(pygame.image.load(os.path.join("images", "failed.png")), (1280, 720))
FAILED_1 = pygame.transform.scale(pygame.image.load(os.path.join("images", "failed1.png")), (1280, 720))
MUSIC_DIR = "musics"

MUSICS = [file for file in os.listdir(MUSIC_DIR) if file.endswith(".mp3")]
CLICK_SOUND = pygame.mixer.Sound(os.path.join("sounds", "click-button.mp3"))

pygame.mixer.init()

WIDTH, HEIGHT = 1280, 720
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("MotorStorm")



def play_music():
    MUSIC = random.choice(MUSICS)
    pygame.mixer.music.load(os.path.join(MUSIC_DIR, MUSIC))
    pygame.mixer.music.play()
        
        
def draw_home(music_con):
    if music_con == True:
        SCREEN.blit(HOME_PAGE_1, (0, 0))
        pygame.display.update()
    else:
        SCREEN.blit(HOME_PAGE_2, (0, 0))
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
       

def draw_result(rank):
    
    if rank == 1:
        SCREEN.blit(WIN, (0, 0))
        pygame.display.update()
        pygame.time.delay(1500)
        SCREEN.blit(WIN_1, (0, 0))
        pygame.display.update()
        rank_page = True
        
    elif rank == 2:
        SCREEN.blit(WIN, (0, 0))
        pygame.display.update()
        pygame.time.delay(1500)
        SCREEN.blit(WIN_2, (0, 0))
        pygame.display.update()
        rank_page = True
        
    elif rank == 3:
        SCREEN.blit(WIN, (0, 0))
        pygame.display.update()
        pygame.time.delay(1500)
        SCREEN.blit(WIN_3, (0, 0))
        pygame.display.update()
        rank_page = True
        
    elif rank >= 4:
        SCREEN.blit(FAILED, (0, 0))
        pygame.display.update()
        pygame.time.delay(1500)
        SCREEN.blit(FAILED_1, (0, 0))
        pygame.display.update()
        rank_page = True
    
    
import pygame

def main():

    run = True
    
    music_con = True
    
    home_page = True
    play_page = False
    map_page = False
    car_page = False
    quit_btn = False
    
    play_page_1 = True
    play_page_2 = False
    play_page_3 = False
    play_page_4 = False
    
    map_page_1 = True
    map_page_2 = False
    map_page_3 = False
    map_page_4 = False
    
    car_page_1 = True
    car_page_2 = False
    car_page_3 = False
    car_page_4 = False
    
    rank_page = False
    
    car1 = True
    car2 = False
    car3 = False
    car4 = False
    
    rank = 0
    
    play_music()
        
    while run:   
        
        if home_page == True and play_page == False and map_page == False and car_page == False:
            draw_home(music_con)
            
        elif home_page == False and play_page == True and map_page == False and car_page == False:
            draw_play(play_page, play_page_1, play_page_2, play_page_3, play_page_4)
            
        elif home_page == False and play_page == False and map_page == True and car_page == False:
            draw_map(map_page, map_page_1, map_page_2, map_page_3, map_page_4)
        
        elif home_page == False and play_page == False and map_page == False and car_page == True:
            draw_car(car_page, car_page_1, car_page_2, car_page_3, car_page_4)
        
        elif home_page == False and play_page == False and map_page == False and car_page == False and quit_btn == True:
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
                    if (pos[0] > 160 and pos[0] < 635 and pos[1] > 625 and pos[1] < 670):
                        CLICK_SOUND.play()
                        if music_con == True:
                            play_music()
                        
                    elif (pos[0] > 60 and pos[0] < 680 and pos[1] > 625 and pos[1] < 670):
                        CLICK_SOUND.play()
                        if music_con == True:
                            pygame.mixer.music.pause()
                            music_con = False
                        else:
                            pygame.mixer.music.unpause()
                            music_con = True
                     
                    elif (pos[0] > 530 and pos[0] < 750 and pos[1] > 260 and pos[1] < 330):
                        CLICK_SOUND.play()
                        home_page = False
                        play_page = True
                        map_page = False
                        car_page = False
                        quit_btn = False
                        
                    elif (pos[0] > 530 and pos[0] < 750 and pos[1] > 365 and pos[1] < 440):
                        CLICK_SOUND.play()
                        home_page = False
                        play_page = False
                        map_page = True
                        car_page = False
                        quit_btn = False
                    
                    elif (pos[0] > 530 and pos[0] < 750 and pos[1] > 470 and pos[1] < 540):
                        CLICK_SOUND.play()
                        home_page = False
                        play_page = False
                        map_page = False
                        car_page = True
                        quit_btn = False
                        
                    elif (pos[0] > 530 and pos[0] < 750 and pos[1] > 575 and pos[1] < 640):
                        CLICK_SOUND.play()
                        home_page = False
                        play_page = False
                        map_page = False
                        car_page = False
                        quit_btn = True
                
                elif (play_page == True):
                    if (pos[0] > 50 and pos[0] < 230 and pos[1] > 50 and pos[1] < 110):
                        CLICK_SOUND.play()
                        home_page = True
                        play_page = False
                
                elif (map_page == True):
                    if (pos[0] > 860 and pos[0] < 1100 and pos[1] > 400 and pos[1] < 465):
                        CLICK_SOUND.play()
                        home_page = True
                        map_page = False
                    
                    elif (pos[0] > 860 and pos[0] < 1100 and pos[1] > 260 and pos[1] < 335):
                        CLICK_SOUND.play()
                        if map_page_1 == True:
                            play_page_1 = True
                            play_page_2 = False
                            play_page_3 = False
                            play_page_4 = False
                        elif map_page_2 == True:
                            play_page_1 = False
                            play_page_2 = True
                            play_page_3 = False
                            play_page_4 = False
                        elif map_page_3 == True:
                            play_page_1 = False
                            play_page_2 = False
                            play_page_3 = True
                            play_page_4 = False
                        elif map_page_4 == True:
                            play_page_1 = False
                            play_page_2 = False
                            play_page_3 = False
                            play_page_4 = True
                        home_page = True
                        map_page = False
                        
                    elif (pos[0] > 90 and pos[0] < 390 and pos[1] > 335 and pos[1] < 390):
                        CLICK_SOUND.play()
                        if map_page_1 == True:
                            map_page_1 = False
                            map_page_4 = True
                        elif map_page_2 == True:
                            map_page_2 = False
                            map_page_1 = True
                        elif map_page_3 == True:
                            map_page_3 = False
                            map_page_2 = True
                        elif map_page_4 == True:
                            map_page_4 = False
                            map_page_3 = True
                    
                    elif (pos[0] > 645 and pos[0] < 695 and pos[1] > 335 and pos[1] < 390):
                        CLICK_SOUND.play()
                        if map_page_1 == True:
                            map_page_1 = False
                            map_page_2 = True
                        elif map_page_2 == True:
                            map_page_2 = False
                            map_page_3 = True
                        elif map_page_3 == True:
                            map_page_3 = False
                            map_page_4 = True
                        elif map_page_4 == True:
                            map_page_4 = False
                            map_page_1 = True               
                    
                elif (car_page == True):
                    if (pos[0] > 860 and pos[0] < 1100 and pos[1] > 400 and pos[1] < 465):
                        CLICK_SOUND.play()
                        home_page = True
                        car_page = False
                    
                    elif (pos[0] > 860 and pos[0] < 1100 and pos[1] > 260 and pos[1] < 335):
                        CLICK_SOUND.play()
                        if car_page_1 == True:
                            car1 = True
                            car2 = False
                            car3 = False
                            car4 = False
                        elif car_page_2 == True:
                            car1 = False
                            car2 = True
                            car3 = False
                            car4 = False
                        elif car_page_3 == True:
                            car1 = False
                            car2 = False
                            car3 = True
                            car4 = False
                        elif car_page_4 == True:
                            car1 = False
                            car2 = False
                            car3 = False
                            car4 = True
                        home_page = True
                        car_page = False
                        
                    elif (pos[0] > 90 and pos[0] < 390 and pos[1] > 335 and pos[1] < 390):
                        CLICK_SOUND.play()
                        if car_page_1 == True:
                            car_page_1 = False
                            car_page_4 = True
                        elif car_page_2 == True:
                            car_page_2 = False
                            car_page_1 = True
                        elif car_page_3 == True:
                            car_page_3 = False
                            car_page_2 = True
                        elif car_page_4 == True:
                            car_page_4 = False
                            car_page_3 = True
                    
                    elif (pos[0] > 645 and pos[0] < 695 and pos[1] > 335 and pos[1] < 390):
                        CLICK_SOUND.play()
                        if car_page_1 == True:
                            car_page_1 = False
                            car_page_2 = True
                        elif car_page_2 == True:
                            car_page_2 = False
                            car_page_3 = True
                        elif car_page_3 == True:
                            car_page_3 = False
                            car_page_4 = True
                        elif car_page_4 == True:
                            car_page_4 = False
                            car_page_1 = True
    main()
    
if __name__ == "__main__":
    main()