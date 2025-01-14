from circleshape import CircleShape
from constants import *
import pygame
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "#FFFFFF", self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt

    def collision(self, other):
        return super().collision(other)
    
    def split(self):
        if self.radius > ASTEROID_MIN_RADIUS:
            randAngle = random.uniform(20, 50)
            for i in range(0, 2):
                newast = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
                if i == 1: randAngle = -randAngle
                newast.velocity = self.velocity.rotate(randAngle)
                newast.velocity *= 1.2
            self.kill()
        else: self.kill()
