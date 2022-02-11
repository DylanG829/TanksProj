import pygame
import random

pygame.init()

game_display = pygame.display.set_mode((800, 600))

pygame.display.set_caption('Tanks - Brought To You By Dylan Goldberg')


clock = pygame.time.Clock()

#tanks dementions
tankWidth = 45
tankHeight = 25

turretWidth = 6
wheelWidth = 5

ground_height = 30

#fonts
font1 = pygame.font.SysFont("Yu Mincho Demibold", 20)
font2 = pygame.font.SysFont("lucidaconsole", 25)
font3 = pygame.font.SysFont("comicsansms", 50)
font4 = pygame.font.SysFont("Yu Mincho Demibold", 85)

#
