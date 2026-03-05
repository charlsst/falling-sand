from custom_types import Display, Grid_Size, Position
from grid import Grid
from settings import Settings
from particle import Particle

class Simulation :
    def __init__(self, settings : Settings) :
        self.settings = settings
        self.grid = Grid(self.settings.GRID_SIZE,
                         self.settings.CELL_SIZE,
                         self.settings.CELL_PADDING,
                         self.settings.SCREEN_BORDER[0],
                         self.settings.SCREEN_BORDER[1],
                         self.settings.EMPTY_COLOUR,
                         self.settings.SAND_COLOUR)
    
    def draw(self, screen : Display) :
        self.grid.draw(screen)

    def get_grid_cell(self, position : Position) :
        return self.grid.get_cell(position)

    def add_particle(self, position : Position, particle : Particle) :
        if 0 <= position[0] < self.settings.GRID_SIZE[0] and 0 <= position[1] < self.settings.GRID_SIZE[1] :
            self.grid.set_cell((position[0], position[1]), particle)
            particle.update(position)

    def delete_particle(self, position : Position) :
        if 0 <= position[0] < self.settings.GRID_SIZE[0] and 0 <= position[1] < self.settings.GRID_SIZE[1] :
            self.grid.set_cell((position[0], position[1]), None)