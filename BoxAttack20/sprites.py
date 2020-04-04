import pygame as pg # chamar sempre pg ao ives de pygame
from random import randint
from settings import *

class Platform(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((WIDTH, 40))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = HEIGHT -40
