import pygame
import random

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
            self.image = pygame.Surface([1, y2 - y1])
            self.image.fill([255, 255, 255])
            self.rect = pygame.Rect(x1, y1, 1, y2 - y1)
        else:  # горизонтальная стенка
            self.add(horizontal_borders)
            self.image = pygame.Surface([x2 - x1, 1])
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


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Pong')
    size = width, height = 800, 600
    screen = pygame.display.set_mode(size)
    all_sprites = pygame.sprite.Group()
    horizontal_borders = pygame.sprite.Group()
    vertical_borders = pygame.sprite.Group()
    Border(5, height - 5, width - 5, height - 5)
    Border(5, 5, 50, height - 5)
    Border(width - 5, 5, width - 5, height - 5)

    player = Pl(0, 400, 20, 600)
    player2 = Pl2(780, 400, 800, 600)
    for i in range(1):
        Ball(20, 100, 500)
    fps = 60
    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    player2.rect.y -= 10
                if event.key == pygame.K_DOWN:
                    player2.rect.y += 10
                if event.key == pygame.K_w:
                    player.rect.y -= 10
                if event.key == pygame.K_s:
                    player.rect.y += 10
        screen.fill((0, 0, 0))
        all_sprites.draw(screen)
        all_sprites.update()
        clock.tick(fps)
        pygame.display.flip()
    pygame.quit()