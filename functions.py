import pygame
import os
import time
import random


pygame.init()
pygame.mixer.init()

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

pygame.mixer.init()

WIDTH, HEIGHT = 1280, 720
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))


MUSIC_DIR = "musics"
MUSICS = [file for file in os.listdir(MUSIC_DIR) if file.endswith(".mp3")]
CLICK_SOUND = pygame.mixer.Sound(os.path.join("sounds", "click-button.mp3"))


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