import pygame
import random

pygame.init()

WIDTH = 800
HEIGHT = 300

# 🎨 Colores tipo Chrome Dino
BG = (247, 247, 247)
BLACK = (83, 83, 83)
GROUND = (172, 172, 172)
GROUND_DARK = (100, 100, 100)


# =========================
# DINOSAURIO (pixel art animado)
# =========================
class Dinosaur:
    def __init__(self):
        self.x = 60
        self.y = 215

        self.vel_y = 0
        self.gravity = 1
        self.on_ground = True

        self.step = 0

    def jump(self):
        if self.on_ground:
            self.vel_y = -16
            self.on_ground = False

    def update(self):
        self.y += self.vel_y
        self.vel_y += self.gravity

        if self.y >= 215:
            self.y = 215
            self.vel_y = 0
            self.on_ground = True

        self.step += 1

    def draw(self, win):
        frame = (self.step // 6) % 2

        # 🦖 cuerpo base (pixel style)
        pygame.draw.rect(win, BLACK, (self.x + 10, self.y + 10, 22, 18))
        pygame.draw.rect(win, BLACK, (self.x + 25, self.y, 15, 15))  # cabeza
        pygame.draw.rect(win, BLACK, (self.x, self.y + 15, 12, 8))    # cola

        # ojo (pixel detalle)
        pygame.draw.rect(win, BG, (self.x + 32, self.y + 4, 3, 3))

        # patas animadas estilo Chrome
        if frame == 0:
            pygame.draw.rect(win, BLACK, (self.x + 12, self.y + 28, 6, 14))
            pygame.draw.rect(win, BLACK, (self.x + 22, self.y + 28, 6, 12))
        else:
            pygame.draw.rect(win, BLACK, (self.x + 14, self.y + 28, 6, 12))
            pygame.draw.rect(win, BLACK, (self.x + 24, self.y + 28, 6, 14))

    def rect(self):
        return pygame.Rect(self.x, self.y, 44, 47)


# =========================
# OBSTÁCULOS (CACTUS + PÁJARO)
# =========================
class Obstacle:
    def __init__(self):
        self.x = WIDTH
        self.type = random.choice(["small", "big", "bird"])

        if self.type == "small":
            self.y = 225
            self.w = 20
            self.h = 40

        elif self.type == "big":
            self.y = 210
            self.w = 30
            self.h = 55

        else:
            self.y = random.choice([170, 190])
            self.w = 36
            self.h = 12

    def update(self, speed):
        self.x -= speed

    def draw(self, win):

        if self.type in ["small", "big"]:
            # 🌵 cactus estilo pixel Chrome
            pygame.draw.rect(win, BLACK, (self.x + 8, self.y, 10, self.h))
            pygame.draw.rect(win, BLACK, (self.x, self.y + 10, 8, self.h - 10))
            pygame.draw.rect(win, BLACK, (self.x + 18, self.y + 15, 8, self.h - 15))

            # brazos
            pygame.draw.rect(win, BLACK, (self.x - 5, self.y + 18, 5, 12))
            pygame.draw.rect(win, BLACK, (self.x + 26, self.y + 25, 5, 12))

        else:
            # 🐦 pájaro pixel animado simple
            pygame.draw.rect(win, BLACK, (self.x, self.y, 10, 10))
            pygame.draw.rect(win, BLACK, (self.x + 10, self.y - 6, 10, 10))
            pygame.draw.rect(win, BLACK, (self.x + 20, self.y, 10, 10))

    def rect(self):
        return pygame.Rect(self.x, self.y, self.w, self.h)


# =========================
# SUELO CHROME STYLE
# =========================
class Ground:
    def __init__(self):
        self.x = 0

    def update(self, speed):
        self.x -= speed
        if self.x <= -800:
            self.x = 0

    def draw(self, win):
        pygame.draw.line(win, GROUND_DARK, (0, 260), (WIDTH, 260), 2)

        # textura pixel suelo
        for i in range(0, WIDTH, 10):
            pygame.draw.circle(win, GROUND, (i - self.x % 10, 262), 2)


# =========================
# SCORE
# =========================
class Score:
    def __init__(self):
        self.score = 0
        self.high = 0

    def update(self):
        self.score += 1