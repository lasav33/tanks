import pygame


class Bullet(pygame.sprite.Sprite):
    def __init__(self, rout, x, y, bul=False):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((8, 8))
        self.color = (255, 0, 0)
        self.yvel = 0
        self.xvel = 0
        self.gamer = bul
        if rout == 0:
            self.rect = pygame.Rect(x + 30, y + 12, 8, 8)
            self.xvel = 8
        if rout == 90:
            self.rect = pygame.Rect(x + 12, y - 8, 8, 8)
            self.yvel = -8
        if rout == -90:
            self.rect = pygame.Rect(x + 12, y + 30, 8, 8)
            self.yvel = 8
        if rout == 180:
            self.rect = pygame.Rect(x - 8, y + 12, 8, 8)
            self.xvel = -8

    def updateVelion(self):
        self.rect.x += self.xvel
        self.rect.y += self.yvel

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
