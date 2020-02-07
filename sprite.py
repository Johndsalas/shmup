# opengameart.org
# flatIcon.com
#Icons made by <a href="https://www.flaticon.com/authors/smashicons" title="Smashicons">Smashicons</a> from <a href="https://www.flaticon.com/" title="Flaticon"> www.flaticon.com</a>
# pygame templet - skeleton for a new pygame project
import pygame
import random
import os

width = 800
height = 600
fps = 30

# define colors
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

# set up assets folders
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder,"img")

class Player(pygame.sprite.Sprite):
    # sprite for the player
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(img_folder, "alien.png")).convert()
        self.image.set_colorkey(white)
        self.rect = self.image.get_rect()
        self.rect.center = (width/2,height/2)
        self.y_speed = 5

    def update(self):
        self.rect.x += 5
        self.rect.y += self.y_speed
        
        if self.rect.bottom > height - 200:
            self.y_speed = -5
        
        if self.rect.top < 200:
            self.y_speed = 5
        
        if self.rect.left > width:
            self.rect.right = 0

# initialize pygame
pygame.init()
pygame.mixer.init()

# create window
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()


all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

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
    # update
    all_sprites.update()
    # draw / reorder
    screen.fill(black)
    all_sprites.draw(screen)

    pygame.display.flip() # after drawing everything

pygame.QUIT()