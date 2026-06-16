import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    #init pygame
    pygame.init()
    # window for game
    screen  = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    is_running  = True
    while is_running  :
        log_state()
        #event processing
        for event in pygame.event.get():
            #pass for now   
            if event.type == pygame.QUIT:
                is_running = False
        screen.fill("black")
        pygame.display.flip()

if __name__ == "__main__":
    main()
