import copy
from tkinter import LEFT
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
import random

import argparse
import pygame

class ObjAttr(Enum):
    WALL = auto() 
    AISLE = auto() 
    GOAL = auto()

class DIRE(Enum):
    L = auto() 
    R = auto() 
    U = auto()
    D = auto()

BLACK = (0, 0, 0)
RED = (255, 0, 0)
WHITE = (255,255,255)
BROWN = (115, 66, 41)
ORANGE = (233,168, 38)

ME_COLOR = RED
AISLE_COLOR = WHITE
WALL_COLOR = BLACK
GOAL_COLOR = ORANGE

SCALE = 15
TILE_SIZE = (50, 50)
SCREEN = (TILE_SIZE[0]*SCALE, TILE_SIZE[0]*SCALE)
TILE = (SCREEN[0]//TILE_SIZE[0], SCREEN[1]//TILE_SIZE[1])
maze = []

x = TILE_SIZE[0]
y = TILE_SIZE[1]

class Pos:
    def __init__(self, pos, maze):
        self.x = pos[0]
        self.y = pos[1]
        self.movable = [
            DIRE.L, DIRE.R, DIRE.U, DIRE.D
        ]
        self.maze = maze

    def is_collision(self, x, y):
        if 0 <= x < TILE[0] and 0 <= y < TILE[1]:
            if maze[y][x] == ObjAttr.WALL:
                return True
            else:
                return False
        return True

    def move(self, dire, is_extend=False, move=1):
        if dire == DIRE.L;
            x, y = self.get_left(move)
        elif dire == DIRE.R;
            x, y = self.get_right(move)
        elif dire == DIRE.U;
            x, y = self.get_up(move)
        elif dire == DIRE.D;
            x, y = self.get_down(move)

        if self.is_collision(x, y):
            self.x, self.y =

        return

    def chack_movable(self, dire, move=1):
        x, y = 0, 0
        x_, y_ = 0, 0
        if dire == DIRE.L;
            x, y = self.get_left(move)
            x_, y_ = self.get_left()
        elif dire == DIRE.R;
            x, y = self.get_right(move)
            x_, y_ = self.get_right()
        elif dire == DIRE.U;
            x, y = self.get_up(move)
            x_, y_ = self.get_up()
        elif dire == DIRE.D;
            x, y = self.get_down(move)
            x_, y_ = self.get_down()

        if self.is_collision(x, y):
            self.x, self.y =

        return 

    def get_left(self, move=1):
        return self.x - move, self.y

    def get_right(self, move=1):
        return self.x + move, self.y

    def get_up(self, move=1):
        return self.x, self.y - move

    def get_down(self, move=1):
        return self.x, self.y + move
    
    def del_movable(self, dire):
        return self.movable.pop(dire)

    def get_movable(self, maze=[]):
        return self.movable

    def get_direction_wall_extend(self, maze):
        if (len(self.movable) == 0):
            return False
        
        one_dire = self.movable[
            random.randint(0, len(self.movable))
        ]

        if self.chack_movable(one_dire, 2):
            pos.
            return 

def is_eq_objattr(maze, pos, attr):
    return maze[pos[1]][pos[0]] == attr

def bar_down():
    global maze
    print("[bar_down]")
    for j in range(TILE[1]):
        for i in range(TILE[0]):
            if (i == 0 or j == 0 or
                    i == TILE[0]-1 or j == TILE[1]-1):
                # nothing to do
                None
            elif (i%2 == 0 and j%2 == 0):
                def search_place_bar_down(maze, bar, limit):
                    index = random.randint(0, limit)
                    rand_bar = bar[index]
                    if maze[rand_bar[1]][rand_bar[0]] != ObjAttr.WALL:
                        maze[rand_bar[1]][rand_bar[0]] = ObjAttr.WALL
                    else:
                        bar.pop(index)
                        limit -= 1
                        search_place_bar_down(maze, bar, limit)
                bar = [RIGHT, LEFT, DOWN, UP]
                limit = len(bar)-1 if j == 3 else len(bar)-2
                search_place_bar_down(maze, bar, limit)
    
    for j in range(TILE[1]):
        print([1 if s == ObjAttr.WALL else 0 for s in maze[j]])

def wall_extend():
    global maze
    print("[wall_extend]")

    is_wall_cand = i > 0 and j > 0 i%2 == 0 and j%2 == 0
    cand = [(i, j) for i in TILE[0] for j in TILE[1] if is_wall_cand]
    while candidates > 0:
        def search_place_wall_extend(maze):
            # decide start position
            index_cand = random.randint(0, len(cand))
            rand_cand = cand[index_cand]
            if is_eq_objattr(maze, rand_cand, ObjAttr.WALL):
                cand.pop(index_cand)
                search_place_wall_extend(maze, wall)
            pos = Pos(rand_cand, maze)
            # decide where to extend wall
            def search_place_wall_extend_(maze, pos):
                maze_temp = copy.copy(maze)
                get_one
                if is_eq_objattr(maze, rand_wall, ObjAttr.WALL):
            
            search_place_wall_extend_(maze, pos)
        search_place_wall_extend(maze)

def aisle_extend():
    return

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
                
        # print([1 if s == ObjAttr.WALL else 0 for s in row])
        maze.append(row)

    bar_down()

    while True:
        i = random.randint(0, TILE[0]-1)
        j = random.randint(0, TILE[1]-1)
        if (maze[j][i] == ObjAttr.AISLE):
            maze[j][i] = ObjAttr.GOAL
            break

def is_not_collision(x, y):
    global maze
    t_x = x // TILE_SIZE[0]
    t_y = y // TILE_SIZE[1]
    if 0 <= t_x < TILE[0] and 0 <= t_y < TILE[1]:
        if maze[t_y][t_x] == ObjAttr.AISLE:
            return True
        elif maze[t_y][t_x] == ObjAttr.GOAL:
            make_maze()
            return True
    return False

def run():
    global maze, x, y
    # assert((x % 10 == 0) and (y % 10 == 0), "screen size error")

    print(SCREEN)
    pygame.init()
    screen = pygame.display.set_mode(SCREEN)
    clock = pygame.time.Clock()
    pygame.key.set_repeat(100, 50)
    make_maze()
    
    count = 0

    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                break

        press = pygame.key.get_pressed()
        if (press[pygame.K_ESCAPE]):
            break
    
        if (press[pygame.K_m]):
            make_maze()

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
                elif maze[j][i] == ObjAttr.GOAL:
                    goal = pygame.Rect(i * TILE_SIZE[0], j * TILE_SIZE[1],
                        TILE_SIZE[0], TILE_SIZE[1])
                    pygame.draw.rect(screen, GOAL_COLOR, goal)

        me = pygame.Rect(x, y, TILE_SIZE[0], TILE_SIZE[1])
        pygame.draw.rect(screen, ME_COLOR, me)
        pygame.display.flip()
        clock.tick(16)
        if (count % 100 == 0):
            print(f"[FPS] {clock.get_fps():.2f}")
        # if (count % 100 == 0):
        #     make_maze()
        count += 1

    pygame.quit()

if __name__ == '__main__':
    # parser = argparse.ArgumentParser()
    # parser.add_argument("-l", "--loop", type=int, default=-1, help="loop")
    # parser.add_argument("-r", "--rom", default="", help="rom")
    # parser.add_argument("-s", "--stop", action="store_true", help="stop after num of loop run")
    # args = parser.parse_args()
    # print(vars(args), tag="args", tag_color="green", color="white")

    run()