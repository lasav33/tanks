import pygame
import random


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.xvel = 0
        self.yvel = 0
        self.image = pygame.image.load('data/enemy.png')
        self.image.convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = 710
        self.rect.y = 40
        self.rot = 'left'

    def updateVel(self, platforms):
        if self.collide(platforms):
            self.rot = rotation[random.randint(0, 3)]
        if self.rot == 'left':
            self.xvel = -ENEMY_SPEED
        if self.rot == 'right':
            self.xvel = ENEMY_SPEED
        if self.rot == 'up':
            self.yvel = -ENEMY_SPEED
        if self.rot == 'down':
            self.yvel = ENEMY_SPEED
        if self.rot != 'down' and self.rot != 'up':
            self.yvel = 0
        if self.rot != 'right' and self.rot != 'left':
            self.xvel = 0
        self.rotation()
        self.rect.y += self.yvel
        self.rect.x += self.xvel
        print(self.rect.x, self.rect.y, self.rot)

    def collide(self, platforms):
        for p in platforms:
            if pygame.sprite.collide_rect(self, p):
                if self.rot == 'right':
                    self.rect.right = p.rect.left

                if self.rot == 'left':
                    self.rect.left = p.rect.right

                if self.rot == 'down':
                    self.rect.bottom = p.rect.top

                if self.rot == 'up':
                    self.rect.top = p.rect.bottom
                return True

    def rotation(self):
        global route
        self.new_image = pygame.image.load('data/enemy.png')
        if self.rot == 'left':
            self.new_image = pygame.transform.flip(self.new_image, True, False)
            route = 180
        if self.rot == 'up':
            self.new_image = pygame.transform.rotate(self.new_image, 90)
            route = 90
        if self.rot == 'down':
            self.new_image = pygame.transform.rotate(self.new_image, -90)
            route = -90
        if self.rot == 'right':
            route = 0
        self.image = self.new_image


rotation = ['left', 'right', 'up', 'down']
ENEMY_SPEED = 4
