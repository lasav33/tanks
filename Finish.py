import pygame


class Finish(pygame.sprite.Sprite):
    def __init__(self, win):
        pygame.sprite.Sprite.__init__(self)
        if not win:
            self.image = pygame.image.load('data/lose.png')
        else:
            self.image = pygame.image.load('data/win.png')
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 600