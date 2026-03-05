import random
import colorsys
from custom_types import Position, Colour
from settings import Settings

settings = Settings()

class Particle :
    colour = (255, 255, 255)

    def __init__(self, do_randomise_colour=True) :
        self.colour = self.randomise_colour(self.colour)

    def get_colour(self) -> Colour :
        return self.colour

    def randomise_colour(self, base_colour_rgb : Colour) -> Colour :
        base_colour_hsv = colorsys.rgb_to_hsv(base_colour_rgb[0]/255, base_colour_rgb[1]/255, base_colour_rgb[2]/255)
        base_colour_hsv = (base_colour_hsv[0] + random.uniform(-0.01, 0.01),
                           base_colour_hsv[1] + random.uniform(-0.05, 0.05),
                           base_colour_hsv[2] + random.uniform(-0.05, 0.05))
        red, green, blue = colorsys.hsv_to_rgb(max(0, min(1, base_colour_hsv[0])),
                                               max(0, min(1, base_colour_hsv[1])),
                                               max(0, min(1, base_colour_hsv[2])))

        return int(red * 255), int(green * 255), int(blue * 255)
    
    def update(self, particle_position : Position) -> Position :
        print("Normal")
        return particle_position

class Sand(Particle) :
    colour = settings.SAND_COLOUR

    def update(self, particle_position) : print("Sand")