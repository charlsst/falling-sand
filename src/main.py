import pygame
from settings import Settings
from grid import Grid

def main() :
    settings = Settings()

    screen = pygame.display.set_mode(settings.SCREEN_SIZE)
    pygame.display.set_caption(settings.SCREEN_TITLE)

    clock = pygame.time.Clock()

    grid = Grid(settings.SCREEN_SIZE, settings.CELL_SIZE, settings.CELL_PADDING, settings.EMPTY_COLOUR)

    running = True

    while running: 
        # Read Events #
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                running = False
        
        # Draw Graphics #
        screen.fill(settings.BACKGROUND_COLOUR)
        grid.draw(screen)

        # Final Changes #
        pygame.display.flip()
        clock.tick()
    
if __name__ == "__main__" :
    main()