import pygame
import sys
from settings import Settings
from grid import Grid
from particle import SAND

def main() :
    settings = Settings()

    screen = pygame.display.set_mode(((settings.GRID_SIZE[0] * (settings.CELL_SIZE + settings.CELL_PADDING)) + settings.SCREEN_BORDER[1] + settings.SCREEN_BORDER[3] - settings.CELL_PADDING,
                                      (settings.GRID_SIZE[1] * (settings.CELL_SIZE + settings.CELL_PADDING)) + settings.SCREEN_BORDER[0] + settings.SCREEN_BORDER[2] - settings.CELL_PADDING))
    pygame.display.set_caption(settings.SCREEN_TITLE)

    clock = pygame.time.Clock()
    grid = Grid(settings)

    while True: 
        # Read Events 
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Update Simulation
        grid.update()
        
        # Check for Inputs
        buttons = pygame.mouse.get_pressed()
        if buttons[0] :
            mouse_position = pygame.mouse.get_pos()
            mouse_x = (mouse_position[0] - settings.SCREEN_BORDER[1]) // (settings.CELL_SIZE + settings.CELL_PADDING)
            mouse_y = (mouse_position[1] - settings.SCREEN_BORDER[0]) // (settings.CELL_SIZE + settings.CELL_PADDING)
            grid.set_cell((mouse_x, mouse_y), SAND)
        

        # Draw Graphics
        screen.fill(settings.BACKGROUND_COLOUR)
        grid.draw(screen)

        # Final Changes
        pygame.display.flip()
        clock.tick(120)
    
if __name__ == "__main__" :
    main()