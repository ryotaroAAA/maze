import copy
import cython
from dataclasses import *
import logging
import logging.config
import numpy as np
from pathlib import Path
import sys
import time
import traceback
from typing import *

from hexdump import hexdump
from pprint import *
from print_color import print
from tabulate import tabulate
import yaml
from enum import auto, Enum

import argparse
import pygame

class ObjAttr(Enum):
    WALL = auto() 
    AISLE = auto() 
    GOAL = auto() 

BLACK = (0, 0, 0)
RED = (255, 0, 0)
WHITE = (255,255,255)
BROWN = (115, 66, 41)
ORANGE = (233,168, 38)

ME_COLOR = RED
AISLE_COLOR = WHITE
WALL_COLOR = BLACK

SCREEN = (210, 210)
TILE_SIZE = (10, 10)
TILE = (SCREEN[0]//TILE_SIZE[0], SCREEN[1]//TILE_SIZE[1])
maze = []

x = 10
y = 10

def make_maze():
    global maze
    maze = []
    for j in range(TILE[1]):
        row = []
        for i in range(TILE[0]):
            # outer wall
            if (i == 0 or j == 0 or
                    i == TILE[0]-1 or j == TILE[1]-1):
                row.append(ObjAttr.WALL)
            elif (i%2 == 0 and j%2 == 0):
                row.append(ObjAttr.WALL)
            else:
                row.append(ObjAttr.AISLE)
                
        print([1 if s == ObjAttr.WALL else 0 for s in row])
        maze.append(row)
        
def is_not_collision(x, y):
    global maze
    t_x = x // TILE_SIZE[0]
    t_y = y // TILE_SIZE[1]
    if 0 <= t_x < TILE[0] and 0 <= t_y < TILE[1]:
        if maze[t_y][t_x] == ObjAttr.AISLE:
            return True
    return False

def run():
    global maze, x, y
    # assert((x % 10 == 0) and (y % 10 == 0), "screen size error")

    print(SCREEN)
    pygame.init()
    screen = pygame.display.set_mode(SCREEN)
    myclock = pygame.time.Clock()
    pygame.key.set_repeat(1000, 1000)
    make_maze()

    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                break

        press = pygame.key.get_pressed()
        if (press[pygame.K_ESCAPE]):
            break

        if (press[pygame.K_LEFT] and is_not_collision(x - TILE_SIZE[0], y)):
            x -= TILE_SIZE[0]

        if (press[pygame.K_RIGHT] and is_not_collision(x + TILE_SIZE[1], y)):
            x += TILE_SIZE[0]
        
        if (press[pygame.K_UP] and is_not_collision(x, y - TILE_SIZE[1])):
            y -= TILE_SIZE[1]

        if (press[pygame.K_DOWN] and is_not_collision(x, y + TILE_SIZE[1])):
            y += TILE_SIZE[1]

        # print(f"[FPS] {}")
        # wall
        for j in range(TILE[1]):
            for i in range(TILE[0]):
                if maze[j][i] == ObjAttr.WALL:
                    wall = pygame.Rect(i * TILE_SIZE[0], j * TILE_SIZE[1],
                        TILE_SIZE[0], TILE_SIZE[1])
                    pygame.draw.rect(screen, WALL_COLOR, wall)
                elif maze[j][i] == ObjAttr.AISLE:
                    aisle = pygame.Rect(i * TILE_SIZE[0], j * TILE_SIZE[1],
                        TILE_SIZE[0], TILE_SIZE[1])
                    pygame.draw.rect(screen, AISLE_COLOR, aisle)

        me = pygame.Rect(x, y, 10, 10)
        pygame.draw.rect(screen, ME_COLOR, me)
        pygame.display.flip()
        myclock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    # parser = argparse.ArgumentParser()
    # parser.add_argument("-l", "--loop", type=int, default=-1, help="loop")
    # parser.add_argument("-r", "--rom", default="", help="rom")
    # parser.add_argument("-s", "--stop", action="store_true", help="stop after num of loop run")
    # args = parser.parse_args()
    # print(vars(args), tag="args", tag_color="green", color="white")

    run()