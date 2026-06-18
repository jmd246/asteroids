import pygame
import sys
from entities.asteroid import Asteroid
from entities.shot import Shot
from util.logger import log_state, log_event
from util.constants import SCREEN_WIDTH, SCREEN_HEIGHT
from entities.player import Player
from entities.asteroid_field import AsteroidField
class GameManager:
    instance = None

    def __new__(cls):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance
    def __init__(self):
        self.is_running = True
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.delta_time = 0
    def stop(self):
        self.is_running = False
    def cleanup(self):
        pygame.quit()
        sys.exit(0)
    def process_events(self):
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
                self.stop()
    def start(self):
        self.is_running = True
        #define player
        updatable  = pygame.sprite.Group()
        drawable = pygame.sprite.Group()
        asteroids = pygame.sprite.Group()
        shots = pygame.sprite.Group()
        Player.containers = (updatable, drawable)
        Asteroid.containers = (asteroids,updatable, drawable)
        Shot.containers = (shots,updatable, drawable)
        AsteroidField.containers = (updatable)
        player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
        asteroid_field = AsteroidField()
        screen = self.screen
      
        try:
            while self.is_running:
                log_state()
                self.delta_time = self.clock.tick(60)/1000
                self.process_events()
                screen.fill("black")
                updatable.update(self.delta_time)

                for asteroid in asteroids:
                    if asteroid.collision_with(player):
                        log_event("player_hit")
                        print("Game over!")
                        self.stop()
                        self.cleanup()
                        sys.exit(0)
                    for shot in shots:
                        if shot.collision_with(asteroid):
                            log_event("asteroid_shot")
                            asteroid.split()
                            shot.kill()

                for entity in drawable:
                    entity.draw(screen)
                pygame.display.flip()
            self.cleanup()
        except KeyboardInterrupt as e:
            print(e)
            self.cleanup()