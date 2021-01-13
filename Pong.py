import sys
import os
import pygame
import pygame_gui

BLACK = (0, 0, 0)
GRAY = (200, 203, 200)

score = 0
score2 = 0

pygame.init()
pygame.display.set_caption('Pong')
size = width, height = 800, 600
screen = pygame.display.set_mode(size)
fps = 60


def terminate():
    pygame.quit()
    sys.exit()


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{name}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


def start_screen():
    """
    Начальная заставка с кнопками
    """
    global score
    global score2
    manager = pygame_gui.UIManager((800, 600), os.path.join('data', 'menu_theme.json'))
    # Кнопки
    start_btn = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((800 // 2 - 75, 600 // 3 - 25), (150, 50)),
        text='Начать игру',
        manager=manager
    )
    exit_btn = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((800 // 2 - 75, 600 // 2 + 125), (150, 50)),
        text='Выход',
        manager=manager
    )
    back = load_image('fon.jpg')
    screen.blit(back, (0, 0))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == start_btn:
                        score = 0
                        score2 = 0
                        game()
                    if event.ui_element == exit_btn:
                        terminate()
            manager.process_events(event)
        manager.update(fps / 1000)
        manager.draw_ui(screen)
        pygame.display.flip()
        clock.tick(fps)


def finish_screen():
    intro_text = ["Это",
                  "Было",
                  "Слишком лекго",
                  "Игрок номер один",
                  "Нажмите пробел чтобы вернуться в меню"]

    fon = pygame.transform.scale(load_image('fon.jpg'), (800, 600))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 50
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('gray'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    start_screen()
        pygame.display.flip()
        clock.tick(fps)


def finish_screen2():
    intro_text = ["Вау",
                  "Как ты смог ",
                  "Победить",
                  "Игрок номер два?",
                  "Нажмите пробел чтобы вернуться в меню"]

    fon = pygame.transform.scale(load_image('fon.jpg'), (800, 600))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 50
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('gray'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    start_screen()
        pygame.display.flip()
        clock.tick(fps)


class Ball(pygame.sprite.Sprite):
    def __init__(self, radius, x, y):
        super().__init__(all_sprites)
        self.radius = radius
        self.image = pygame.Surface((2 * radius, 2 * radius),
                                    pygame.SRCALPHA, 32)
        pygame.draw.circle(self.image, pygame.Color("white"),
                           (radius, radius), radius)
        self.rect = pygame.Rect(x, y, 2 * radius, 2 * radius)
        self.vx = 4
        self.vy = 5

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


def game():
    global score
    global score2
    Border(0, 100, 800, 100)
    Border(5, height - 5, width - 5, height - 5)
    player = Pl(0, 200, 20, 350)
    player2 = Pl2(780, 200, 800, 350)
    ball = Ball(12, 400, 300)
    for i in range(1):
        ball
    running = True
    while running:
        if ball.rect.x >= 800:
            ball.rect.x = 400
            ball.rect.y = 300
            score += 1
            if score == 3:
                player.kill()
                player2.kill()
                ball.kill()
                finish_screen()
        elif ball.rect.x <= 0:
            ball.rect.x = 400
            ball.rect.y = 300
            score2 += 1
            if score2 == 3:
                player.kill()
                player2.kill()
                ball.kill()
                finish_screen2()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                terminate()
        if pygame.key.get_pressed()[pygame.K_w]:
            player.rect.y -= 7
            if player.rect.y < 99:
                player.rect.y = 100
        if pygame.key.get_pressed()[pygame.K_s]:
            player.rect.y += 7
            if player.rect.y > 455:
                player.rect.y = 455
        if pygame.key.get_pressed()[pygame.K_UP]:
            player2.rect.y -= 7
            if player2.rect.y < 99:
                player2.rect.y = 100
        if pygame.key.get_pressed()[pygame.K_DOWN]:
            player2.rect.y += 7
            if player2.rect.y > 455:
                player2.rect.y = 455
        draw()
        screen.fill((0, 0, 0))
        all_sprites.draw(screen)
        all_sprites.update()
        font = pygame.font.Font(None, 85)
        text = font.render(str(score), 1, (255, 255, 255))
        screen.blit(text, (200, 25))
        text = font.render(str(score2), 1, (255, 255, 255))
        screen.blit(text, (600, 25))
        clock.tick(fps)
        draw()
        pygame.display.flip()


clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
horizontal_borders = pygame.sprite.Group()
vertical_borders = pygame.sprite.Group()
start_screen()
pygame.quit()
