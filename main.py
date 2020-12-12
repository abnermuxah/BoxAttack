import pygame as pg
from random import randint
from random import randrange
from time import sleep
from settings import *
from sprites import *

class Game: 
    def __init__(self):
        # initialize game window, etc
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.running = True

    def new(self):
        # start a new game
        self.all_sprites = pg.sprite.Group()
        self.platforms = pg.sprite.Group()
        self.boxes = pg.sprite.Group()
        self.stars = pg.sprite.Group()

        self.player = Player(self)
        self.all_sprites.add(self.player)

        
    
        
        self.box1 = Box(self)
        self.boxes.add(self.box1)
        self.all_sprites.add(self.box1)

        self.box2 = Box(self)
        self.boxes.add(self.box2)
        self.all_sprites.add(self.box2)

        self.box3 = Box(self)
        self.boxes.add(self.box3)
        self.all_sprites.add(self.box3)

        self.box4 = Box(self)
        self.boxes.add(self.box4)
        self.all_sprites.add(self.box4)

        self.box5 = Box(self)
        self.boxes.add(self.box5)
        self.all_sprites.add(self.box5)

        self.box6 = Box(self)
        self.boxes.add(self.box6)
        self.all_sprites.add(self.box6)

        self.star = Star(self)
        self.stars.add(self.star)
        self.all_sprites.add(self.star)

            
        self.platform2 = Platform2(self)
        self.all_sprites.add(self.platform2)
        self.platforms.add(self.platform2)

        self.run()

    def run(self):
        # Game Loop
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def update(self):
        # Game Loop - Update
        self.all_sprites.update()
        # check if player hits a platform - only if falling
        if self.player.vel.y > 0:
            hits = pg.sprite.spritecollide(self.player, self.platforms, False)
            if hits:
                self.player.pos.y = hits[0].rect.top
                self.player.vel.y = 0
        if self.box1.vel.y > 0:
            hits = pg.sprite.spritecollide(self.box1, self.platforms, False)
            if hits:
                self.rand_x = randrange(0,WIDTH,40)
                self.rand_y = randint(0,220)
                self.box1.pos = vec(self.rand_x,self.rand_y)
                self.box1.vel = vec(0, 0)
                self.box1.acc = vec(0, 0)
        if self.box2.vel.y > 0:
            hits = pg.sprite.spritecollide(self.box2, self.platforms, False)
            if hits:
                self.rand_x = randrange(0,WIDTH,40)
                self.rand_y = randint(0,50)
                self.box2.pos = vec(self.rand_x,self.rand_y)
                self.box2.vel = vec(0, 0)
                self.box2.acc = vec(0, 0)
        if self.box3.vel.y > 0:
            hits = pg.sprite.spritecollide(self.box3, self.platforms, False)
            if hits:
                self.rand_x = randrange(0,WIDTH,40)
                self.rand_y = randint(0,150)
                self.box3.pos = vec(self.rand_x,self.rand_y)
                self.box3.vel = vec(0, 0)
                self.box3.acc = vec(0, 0)
        if self.box4.vel.y > 0:
            hits = pg.sprite.spritecollide(self.box4, self.platforms, False)
            if hits:
                self.rand_x = randrange(0,WIDTH,40)
                self.rand_y = randint(0,150)
                self.box4.pos = vec(self.rand_x,self.rand_y)
                self.box4.vel = vec(0, 0)
                self.box4.acc = vec(0, 0)
        if self.box5.vel.y > 0:
            hits = pg.sprite.spritecollide(self.box5, self.platforms, False)
            if hits:
                self.rand_x = randrange(0,WIDTH,40)
                self.rand_y = randint(0,150)
                self.box5.pos = vec(self.rand_x,self.rand_y)
                self.box5.vel = vec(0, 0)
                self.box5.acc = vec(0, 0)
        if self.box6.vel.y > 0:
            hits = pg.sprite.spritecollide(self.box5, self.platforms, False)
            if hits:
                self.rand_x = randrange(0,WIDTH,40)
                self.rand_y = randint(0,15)
                self.box6.pos = vec(self.rand_x,self.rand_y)
                self.box6.vel = vec(0, 0)
                self.box6.acc = vec(0, 0)
        if self.star.vel.y > 0:
            hits = pg.sprite.spritecollide(self.star, self.platforms, False)
            if hits:
                self.rand_x = randint(0,WIDTH)
                self.rand_y = randint(0,15)
                self.star.pos = vec(self.rand_x,self.rand_y)
                self.star.vel = vec(0, 0)
                self.star.acc = vec(0, 0)

        
        
        
        

    def events(self):
        # Game Loop - events
        for event in pg.event.get():
            # check for closing window
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_UP:
                    self.player.jump()

    def draw(self):
        # Game Loop - draw
        self.screen.fill(LIGHTBLUE)
        self.all_sprites.draw(self.screen)
        # *after* drawing everything, flip the display
        pg.display.flip()

    def show_start_screen(self):
        # game splash/start screen
        pass

    def show_go_screen(self):
        # game over/continue
        pass

g = Game()
g.show_start_screen()
while g.running:
    g.new()
    g.show_go_screen()
    print(g.player.vel)
pg.quit()