import pygame
from constants import *
def main():
    pygame.init
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True is True: #infinite while loop, used to draw visuals
        pygame.Surface.fill(screen,000)


        pygame.display.flip()






if __name__ == "__main__":
    main()