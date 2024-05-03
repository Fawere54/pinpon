from pygame import *

WIN_WIDTH = 700
WIN_HEIGHT = 500
FPS = 60
BG = (100, 10, 0)

class GameSprite(sprite.Sprite):
    def __init__(self, player_sprite, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale( image.load(player_sprite), (size_x, size_y) )
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player1(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[ K_s ] and self.rect.y < 290:
            self.rect.y += self.speed
        if keys[ K_w ] and self.rect.y > 10:
            self.rect.y -= self.speed

class Player2(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[ K_DOWN ] and self.rect.y < 290:
            self.rect.y += self.speed
        if keys[ K_UP ] and self.rect.y > 10:
            self.rect.y -= self.speed

window = display.set_mode((WIN_WIDTH, WIN_HEIGHT))
display.set_caption('PingPong')

clock = time.Clock()

game = True
finish = False

playerR = Player1('racket.png', 600, 100, 50, 200, 5)
playerL = Player2('racket.png', 55, 100, 50, 200, 5)

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    window.fill(BG)

    playerL.reset()
    playerL.update()

    playerR.reset()
    playerR.update()

    display.update()
    clock.tick(FPS)