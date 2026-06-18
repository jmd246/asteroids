from entities.circleshape import CircleShape
from entities.shot import Shot
from util.constants import LINE_WIDTH, PLAYER_SHOOT_COOLDOWN_SECONDS, PLAYER_SHOOT_SPEED, SCREEN_WIDTH, SCREEN_HEIGHT, PLAYER_RADIUS, PLAYER_TURN_SPEED
import pygame
class Player (CircleShape):
    def __init__(self, x_pos:float, y_pos:float) -> None : 
        self.rotation = 0
        super().__init__(x_pos, y_pos, PLAYER_RADIUS)
        self.player_shoot_cooldown = 0
    

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
        pygame.draw.polygon(screen, "white", self.triangle(), LINE_WIDTH)
    def shoot(self)-> None:
        #check cooldown
        #if on cooldown return
        if self.player_shoot_cooldown > 0:
            return
        #not on cooldown
        #set cooldown
        self.player_shoot_cooldown =PLAYER_SHOOT_COOLDOWN_SECONDS
        #generate bullet
        bullet = Shot(self.position.x, self.position.y, 5)
        bullet.velocity = pygame.Vector2(0,1).rotate(self.rotation)
        bullet.velocity *= PLAYER_SHOOT_SPEED

    def player_controls(self,dt:float) -> None:
        keys = pygame.key.get_pressed()    
        if keys[pygame.K_a]:
            self.rotate(-dt)
        elif keys[pygame.K_d]:
            self.rotate(dt)
        elif keys[pygame.K_w]:
            self.move(-dt)
        elif keys[pygame.K_s]:
            self.move(dt)
        elif keys[pygame.K_SPACE]or keys[pygame.K_k]:
            self.shoot()

    def update(self, dt:float) -> None:
       #decrease cooldown
       self.player_shoot_cooldown -= dt
       self.player_controls(dt)
        

        