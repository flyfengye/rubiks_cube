from math import pi

import sys
import pygame
from pygame import Surface

pygame.init()

screen = pygame.display.set_mode((600, 400))
# screen.fill((255, 255, 255))

pygame.display.set_caption("Pygame图形绘制")

YELLOW = 255, 255, 0
ORANGE = 255, 165, 0
BLUE = 0, 0, 255
GREEN = 0, 255, 0
RED = 255, 0, 0
WHITE = 255, 255, 255

LINEN = 250, 240, 230

# size = (150, 150)
size = (600, 400)
surface = Surface(size)
surface.set_colorkey((0, 0, 0))
# surface.set_alpha(200)


# 绘制矩形
# r1rect = pygame.draw.rect(screen, GOLD, (100,100,200,100), 5)
# r2rect = pygame.draw.rect(screen, RED, (210,210,200,100), 0)

# p4poly = pygame.draw.polygon(surface, GREEN, [(100, 200), (150, 150), (150, 250), (100, 300)], 0)
# p5poly = pygame.draw.polygon(surface, WHITE, [(100, 300), (200, 300), (250, 250), (150, 250)], 0)
# p6poly = pygame.draw.polygon(surface, RED, [(150, 150), (150, 250), (250, 250), (250, 150)], 0)
# import time
# time.sleep(3)
p4poly = pygame.draw.polygon(surface, LINEN, [(100, 200), (150, 150), (150, 250), (100, 300)], 0)
p5poly = pygame.draw.polygon(surface, LINEN, [(100, 300), (200, 300), (250, 250), (150, 250)], 0)
p6poly = pygame.draw.polygon(surface, LINEN, [(150, 150), (150, 250), (250, 250), (250, 150)], 0)
p0poly = pygame.draw.polygon(surface, YELLOW, [(100, 200), (150, 150), (250, 150), (200, 200)], 0)
p1poly = pygame.draw.polygon(surface, ORANGE, [(100, 200), (100, 300), (200, 300), (200, 200)], 0)
p2poly = pygame.draw.polygon(surface, BLUE, [(200, 200), (200, 300), (250, 250), (250, 150)], 0)
screen.blit(surface, (0, 0))
# screen.blit(white_sfc, (0, 0))
# screen.blit(red_sfc, (0, 0))
# screen.blit(yellow_sfc, (0, 0))
# screen.blit(orange_sfc, (0, 0))
# screen.blit(blue_sfc, (0, 0))


# 绘制笑脸
# e1rect = pygame.draw.ellipse(screen, GREEN, (50,50,500,300), 3)
# c1rect = pygame.draw.circle(screen, GOLD, (200,180), 30, 5)
# c2rect = pygame.draw.circle(screen, GOLD, (400,180), 30)
# r1rect = pygame.draw.rect(screen, RED, (170,130, 60, 10), 3)
# r2rect = pygame.draw.rect(screen, RED, (370,130, 60, 10))
# plist = [(295,170), (285,250), (260,280), (340,280), (315,250), (305,170)]
# l1rect = pygame.draw.lines(screen, GOLD, True, plist, 2)
# al1rect = pygame.draw.aalines(screen, GOLD, True, plist, 2)
# a1rect = pygame.draw.arc(screen, RED, (200,220,200,100), 1.4*pi, 1.9*pi, 3)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    pygame.display.update()
