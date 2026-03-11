from config_loader import load_config

class Settings :

    def __init__(self) :
        config_data = load_config()

        try :
            self.BACKGROUND_COLOUR = config_data["background_colour"]
            self.PARTICLE_COLOURS = config_data["particle_colours"]
            self.RANDOMISE_PARTICLE_COLOUR = config_data["randomise_particle_colour"]
            self.SCREEN_TITLE = config_data["screen_title"]
            self.GRID_SIZE = config_data["grid_size"]
            self.CELL_SIZE = config_data["cell_size"]
            self.CELL_PADDING = config_data["cell_padding"]
            self.SCREEN_BORDER = config_data["screen_border"]
            self.TARGET_FPS = config_data["target_fps"]
        except KeyError as e :
            raise KeyError(f"Missing config key for settings initialisation: {e.args[0]}")

        self.validate()
    
    def validate(self) :
        # Validate all colours
        for colour in self.PARTICLE_COLOURS :
            if not isinstance(colour, list) or len(colour) != 3:
                raise ValueError("Colours must be a list of length 3.")
            else :
                for num in colour :
                    if num < 0 or num > 255 :
                        raise ValueError("Colours must contain integers from 0-255.")

        # Validate randomise particle colour
        for val in self.RANDOMISE_PARTICLE_COLOUR :
            if isinstance(val, bool) :
                if len(self.RANDOMISE_PARTICLE_COLOUR) != len(self.PARTICLE_COLOURS) :
                    raise ValueError("Randomise colours must contain enough booleans for each colour.")
            else :
                raise ValueError("Randomise colours must contain only booleans.")

        # Validate SCREEN_TITLE
        if not isinstance(self.SCREEN_TITLE, str) :
            raise ValueError("SCREEN_TITLE must be a string.")

        # Validate GRID_SIZE
        if not isinstance(self.GRID_SIZE, list) or len(self.GRID_SIZE) != 2:
            raise ValueError("GRID_SIZE must be a list of length 2.")
        for x in self.GRID_SIZE :
            if not isinstance(x, int) or x < 0 :
                raise ValueError("GRID_SIZE values must be non-negative integers.")

        # Validate CELL_SIZE
        if not isinstance(self.CELL_SIZE, int) or self.CELL_SIZE < 0:
            raise ValueError("CELL_SIZE must be a non-negative integer.")

        # Validate CELL_PADDING
        if not isinstance(self.CELL_PADDING, int) or self.CELL_PADDING < 0:
            raise ValueError("CELL_PADDING must be a non-negative integer.")

        # Validate SCREEN_BORDER
        if not isinstance(self.SCREEN_BORDER, list):
            raise ValueError("SCREEN_BORDER must be a list.")
        for edge in self.SCREEN_BORDER :
            if not isinstance(edge, int) or edge < 0 :
                raise ValueError("SCREEN_BORDER values must be non-negative integers.")
        
        # Validate TARGET_FPS
        if not isinstance(self.TARGET_FPS, int) or self.TARGET_FPS < 0:
            raise ValueError("TARGET_FPS must be a non-negative integer.")