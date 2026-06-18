import random

import pygame
from pygame import Surface
from entities.circleshape import CircleShape
from util.constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
from util.logger import log_event
class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)
        


    def draw(self, screen: Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += self.velocity*dt

    def split(self):
        self.kill()
        if self.radius < ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        #split into 2 asteroids goin in a random direction of 20 to 50 degrees from current
        dir_a = random.uniform(20, 50)
        dir_b = random.uniform(20, 50)

        

        radius = self.radius-ASTEROID_MIN_RADIUS
        speed=1.2
        movement_a= self.velocity.rotate(dir_a)*speed
        movement_b = self.velocity.rotate(dir_b)*speed
        asteroid_a = Asteroid(self.position.x+radius, self.position.y+radius, radius)
        asteroid_b = Asteroid(self.position.x-radius, self.position.y-radius, radius)
        asteroid_a.velocity = movement_a
        asteroid_b.velocity = movement_b
    
