import pygame
from shooter_3d.settings import *
from shooter_3d.player import Player
import math
from shooter_3d.map import *

pygame.init()
sc = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
player = Player()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    player.movement()
    sc.fill(BLACK)

    pygame.draw.circle(sc, GREEN, player.pos, 12)
    pygame.draw.line(sc, GREEN, player.pos,
                     (int(player.x + WIDTH * math.cos(player.angle)),
                      int(player.y + WIDTH * math.sin(player.angle))))
    for x, y in world_map:
        pygame.draw.rect(sc, DARKGRAY, (x, y, TILE, TILE),2)
    pygame.display.flip()
    clock.tick(FPS)
