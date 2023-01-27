import pygame
import border
import road
import random
import bullet
import enemies


class Player_tank(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.xvel = 0
        self.yvel = 0
        self.image = pygame.image.load('data/player_tank.png')
        self.image.convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = 50
        self.rect.y = 520

    def updateVel(self):
        global run
        if left and not run:
            self.xvel = -PLAYER_SPEED
            run = True
        if right and not run:
            self.xvel = PLAYER_SPEED
            run = True
        if up and not run:
            self.yvel = -PLAYER_SPEED
            run = True
        if down and not run:
            self.yvel = PLAYER_SPEED
            run = True
        if not (left or right or up or down):
            run = False
        if not (left or right):
            self.xvel = 0
        if not (up or down):
            self.yvel = 0
        if run:
            self.rotation()
        self.rect.y += self.yvel
        self.collide()
        self.rect.x += self.xvel
        self.collide()

    def rotation(self):
        global route
        self.new_image = pygame.image.load('data/player_tank.png')
        if left:
            self.new_image = pygame.transform.flip(self.new_image, True, False)
            route = 180
        if up:
            self.new_image = pygame.transform.rotate(self.new_image, 90)
            route = 90
        if down:
            self.new_image = pygame.transform.rotate(self.new_image, -90)
            route = -90
        if right:
            route = 0
        self.image = self.new_image

    def collide(self):
        for p in platforms:
            if pygame.sprite.collide_rect(self, p):

                if self.xvel > 0:
                    self.rect.right = p.rect.left

                if self.xvel < 0:
                    self.rect.left = p.rect.right

                if self.yvel > 0:
                    self.rect.bottom = p.rect.top

                if self.yvel < 0:
                    self.rect.top = p.rect.bottom


mapp = ['********************',
        '*                  *',
        '* **************** *',
        '* **            ** *',
        '*    ******* ** *  *',
        '****         **   **',
        '*    ** * ******* **',
        '* ***** *         **',
        '*       * ******* **',
        '* ******* **       *',
        '*    ***  ** ***** *',
        '****   * *   **    *',
        '*  *** * * **** ** *',
        '*                  *',
        '********************']

homes = ['data/home1.png', 'data/home2.png', 'data/home3.png', 'data/home4.png']
route = 0
run = False
timer = pygame.time.Clock()
PLAYER_SPEED = 1
pygame.init()
size = width, height = 800, 600
screen = pygame.display.set_mode(size)
pygame.display.flip()
platforms = list()
all_objects = pygame.sprite.Group()
bullet_all = list()
for i in range(15):
    for j in range(20):
        if mapp[i][j] == '*':
            bord = border.Border(j * 40, i * 40, homes[random.randrange(len(homes))])
            platforms.append(bord)
            all_objects.add(bord)
        else:
            roads = road.Road(j * 40, i * 40)
            all_objects.add(roads)
gamer = Player_tank()
all_objects.add(gamer)
GAME = True
clock = pygame.time.Clock()
fps = 60
left = False
right = False
up = False
down = False
enemy = enemies.Enemy()
all_objects.add(enemy)
while GAME:
    timer.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GAME = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_a:
            left = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_d:
            right = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_w:
            up = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
            down = True
        if event.type == pygame.KEYUP and event.key == pygame.K_d:
            right = False
        if event.type == pygame.KEYUP and event.key == pygame.K_a:
            left = False
        if event.type == pygame.KEYUP and event.key == pygame.K_w:
            up = False
        if event.type == pygame.KEYUP and event.key == pygame.K_s:
            down = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            bull = bullet.Bullet(route, gamer.rect.x, gamer.rect.y)
            bullet_all.append(bull)

    screen.fill('black')
    all_objects.draw(screen)
    for obj in bullet_all:
        obj.updateVelion()
        for i in platforms:
            if i.collide(obj):
                bullet_all.pop(bullet_all.index(obj))
        obj.draw(screen)
        print(bullet_all)
    enemy.updateVel(platforms)
    gamer.updateVel()
    clock.tick(fps)
    pygame.display.flip()
pygame.quit()
