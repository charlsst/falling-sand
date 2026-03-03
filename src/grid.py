import pygame
from settings import Settings

class Grid :
    def __init__(self, grid_size, cell_size, cell_padding, empty_colour) :
        self.rows = grid_size[1] // cell_size
        self.columns = grid_size[0] // cell_size
        self.cell_size = cell_size
        self.cell_padding = cell_padding
        self.cells = [[None for _ in range(self.columns)] for _ in range(self.rows)]

        self.empty_colour = empty_colour

    def draw(self, screen) :
        for row in range(self.rows) :
            for column in range(self.columns) :
                pygame.draw.rect(screen, self.empty_colour, (column * (self.cell_size+self.cell_padding),
                                                         row * (self.cell_size+self.cell_padding),
                                                         self.cell_size,
                                                         self.cell_size))
                