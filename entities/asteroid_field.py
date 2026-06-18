import random
from collections.abc import Callable

import pygame
from entities.asteroid import Asteroid
from util.constants import (
    ASTEROID_KINDS,
    ASTEROID_MAX_RADIUS,
    ASTEROID_MIN_RADIUS,
    ASTEROID_SPAWN_RATE_SECONDS,
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
)

# A pair containing a direction vector and a function that computes a spawn point
# along the corresponding edge of the screen.
Edge = tuple[pygame.Vector2, Callable[[float], pygame.Vector2]]


class AsteroidField(pygame.sprite.Sprite):
    containers: pygame.sprite.Group

    # Predefine the four screen edges where new asteroids may appear.
    # Each edge is represented by:
    # - a direction vector (used to determine asteroid motion)
    # - a lambda that maps a normalized position to a screen coordinate
    edges: list[Edge] = [
        (
            pygame.Vector2(1, 0),   
            lambda y: pygame.Vector2(-ASTEROID_MAX_RADIUS, y * SCREEN_HEIGHT),
        ),
        (
            pygame.Vector2(-1, 0),
            lambda y: pygame.Vector2(
                SCREEN_WIDTH + ASTEROID_MAX_RADIUS, y * SCREEN_HEIGHT
            ),
        ),
        (
            pygame.Vector2(0, 1),
            lambda x: pygame.Vector2(x * SCREEN_WIDTH, -ASTEROID_MAX_RADIUS),
        ),
        (
            pygame.Vector2(0, -1),
            lambda x: pygame.Vector2(
                x * SCREEN_WIDTH, SCREEN_HEIGHT + ASTEROID_MAX_RADIUS
            ),
        ),
    ]

    def __init__(self) -> None:
        # Initialize the sprite base class and reset the spawn timer.
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.spawn_timer = 0.0

    def spawn(
        self, radius: float, position: pygame.Vector2, velocity: pygame.Vector2
    ) -> None:
        # Create a new asteroid at the requested position and give it motion.
        asteroid = Asteroid(position.x, position.y, radius)
        asteroid.velocity = velocity

    def update(self, dt: float) -> None:
        # Advance the timer and spawn a new asteroid when enough time has passed.
        self.spawn_timer += dt
        if self.spawn_timer > ASTEROID_SPAWN_RATE_SECONDS:
            self.spawn_timer = 0

            # Pick a random edge and use it to calculate the asteroid's starting
            # position and initial direction.
            edge = random.choice(self.edges)
            speed = random.randint(40, 100)
            velocity = edge[0] * speed
            velocity = velocity.rotate(random.randint(-30, 30))
            position = edge[1](random.uniform(0, 1))

            # Choose a random asteroid size variant.
            kind = random.randint(1, ASTEROID_KINDS)
            self.spawn(ASTEROID_MIN_RADIUS * kind, position, velocity)