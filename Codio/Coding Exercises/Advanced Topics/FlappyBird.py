# Flappy Bird clone

import pygame
import sys
from game import Game

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((400, 720))
    clock = pygame.time.Clock()

    SPAWNPIPE = pygame.USEREVENT
    pygame.time.set_timer(SPAWNPIPE, 1800)

    game = Game('student_folder/flappy_bird/bird.png', 'student_folder/flappy_bird/pipe.png',
                'student_folder/flappy_bird/background.png', 'student_folder/flappy_bird/ground.png')
    game.resize_images()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and game.active:
                    game.flap()

                if event.key == pygame.K_SPACE and game.active == False:
                    game.restart()

            if event.type == SPAWNPIPE:
                game.add_pipe()

        game.show_background(screen)

        if game.active:
            game.show_bird(screen)
            game.update_bird()
            game.move_pipes()
            game.show_pipes(screen)
            game.check_collision()
            game.update_score()
            game.show_score('playing', screen, (255, 255, 255))
        else:
            game.game_over(screen, (255, 255, 255))

        game.show_ground(screen)
        game.move_ground()

        pygame.display.update()
        clock.tick(120)