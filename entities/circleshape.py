import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    containers: tuple[pygame.sprite.Group, ...]

    def __init__(self, x: float, y: float, radius: float) -> None:
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(*self.containers)
        else:
            super().__init__()

        self.position: pygame.Vector2 = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen: pygame.Surface) -> None:
        # must override
        pygame.draw.circle(screen, "red", self.position, self.radius)

    def update(self, dt: float) -> None:
        # must override
        pass
    

    def collision_with(self,other):
        #steps:
        # 1. calculate distance between centers
        # 2. if the distance is less than the sum of the radii, then there is a collision
        # 3. return True or False
        distance = self.position.distance_to(other.position)
        return distance < self.radius + other.radius