import pygame as pg # biblioteca pygame
from os import path # biblioteca do OS salvar arquivo Score.txt
from random import randint # bibioteca para posicionar aleatoriamente a caixa e cristal no eixo x e y
from random import randrange # bibioteca para posicionar aleatoriamente a caixa e cristal no eixo x e y
from settings import * # modularizar o codigo
from sprites import * # modularizar o codigo

class Game: 
    def __init__(self): # construtor da classe GAME
        # initialize game window, etc
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.running = True
        self.font_name = pg.font.match_font(FONT_NAME)
        self.load_data()
        self.score = 0
        self.max_score = 0
    
    def load_data(self):
        # carregar o score.txt
        self.dir = path.dirname(__file__)
        with open(path.join(self.dir, HS_FILE), 'r') as f:
            try:
                self.highscore = int(f.read())
            except:
                self.highscore = 0
    
    def new(self): # iniciar novo jogo
        
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

    def run(self): #  enquanto jogador estver jogando...
        # Game Loop
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def update(self): # atualizar todos os objetos em (FPS) 
        # Game Loop - Update
        self.all_sprites.update()
        # check if player hits a platform - only if falling

        if self.score < 0:
            self.playing = False

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

        hits = pg.sprite.spritecollide(self.player, self.boxes, False)
        if hits:
            self.score += -1 
            

        hits = pg.sprite.spritecollide(self.player, self.stars, False)
        if hits:
            self.score += 1
            self.max_score += 1
            self.rand_x = randint(0,WIDTH)
            self.rand_y = randint(0,15)
            self.star.pos = vec(self.rand_x,self.rand_y)
            self.star.vel = vec(0, 0)
            self.star.acc = vec(0, 0)

    def events(self): # Acionar Eventos (Pular) (Andar) (Fechar Jogo) Etc
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
                        
    def draw(self): # Desenhar na tela de fundo (BG_AZUL) e (PONTUAÇÃO)
        # Game Loop - draw
        self.screen.fill(LIGHTBLUE)
        self.all_sprites.draw(self.screen)
        self.draw_text('STARS: '+str(self.score), 35, YELLOW, 80, 20)
        pg.display.flip()

    def show_start_screen(self): # TELA INICIAL 
        self.screen.fill(BLACK)
        self.draw_text(TITLE, 48, WHITE, WIDTH / 2, HEIGHT / 4)
        self.draw_text("Setas para mover, cima pra pular", 22, WHITE, WIDTH / 2, HEIGHT / 2)
        self.draw_text("Precione qualquer tecla pra iniciar", 22, WHITE, WIDTH / 2, HEIGHT * 3 / 4)
        self.draw_text("Maior Score: " + str(self.highscore), 22, WHITE, WIDTH / 2, 15)
        pg.display.flip()
        self.wait_for_key()
        pg.display.flip()
    
    def show_go_screen(self): # TELA GAME OVER
        
        if not self.running:
            return
        self.screen.fill(BGCOLOR)
        self.draw_text("PERDEU PLAYBOY", 48, WHITE, WIDTH / 2, HEIGHT / 4)
        self.draw_text("SEU SCORE: " + str(self.max_score), 22, WHITE, WIDTH / 2, HEIGHT / 2)
        if self.max_score > self.highscore:
            self.highscore = self.max_score
            self.draw_text("NOVO SCORE!", 22, WHITE, WIDTH / 2, HEIGHT / 2 + 40)
            with open(path.join(self.dir, HS_FILE), 'w') as f:
                f.write(str(self.max_score))
        else:
            self.draw_text("MELHOR SCORE: " + str(self.highscore), 22, WHITE, WIDTH / 2, HEIGHT / 2 + 40)
        pg.display.flip()
        self.wait_for_key()

    def wait_for_key(self): # AGUARDAR A TECLA QUIT PRA FECHAR O JOGO
        waiting = True
        while waiting:
            self.clock.tick(FPS)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    waiting = False
                    self.running = False
                if event.type == pg.KEYUP:
                    waiting = False

    def draw_text(self, text, size, color, x, y): # FUNÇÃO QUE ESCREVE TEXTO NA JANELA DE PROJEÇÃO
        font = pg.font.Font(self.font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        self.screen.blit(text_surface, text_rect)

g = Game()
g.show_start_screen()
while g.running:
    g.new()
    g.show_go_screen()
pg.quit()