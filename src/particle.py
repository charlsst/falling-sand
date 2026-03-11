import random
from settings import Settings
from sand import update_sand
from water import update_water

settings = Settings()
RANDOMISE_COLOURS = settings.RANDOMISE_PARTICLE_COLOUR

# [EMPTY, SAND, ROCK]

EMPTY = 0
EMPTY_COLOUR = settings.PARTICLE_COLOURS[EMPTY]
EMPTY_COLOURS_MAP = [None for i in range(settings.GRID_SIZE[0]*settings.GRID_SIZE[1])]

SAND = 1
SAND_COLOUR = settings.PARTICLE_COLOURS[SAND]
SAND_COLOURS_MAP = [None for i in range(settings.GRID_SIZE[0]*settings.GRID_SIZE[1])]

ROCK = 2
ROCK_COLOUR = settings.PARTICLE_COLOURS[ROCK]
ROCK_COLOURS_MAP = [None for i in range(settings.GRID_SIZE[0]*settings.GRID_SIZE[1])]

WATER = 3
WATER_COLOUR = settings.PARTICLE_COLOURS[WATER]
WATER_COLOURS_MAP = [None for i in range(settings.GRID_SIZE[0]*settings.GRID_SIZE[1])]

COLOURS = [EMPTY_COLOUR, SAND_COLOUR, ROCK_COLOUR, WATER_COLOUR]
COLOURS_MAP = [EMPTY_COLOURS_MAP, SAND_COLOURS_MAP, ROCK_COLOURS_MAP, WATER_COLOURS_MAP]
UPDATES = [None, update_sand, None, update_water]

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
else :
    EMPTY_COLOURS_MAP = [EMPTY_COLOUR for i in range(settings.GRID_SIZE[0]*settings.GRID_SIZE[1])]
    COLOURS_MAP[0] = EMPTY_COLOURS_MAP