import sys
import pygame
from pygame import Surface

pygame.init()

size = (1200, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pygame图形绘制")

YELLOW = 255, 255, 0
ORANGE = 255, 165, 0
BLUE = 0, 0, 255
GREEN = 0, 255, 0
RED = 255, 0, 0
WHITE = 255, 255, 255

LINEN = 150, 150, 150


surface = Surface(size)
# surface.set_colorkey((0, 0, 0))
# surface.set_alpha(200)

color_dict = {'u': YELLOW, 'd': WHITE, 'r': BLUE, 'l': GREEN, 'f': ORANGE, 'b': RED}
pos = (1, 1, 1)
color = ('u', 'b', 'r')

# 1.角块坐标转换，




# 绘制矩形
# r1rect = pygame.draw.rect(screen, GOLD, (100,100,200,100), 5)
# r2rect = pygame.draw.rect(screen, RED, (210,210,200,100), 0)

# p4poly = pygame.draw.polygon(surface, GREEN, [(100, 200), (150, 150), (150, 250), (100, 300)], 0)
# p5poly = pygame.draw.polygon(surface, WHITE, [(100, 300), (200, 300), (250, 250), (150, 250)], 0)
# p6poly = pygame.draw.polygon(surface, RED, [(150, 150), (150, 250), (250, 250), (250, 150)], 0)

# p4poly = pygame.draw.polygon(surface, LINEN, [(600, 200), (490, 190), (490, 340), (600, 350)], 0)  #
# p5poly = pygame.draw.polygon(surface, LINEN, [(600, 200), (200, 300), (250, 250), (150, 250)], 0)
# p6poly = pygame.draw.polygon(surface, LINEN, [(150, 150), (150, 250), (250, 250), (250, 150)], 0)

# p0poly = pygame.draw.polygon(surface, LINEN, [(600, 200), (450, 150), (600, 100), (750, 150)], 0)
# p1poly = pygame.draw.polygon(surface, LINEN, [(600, 200), (450, 150), (450, 350), (600, 400)], 0)
# p2poly = pygame.draw.polygon(surface, LINEN, [(600, 200), (750, 150), (750, 350), (600, 400)], 0)
#
# p0poly = pygame.draw.polygon(surface, YELLOW, [(600, 195), (465, 150), (600, 105), (735, 150)], 0)
# p1poly = pygame.draw.polygon(surface, ORANGE, [(592.5, 210), (457.5, 162.5), (457.5, 342.5), (592.5, 390)], 0)
# p2poly = pygame.draw.polygon(surface, BLUE, [(607.5, 210), (742.5, 162.5), (742.5, 342.5), (607.5, 390)], 0)

color_order = list(color_dict.values())
import test2
dr = test2.DrawRubikS(1)
all = dr.add_all_cube() # 如何从生成器指定位置获取值，前面的丢弃不用
count = 0
max = 26
for xx in all:
    count += 1
    if count > max:
        break

    i = 0
    for x in xx:
        pygame.draw.polygon(surface, LINEN, x, 0)
        i+=1




while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.blit(surface, (0, 0))
    pygame.display.update()
