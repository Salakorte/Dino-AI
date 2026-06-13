import neat
import pygame
import pickle
from game import *

pygame.init()

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
FONT = pygame.font.SysFont("consolas", 20)


def eval_genomes(genomes, config):

    nets = []
    ge = []
    dinos = []

    obstacles = [Obstacle()]
    ground = Ground()

    SPEED = 12
    score = Score()

    for _, genome in genomes:
        genome.fitness = 0
        net = neat.nn.FeedForwardNetwork.create(genome, config)

        nets.append(net)
        dinos.append(Dinosaur())
        ge.append(genome)

    clock = pygame.time.Clock()

    run = True

    while run and len(dinos) > 0:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        score.update()

        ground.update(SPEED)

        for d in dinos:
            d.update()

        obs = obstacles[0]

        for i, dino in enumerate(dinos):

            dist = obs.x - dino.x
            out = nets[i].activate((dist, dino.y, SPEED))

            if out[0] > 0.5:
                dino.jump()

            ge[i].fitness += 0.1

        for o in obstacles:
            o.update(SPEED)

            for i, dino in enumerate(dinos):
                if dino.rect().colliderect(o.rect()):
                    ge[i].fitness -= 5
                    dinos.pop(i)
                    nets.pop(i)
                    ge.pop(i)
                    break

        if obstacles[-1].x < 500:
            obstacles.append(Obstacle())

        if obstacles[0].x < -50:
            obstacles.pop(0)

        # DRAW
        WIN.fill(BG)

        ground.draw(WIN)

        for o in obstacles:
            o.draw(WIN)

        for d in dinos:
            d.draw(WIN)

        WIN.blit(FONT.render(str(int(score.score)), True, GROUND_DARK), (720, 10))

        pygame.display.update()


def run():

    config = neat.Config(
        neat.DefaultGenome,
        neat.DefaultReproduction,
        neat.DefaultSpeciesSet,
        neat.DefaultStagnation,
        "config-feedforward.txt"
    )

    p = neat.Population(config)

    p.add_reporter(neat.StdOutReporter(True))
    p.add_reporter(neat.StatisticsReporter())

    winner = p.run(eval_genomes, 50)

    with open("best_dino.pkl", "wb") as f:
        pickle.dump(winner, f)


if __name__ == "__main__":
    run()