# Pygame шаблон - скелет для нового проекта Pygame
import pygame
import random

WIDTH = 900
HEIGHT = 900
FPS = 75

#Game Options
DIRECTIONX = 0
DIRECTIONY = 0
SPEED = 10
SCORE = 0

# Задаем цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)

class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(0, WIDTH), random.randint(0, HEIGHT))


     # def update(self):

        #ПИШЕМ СЮДА
        # if keys[K_LEFT]:
        #     print("h")

        # self.rect.x += 5
        # if self.rect.left > WIDTH:
        #     self.rect.right = 0


# Создаем игру и окно
pygame.init()
keys=pygame.key.get_pressed()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)
all_sprites = pygame.sprite.Group()
mob = Mob()
player = Player()
all_sprites.add(player)
all_sprites.add(mob)

# Цикл игры
running = True
while running:
    # Держим цикл на правильной скорости
    clock.tick(FPS)
    if (player.rect.colliderect(mob)):
        mob.rect.x = random.randint(0, WIDTH - 50)
        mob.rect.y = random.randint(0, HEIGHT - 50)
        SCORE += 1;
        SPEED += 1;
        textsurface = myfont.render(str(SCORE), False, (255, 255, 255))
        screen.blit(textsurface,(52,52))
        print(SCORE)
    if (player.rect.x < 0) or (player.rect.x > 890) or (player.rect.y > 890) or (player.rect.y < 0):
        running = False

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                # player.rect.x -= 90
                DIRECTIONX = -1
                DIRECTIONY = 0
            if event.key == pygame.K_RIGHT:
                # player.rect.x += 90
                DIRECTIONX = 1
                DIRECTIONY = 0
                # print(player.rect.x)
            if event.key == pygame.K_UP:
                # player.rect.y -= 90
                DIRECTIONX = 0
                DIRECTIONY = 1
            if event.key == pygame.K_DOWN:
                # player.rect.y += 90
                DIRECTIONX = 0
                DIRECTIONY = -1
                # print(player.rect.y)

    if DIRECTIONX == 1:
        player.rect.x += SPEED
    if DIRECTIONX == -1:
        player.rect.x -= SPEED
    if DIRECTIONY == 1:
        player.rect.y -= SPEED
    if DIRECTIONY == -1:
        player.rect.y += SPEED


    # Ввод процесса (события)
    for event in pygame.event.get():

        # check for closing window
        if event.type == pygame.QUIT:
            running = False

    # Обновление
    all_sprites.update()

    # Рендеринг
    screen.fill(BLACK)
    all_sprites.draw(screen)
    # После отрисовки всего, переворачиваем экран
    pygame.display.flip()

pygame.quit()
