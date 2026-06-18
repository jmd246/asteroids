import pygame
from pygame import Surface
from entities.circleshape import CircleShape
from util.constants import LINE_WIDTH
class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)
        #gravity
        self.velocity = pygame.Vector2(0,50)


    def draw(self, screen: Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += self.velocity*dt