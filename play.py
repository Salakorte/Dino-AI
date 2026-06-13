import neat
import pygame
import pickle
import os
from game import *

pygame.init()

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
FONT = pygame.font.SysFont("consolas", 18)


def run():

    if not os.path.exists("best_dino.pkl"):
        print("❌ No hay modelo. Ejecuta train.py primero")
        return

    with open("best_dino.pkl", "rb") as f:
        winner = pickle.load(f)

    if winner is None:
        print("❌ Modelo corrupto")
        return

    config = neat.Config(
        neat.DefaultGenome,
        neat.DefaultReproduction,
        neat.DefaultSpeciesSet,
        neat.DefaultStagnation,
        "config-feedforward.txt"
    )

    net = neat.nn.FeedForwardNetwork.create(winner, config)

    dino = Dinosaur()
    obs = Obstacle()
    speed = 12

    score = 0
    clock = pygame.time.Clock()

    running = True

    while running:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        score += 1

        dino.update()
        obs.update(speed)

        dist = obs.x - dino.x
        output = net.activate((dist, dino.y, speed))

        if output[0] > 0.5:
            dino.jump()

        if dino.rect().colliderect(obs.rect()):
            print("💀 GAME OVER:", score)
            running = False

        if obs.x < -50:
            obs = Obstacle()

        WIN.fill(WHITE)

        draw_ground(WIN, pygame.time.get_ticks() // 10)

        obs.draw(WIN)
        dino.draw(WIN)

        WIN.blit(FONT.render(str(score), True, DARK_GRAY), (720, 10))

        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    run()