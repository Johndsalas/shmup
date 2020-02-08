# pygame templet - skeleton for a new pygame project
import pygame
import random
from os import path

# get path to image folder
img_dir =path.join(path.dirname(__file__),'img')

width = 480
height = 600
fps = 60

# define colors
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
yellow = (255,255,0)

# initialize pygame
pygame.init()
pygame.mixer.init()

# create window
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Shmup")
clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(player_img, (50, 38))
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()
        self.rect.centerx = width/2
        self.rect.bottom = height -10
        self.speedx = 0

    def update(self):

        # set speed to 0
        self.speedx = 0

        # get key presses
        keystate = pygame.key.get_pressed()

        # if key press is a move sprite to the left
        if keystate[pygame.K_a]:
            self.speedx = -5

        # if key press is s move sprite to the right
        if keystate[pygame.K_s]:
            self.speedx = 5

        # update movement
        self.rect.x += self.speedx

        # set side of screen as a barrier 
        if self.rect.right > width:
            self.rect.right = width
        if self.rect.left < 0:
            self.rect.left = 0
    
    def shoot(self):
        # spawn bullet at (x,y)
        bullet = Bullet(self.rect.centerx,self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)

class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = meteor_img
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0,width-self.rect.width)
        self.rect.y = random.randrange(-100,-40)
        self.speedy = random.randrange(1,8)
        self.speedx =random.randrange(-3,+3)

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > height+10 or self.rect.left < -25 or self.rect.right > width + 20:
            self.rect.x = random.randrange(0,width-self.rect.width)
            self.rect.y = random.randrange(-100,-40)
            self.speedy = random.randrange(1,8)

class Bullet(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = bullet_img
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10

    def update(self):
        self.rect.y += self.speedy

        # remove bullet if it leaves the screen
        if self.rect.bottom < 0:
            self.kill()

# load all game graphics
background = pygame.image.load(path.join(img_dir, "stars-in-the-night-sky.png")).convert()
background_rect = background.get_rect()
player_img = pygame.image.load(path.join(img_dir, "playerShip1_orange.png")).convert()
meteor_img = pygame.image.load(path.join(img_dir, "meteorBrown_med1.png")).convert()
bullet_img = pygame.image.load(path.join(img_dir, "laserRed16.png")).convert()

# sprite groups
all_sprites = pygame.sprite.Group()
mobs = pygame.sprite.Group()
bullets = pygame.sprite.Group()

player = Player()
all_sprites.add(player)

# add range number of mobs to sprite groups
for i in range(8):
    m = Mob()
    all_sprites.add(m)
    mobs.add(m)

# game loop

running = True

while running:

    # keep loop running at the right speed
    clock.tick(fps)

    # process input (events)
    for event in pygame.event.get():

        # check for closing the window
        if event.type == pygame.QUIT:
            running = False

        # check for pressed key
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_SPACE:
                player.shoot()


    # update
    all_sprites.update()

    # check to see if a bullet has hit a mob. True = corresponding sprite deleted if hit
    hits = pygame.sprite.groupcollide(mobs,bullets,True,True)
    
    # respawn hit mobs
    for hit in hits:
        m = Mob()
        all_sprites.add(m)
        mobs.add(m)


    # check to see if a mob hit the player
    hits = pygame.sprite.spritecollide(player,mobs,False)
    if hits:
        running = False

    # draw / render
    screen.fill(black)
    screen.blit(background,background_rect)
    all_sprites.draw(screen)

    pygame.display.flip() # after drawing everything

pygame.display.quit()
pygame.quit()
exit()
