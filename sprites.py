import pygame as pg
from time import sleep
from random import randint
from random import randrange
from settings import *
vec = pg.math.Vector2

class Player(pg.sprite.Sprite):
    def __init__(self, game):
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.image = pg.Surface((30, 40))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.pos = vec(WIDTH / 2+100, HEIGHT / 2)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)


    def jump(self):
        # pular apenas quando tiver na plataforma
        self.rect.x += 1
        hits = pg.sprite.spritecollide(self, self.game.platforms, False)
        self.rect.x -= 1
        if hits:
            self.vel.y = -20
        self.rect.x -= 1
        if hits:
            self.vel.y = -20

    def update(self):
        self.acc = vec(0, PLAYER_GRAV)
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.acc.x = -PLAYER_ACC
        if keys[pg.K_RIGHT]:
            self.acc.x = PLAYER_ACC
        
        # apply friction
        self.acc.x += self.vel.x * PLAYER_FRICTION
        # equations of motion
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        # nao permitir que o objeto ultrapasse o limite da janela
        if self.pos.x > WIDTH:
            self.pos.x = WIDTH
        if self.pos.x < 0:
            self.pos.x = 0
        self.rect.midbottom = self.pos
        
        
        




class Box(pg.sprite.Sprite):
    def __init__(self, game): 
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.image = pg.Surface((40, 40))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)

      
        self.rand_x = randrange(0,WIDTH,40)
        self.rand_y = randint(0,100)
        self.pos = vec(self.rand_x, self.rand_y)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)


    def update(self):
        self.acc = vec(0, BOX_GRAV)
        # apply friction
        self.acc.x += self.vel.x * BOX_FRICTION
        # equations of motion
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc 
        self.rect.midbottom = self.pos


         
        

        
  

class Platform2(pg.sprite.Sprite):
    def __init__(self, game):
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.image = pg.Surface((WIDTH, 40))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = HEIGHT -40


class Star(pg.sprite.Sprite):
    def __init__(self, game):
        
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.image = pg.Surface((20, 20))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)

      
        self.rand_x = randrange(0,WIDTH,20)
        self.rand_y = randint(0,100)
        self.pos = vec(self.rand_x, self.rand_y)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)


    def update(self):
        self.acc = vec(0, BOX_GRAV)
        # apply friction
        self.acc.x += self.vel.x * BOX_FRICTION
        # equations of motion
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc 
        self.rect.midbottom = self.pos

