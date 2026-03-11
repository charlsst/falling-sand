import pygame
from custom_types import Display, Position
from settings import Settings
from particle import COLOURS_MAP, UPDATES, set_colour

class Grid :
    def __init__(self, settings : Settings) :
        self.settings = settings
        self.grid_width = self.settings.GRID_SIZE[0]
        self.grid_height = self.settings.GRID_SIZE[1]
        self.cell_size = self.settings.CELL_SIZE
        self.cell_padding = self.settings.CELL_PADDING
        self.top_padding = self.settings.SCREEN_BORDER[0]
        self.left_padding = self.settings.SCREEN_BORDER[1]
        self.scan_left = True
    
        self.grid = [0 for _ in range(self.grid_width*self.grid_height)]
        self.active_cells = []
        self.next_active_cells = []

    # Updates every tile in the grid
    def update(self) :
        grid = self.grid
        grid_width = self.grid_width
        self.next_active_cells = []
        for i in self.active_cells :
            particle = grid[i]
            if UPDATES[particle] is not None :
                y = i // grid_width
                x = i - y * grid_width
                new_positions = UPDATES[particle]((x, y), grid)
                for new_position in new_positions :
                    self.set_cell(new_position[0], new_position[1])
                    if new_position[1] != 0 and i not in self.next_active_cells :
                        self.next_active_cells.append(i)
        self.active_cells = self.next_active_cells

    def get_cell(self, position : Position) :
        return self.grid[position[0] + (position[1] * self.grid_width)]

    def set_cell(self, position : Position, particle_id : int) :
        x = position[0]
        y = position[1]
        if 0 <= x < self.grid_width and 0 <= y < self.grid_height :
            i = x + (y * self.grid_width)
            self.grid[i] = particle_id

            if particle_id != 0 and i not in self.next_active_cells :
                self.next_active_cells.append(i)

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