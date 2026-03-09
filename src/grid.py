import pygame
from custom_types import Display, Position
from settings import Settings
from particle import SAND, COLOURS_MAP, UPDATES, set_colour

class Grid :
    def __init__(self, settings : Settings) :
        self.settings = settings
        self.grid_width = self.settings.GRID_SIZE[0]
        self.grid_height = self.settings.GRID_SIZE[1]
        self.cell_size = self.settings.CELL_SIZE
        self.cell_padding = self.settings.CELL_PADDING
        self.top_padding = self.settings.SCREEN_BORDER[0]
        self.left_padding = self.settings.SCREEN_BORDER[1]
    
        self.grid = [0 for _ in range(self.grid_width*self.grid_height)]

    # Updates every tile in the grid
    def update(self) :
        grid = self.grid
        grid_width = self.grid_width
        grid_height = self.grid_height

        for y in range(grid_height -2, -1, -1) :
            for x in range(grid_width) :
                particle = grid[x + (y * grid_width)]
                if particle != 0 :
                    new_position = UPDATES[SAND]((x, y), grid)
                    
                    if new_position != (x, y) :
                        self.set_cell(new_position, SAND)
                        self.set_cell((x, y), 0)

    def get_cell(self, position : Position) :
        return self.grid[position[0] + (position[1] * self.grid_width)]

    def set_cell(self, position : Position, particle_id : int) :
        if 0 <= position[0] < self.grid_width and 0 <= position[1] < self.grid_height :
            self.grid[position[0] + (position[1] * self.grid_width)] = particle_id

    # Draws the grid to the screen

    def draw(self, screen : Display) :
        grid = self.grid
        grid_width = self.grid_width
        grid_height = self.grid_height

        cell_padding = self.cell_padding
        cell_size = self.cell_size
        top_padding = self.top_padding
        left_padding = self.left_padding

        for y in range(grid_height) :
            for x in range(grid_width) :
                colour = COLOURS_MAP[0][x + (y * grid_width)]
                particle_id = grid[x + (y * grid_width)]
                if particle_id != 0 :
                    colour = COLOURS_MAP[particle_id][x + (y * grid_width)]
                    if colour is None :
                        colour = set_colour(x + (y * grid_width), particle_id)
                
                pygame.draw.rect(screen, colour, (x * (cell_size+cell_padding) + top_padding,
                                                  y * (cell_size+cell_padding) + left_padding,
                                                  cell_size,
                                                  cell_size))