import pygame
from custom_types import Display, Position, Colour
from particle import Particle

class Grid :
    def __init__(self, grid_size : int,
                 cell_size : int, cell_padding : int,
                 top_padding : int, left_padding : int,
                 empty_colour : Colour, sand_colour : Colour) :
        self.rows = grid_size[1]
        self.columns = grid_size[0]
        self.cell_size = cell_size
        self.cell_padding = cell_padding
        self.top_padding = top_padding
        self.left_padding = left_padding


        self.cells = [[None for _ in range(self.columns)] for _ in range(self.rows)]

        self.empty_colour = empty_colour
        self.sand_colour = sand_colour

    def draw(self, screen : Display) :
        for row in range(self.rows) :
            for column in range(self.columns) :
                colour = self.empty_colour
                particle = self.cells[row][column]
                if particle is not None :
                    colour = particle.get_colour()
                
                pygame.draw.rect(screen, colour, (column * (self.cell_size+self.cell_padding) + self.top_padding,
                                                         row * (self.cell_size+self.cell_padding) + self.left_padding,
                                                         self.cell_size,
                                                         self.cell_size))
                
    def get_cell(self, position : Position) -> Particle :
        return self.cells[position[1]][position[0]]
    
    def set_cell(self, position : Position, particle : Particle) :
        self.cells[position[1]][position[0]] = particle