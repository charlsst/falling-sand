import random
from custom_types import Colour
from settings import Settings
from sand import update_sand

settings = Settings()
RANDOMISE_COLOURS = settings.RANDOMISE_PARTICLE_COLOUR

# [EMPTY, SAND]

EMPTY = 0
EMPTY_COLOUR = settings.PARTICLE_COLOURS[EMPTY]
EMPTY_COLOURS_MAP = [EMPTY_COLOUR for i in range(settings.GRID_SIZE[0]*settings.GRID_SIZE[1])]

SAND = 1
SAND_COLOUR = settings.PARTICLE_COLOURS[SAND]
SAND_COLOURS_MAP = [None for i in range(settings.GRID_SIZE[0]*settings.GRID_SIZE[1])]

COLOURS = [EMPTY_COLOUR, SAND_COLOUR]
COLOURS_MAP = [EMPTY_COLOURS_MAP, SAND_COLOURS_MAP]
UPDATES = [None, update_sand]

def set_colour(i : int, particle_id : int) :
    base_colour_rgb = COLOURS[particle_id]
    if RANDOMISE_COLOURS[particle_id] :
        grid_width = settings.GRID_SIZE[0]
        grid_height = settings.GRID_SIZE[1]

        x = i % grid_width
        y = i // grid_height

        rng = random.Random(x * 73856093 ^ y * 19349663)

        v = rng.randint(-10, 10)
        r = max(0, min(255, base_colour_rgb[0] + v))
        g = max(0, min(255, base_colour_rgb[1] + v))
        b = max(0, min(255, base_colour_rgb[2] + v))
        COLOURS_MAP[particle_id][i] = (r,g,b)
        return (r,g,b)
    else :
        COLOURS_MAP[particle_id][i] = base_colour_rgb
        return base_colour_rgb
    
if RANDOMISE_COLOURS[0] :
    for i in EMPTY_COLOURS_MAP :
        set_colour(i, 0)