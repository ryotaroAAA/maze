import pygame
import copy
# from dataclasses import *
# from enum import auto, Enum
import logging
import logging.config
import numpy as np
# from pathlib import Path
import sys
import time
import traceback
# from typing import DefaultDict
import argparse
# from hexdump import hexdump
from pprint import *
# from print_color import print
# from tabulate import tabulate
# import yaml

WHITE = (255, 255, 255)
RED = (255, 0, 0)

SCREEN = (640, 480)
OBJ = (10, 10)

pygame.init()
screen = pygame.display.set_mode(SCREEN)
myclock = pygame.time.Clock()
pygame.key.set_repeat(1000, 1000)

flag=0
x = 250
y = 250

# @dataclass
# class Obj:
#     x: int = 0
#     y: int = 0
#     attr: ObjAttr()

#     def reset(self):
#         self.X = 0
#         self.Y = 0

# class ObjAttr(Enum):
#     collisionable = auto() 
#     breakable = auto()

# @dataclass
class Hero:
    # x: int = 0
    # y: int = 0
    # attr: ObjAttr()

    def __init__(self):
        self.X = 0
        self.Y = 0
    

def run(args):
    me = Hero()
    flag = 0
    while flag==0:
        for event in pygame.event.get():
            if event.type==pygame.QUIT: flag=1

        press = pygame.key.get_pressed()

        if (press[pygame.K_LEFT] and (x - OBJ[0]) >= 0):
            x -= OBJ[0]

        if (press[pygame.K_RIGHT] and
                (x + OBJ[0]) < SCREEN[0]):
            x += OBJ[0]
        
        if (press[pygame.K_UP] and (y - OBJ[1]) >= 0):
            y -= OBJ[1]

        if (press[pygame.K_DOWN] and
                (y + OBJ[1]) < SCREEN[1]):
            y += OBJ[1]
        
        if (press[pygame.K_ESCAPE]):
            break

        screen.fill(WHITE)
        rect = pygame.Rect(x, y, 10, 10)
        pygame.draw.rect(screen, RED, rect)
        pygame.display.flip()
        myclock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    # parser.add_argument("-l", "--loop", type=int, default=-1, help="loop")
    args = parser.parse_args()
    # print(vars(args), tag="args", tag_color="green", color="white")
    print(vars(args))

    run(args)