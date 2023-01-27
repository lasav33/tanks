import pygame


class Finish(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('data/lose.png')
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 600