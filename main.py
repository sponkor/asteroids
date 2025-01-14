import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField 
from circleshape import Shot

def main():
    pygame.init
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    screen, clock, dt, updatable, drawable, astGroup, shotGroup =( 
        pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)),
        pygame.time.Clock(),
        0,
        pygame.sprite.Group(),
        pygame.sprite.Group(),
        pygame.sprite.Group(),
        pygame.sprite.Group()
    )
    AsteroidField.containers, Asteroid.containers, Player.containers, Shot.containers = (
         (updatable),
         (astGroup, updatable, drawable),
         (updatable, drawable),
         (shotGroup, updatable, drawable)
         )

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    astfield = AsteroidField()

    while True: #infinite while loop, used to update game
        pygame.Surface.fill(screen,000)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        for obj in updatable:
            obj.update(dt)
        for ast in astGroup:
            if ast.collision(player) == False:
                pass
            else: (
                print("Game over!"),
                pygame.quit(),
                quit()
            )
            for bullet in shotGroup:
                if ast.collision(bullet) == True:
                    bullet.kill()
                    ast.split()
                else: pass
        for obj in drawable:
            obj.draw(screen)
        
        
        
        pygame.display.flip()
        dt = clock.tick(60) / 1000






if __name__ == "__main__":
    main()