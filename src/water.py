import random
from custom_types import Position
from settings import Settings

settings = Settings()

EMPTY = 0
WATER = 3

# Fill with IDs of particles to replace when falling
ignore_list = [EMPTY]

# Returns a list of tuples: ((x, y), particle_id) in case you want particles to change many adjacent spaces at once.
def update_water(particle_position: Position, grid: list[int]) -> list[tuple[Position, int]]:
    x, y = particle_position
    width = settings.GRID_SIZE[0]
    height = settings.GRID_SIZE[1]

    new_y = y + 1

    if new_y >= height :
        return [((x, y), WATER)]

    below = x + new_y * width

    if grid[below] in ignore_list:
        return [((x, new_y), WATER), ((x, y), grid[below])]
    
    if random.random() < 0.5:
        offsets = (-1, 1)
    else:
        offsets = (1, -1)

    for dx in offsets :
        nx = x + dx

        if 0 <= nx < width :
            idx = nx + new_y * width
            above_idx = nx + y * width

            if grid[idx] in ignore_list and grid[above_idx] in ignore_list:
                return [((nx, new_y), WATER), ((x, y), grid[idx])]
            
            if grid[above_idx] in ignore_list:
                return [((nx, y), WATER), ((x, y), grid[above_idx])]

    return [((x, y), WATER)]