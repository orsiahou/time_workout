import pygame
import const
import random
from tabulate import tabulate

def grass_screen():
    # FPS = 60
    # clock = pygame.time.Clock()
    screen = pygame.display.set_mode(const.size)
    pygame.display.set_caption("The Flag Game")
    screen.fill(const.BACKGROUND_COLOR)
    grass_img = pygame.image.load('grassnew.png').convert()
    grass_img.set_colorkey((0, 0, 0))
    input_grass(index_to_px(random_grass()), screen, grass_img)
    pygame.display.flip()
    finish = False
    while not finish:
        # clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finish = True


def random_grass():
    list = []
    small_list = []
    for i in range(20):
        x = random.randint(0,47)
        y = random.randint(0,23)
        small_list.append(x)
        small_list.append(y)
        list.append(small_list.copy())
        small_list.clear()
    return list

def index_to_px(list):
    list_px = []
    small_list_px =[]
    for i in range(20):
        x = list[i][0]*20
        small_list_px.append(x)
        y = list[i][1]*24
        small_list_px.append(y)
        list_px.append(small_list_px.copy())
        small_list_px.clear()
    return list_px

def input_grass(list, screen, grass_img):
    for i in range(20):
        screen.blit(grass_img, [list[i][0],list[i][1]])
        pygame.display.flip()

def normal_screen():
    FPS = 60
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode(const.size)
    pygame.display.set_caption("The Flag Game")
    finish = False
    while not finish:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finish = True
        screen.fill(const.BACKGROUND_COLOR)
        pygame.display.flip()


def print_table(screen):
    for row in range(26):
        pygame.draw.lines(screen, const.BACKGROUND_COLOR, True, [(0, 24*row), (1000, 24*row)])
    for cal in range(50):
        pygame.draw.aalines(screen, const.BACKGROUND_COLOR, True, [(20*cal, 0), (20*cal, 600)])
    pygame.display.flip()

def grass_screen2():
    # FPS = 60
    # clock = pygame.time.Clock()
    screen = pygame.display.set_mode(const.size)
    pygame.display.set_caption("The Flag Game")
    screen.fill(const.BACKGROUND_COLOR)
    player_img = pygame.image.load('player.png').convert()
    player_img.set_colorkey((0, 0, 0))
    screen.blit(player_img, (0,0))
    grass_img = pygame.image.load('grassnew.png').convert()
    grass_img.set_colorkey((0, 0, 0))
    input_grass(index_to_px(random_grass()), screen, grass_img)
    flag_img = pygame.image.load('flag.png').convert()
    flag_img.set_colorkey((0, 0, 0))
    screen.blit(flag_img, (920, 528))
    pygame.display.flip()
    finish = False
    while not finish:
        # clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finish = True



def grid_screen():
    screen = pygame.display.set_mode(const.size)
    pygame.display.set_caption("The Flag Game")
    screen.fill((0,0,0))
    print_table(screen)
    bomb_img = pygame.image.load('Bomb.png').convert()
    bomb_img.set_colorkey((0, 0, 0))
    input_grass(index_to_px(random_grass()), screen, bomb_img)
    player2_img = pygame.image.load('player2.png').convert()
    player2_img.set_colorkey((0, 0, 0))
    screen.blit(player2_img, (0, 0))
    pygame.display.flip()

    finish = False
    while not finish:
        # clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finish = True

grid_screen()




