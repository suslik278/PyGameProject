import pygame
import random

BLACK = (0, 0, 0)
GRAY = (200, 203, 200)

pygame.init()
pygame.display.set_caption('Pong')
size = width, height = 800, 600
screen = pygame.display.set_mode(size)


class Ball(pygame.sprite.Sprite):
    def __init__(self, radius, x, y):
        super().__init__(all_sprites)
        self.radius = radius
        self.image = pygame.Surface((2 * radius, 2 * radius),
                                    pygame.SRCALPHA, 32)
        pygame.draw.circle(self.image, pygame.Color("white"),
                           (radius, radius), radius)
        self.rect = pygame.Rect(x, y, 2 * radius, 2 * radius)
        self.vx = 1
        self.vy = random.randrange(-30, 30)

    def update(self):
        self.rect = self.rect.move(self.vx, self.vy)
        if pygame.sprite.spritecollideany(self, horizontal_borders):
            self.vy = -self.vy
        if pygame.sprite.spritecollideany(self, vertical_borders):
            self.vx = -self.vx


class Border(pygame.sprite.Sprite):
    # строго вертикальный или строго горизонтальный отрезок
    def __init__(self, x1, y1, x2, y2):
        super().__init__(all_sprites)
        if x1 == x2:  # вертикальная стенка
            self.add(vertical_borders)
            self.image = pygame.Surface([6, y2 - y1])
            self.image.fill([255, 255, 255])
            self.rect = pygame.Rect(x1, y1, 1, y2 - y1)
        else:  # горизонтальная стенка
            self.add(horizontal_borders)
            self.image = pygame.Surface([x2 - x1, 6])
            self.image.fill([255, 255, 255])
            self.rect = pygame.Rect(x1, y1, x2 - x1, 1)


class Pl(pygame.sprite.Sprite):
    def __init__(self, x1, y1, x2, y2):
        super().__init__(all_sprites)
        self.add(vertical_borders)
        self.image = pygame.Surface([x2 - x1, y2 - y1])
        self.image.fill([255, 255, 255])
        self.rect = pygame.Rect(x1, y1, x2 - x1, y2 - y1)


class Pl2(pygame.sprite.Sprite):
    def __init__(self, x1, y1, x2, y2):
        super().__init__(all_sprites)
        self.add(vertical_borders)
        self.image = pygame.Surface([x2 - x1, y2 - y1])
        self.image.fill([255, 255, 255])
        self.rect = pygame.Rect(x1, y1, x2 - x1, y2 - y1)

def draw():
    pygame.draw.line(screen, GRAY, (400, 0), (400, 600), 5)



if __name__ == '__main__':
    all_sprites = pygame.sprite.Group()
    horizontal_borders = pygame.sprite.Group()
    vertical_borders = pygame.sprite.Group()
    Border(0, 100, 800, 100)

    player = Pl(0, 200, 20, 350)
    player2 = Pl2(780, 200, 800, 350)
    for i in range(1):
        Ball(20, 100, 500)
    fps = 60
    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        if pygame.key.get_pressed()[pygame.K_w]:
            player.rect.y -= 7
        if pygame.key.get_pressed()[pygame.K_s]:
            player.rect.y += 7
        if pygame.key.get_pressed()[pygame.K_UP]:
            player2.rect.y -= 7
        if pygame.key.get_pressed()[pygame.K_DOWN]:
            player2.rect.y += 7
        draw()
        screen.fill((0, 0, 0))
        all_sprites.draw(screen)
        all_sprites.update()
        clock.tick(fps)
        draw()
        pygame.display.flip()
    pygame.quit()
