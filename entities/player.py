from entities.circleshape import CircleShape
from util.constants import SCREEN_WIDTH, SCREEN_HEIGHT, PLAYER_RADIUS, PLAYER_TURN_SPEED
import pygame
class Player (CircleShape):
    def __init__(self, x_pos:float, y_pos:float) -> None : 
        self.rotation = 0
        super().__init__(x_pos, y_pos, PLAYER_RADIUS)

    def triangle(self) ->  list[pygame.Vector2]:
        # must override with current position
        forward = pygame.Vector2(0,1).rotate(self.rotation )
        right =  pygame.Vector2(0,1).rotate(self.rotation + 90) * self.radius/1.5
        #create triangle
        #a is 
        a = self.position - forward * self.radius
        b = self.position + forward * self.radius-right
        c = self.position + forward * self.radius+right
        return [a,b,c]
    
    def rotate(self, dt:float) -> None:
        self.rotation += PLAYER_TURN_SPEED * dt
    def move(self, dt:float) -> None:
        #update position
        #start with unit vector pointing forward
        unit_vector = pygame.Vector2(0,1)
        #rotate so it points in the direction we are moving
        rotated_vector = unit_vector.rotate(self.rotation)
        #update position
        updated_position = rotated_vector * PLAYER_TURN_SPEED * dt
        #add to current position
        self.position += updated_position
    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.polygon(screen, "white", self.triangle())

    def update(self, dt:float) -> None:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(-dt)
        if keys[pygame.K_s]:
            self.move(dt)
        

        