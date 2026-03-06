import random
from custom_types import Position
from settings import Settings

settings = Settings()

def update_sand(particle_position: Position, grid: list[int]) -> Position:
    x, y = particle_position
    width = settings.GRID_SIZE[0]
    height = settings.GRID_SIZE[1]

    new_y = y + 1

    if new_y >= height:
        return (x, y)

    below = x + new_y * width

    if grid[below] == 0:
        return (x, new_y)
    
    if random.random() < 0.5:
        offsets = (-1, 1)
    else:
        offsets = (1, -1)

    for dx in offsets:
        nx = x + dx

        if 0 <= nx < width:
            idx = nx + new_y * width

            if grid[idx] == 0:
                return (nx, new_y)

    return (x, y)