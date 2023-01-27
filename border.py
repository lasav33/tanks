import pygame


class Border(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def checker(self, player):
        return not self.rect.colliderect(player.rect)

    def stop(self, player):
        if player.xvel > 0:
            self.rect.right = player.rect.left

        if player.xvel < 0:
            self.rect.left = player.rect.right

        if player.yvel > 0:
            self.rect.bottom = player.rect.top

        if player.yvel < 0:
            self.rect.top = player.rect.bottom

    def collide(self, obj):
        if pygame.sprite.collide_rect(self, obj):
            del obj
            return True
        return False
