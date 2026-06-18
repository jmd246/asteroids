import pygame
import sys
from util.logger import log_state
from util.constants import SCREEN_WIDTH, SCREEN_HEIGHT
from entities.player import Player
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
        Player.containers = (updatable, drawable)
        player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
        screen = self.screen
      
        try:
            while self.is_running:
                log_state()
                self.delta_time = self.clock.tick(60)/1000
                self.process_events()
                screen.fill("black")
                updatable.update(self.delta_time)
                for entity in drawable:
                    entity.draw(screen)
                pygame.display.flip()
            self.cleanup()
        except KeyboardInterrupt as e:
            print(e)
            self.cleanup()