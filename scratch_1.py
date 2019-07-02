import sys
import pygame


from settings import settings

def run_game():
    pygame.init()
    infropy_settings = settings()
    screen = pygame.display.set_mode((infropy_settings.screen_width, infropy_settings.screen_height))
    pygame.display.set_caption("Invaders from python")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
             sys.exit()

        screen.fill(infropy_settings.bg_coulor)

        pygame.display.flip()

run_game()