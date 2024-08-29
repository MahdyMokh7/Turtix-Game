class Map:   # edit
    def __init__(self, map_text_files, level):
        self.map_text_files = map_text_files  # List of text files containing map data
        self.maap_text_base = self.load_map_data(level)  # 2D array representing the textual map
        self.maap_tile_base = self.convert_to_tiles(self.maap_text_base)  # 2D array representing the tile map
        self.level = level  # Current level of the map

    def load_map_data(self, level):
        """Loads the map data from the text file corresponding to the given level."""
        # Example logic to load map data from a file
        with open(self.map_text_files[level], 'r') as file:
            data = [line.strip() for line in file]
        # Convert the list of strings into a 2D array
        maap_text_base = [list(line) for line in data]
        return maap_text_base

    def convert_to_tiles(self, maap_text_base):
        """Converts the textual map base to a 2D array of tiles."""
        # This method would convert the characters in maap_text_base to actual tile objects
        # For simplicity, returning the same base map. Replace this with your actual tile conversion logic.
        maap_tile_base = [[self.char_to_tile(char) for char in row] for row in maap_text_base]
        return maap_tile_base

    def char_to_tile(self, char):
        """Converts a character from the map text base to a corresponding Tile object."""
        # Replace this with the actual logic to create Tile objects based on characters
        return char  # Placeholder return

    def initialize(self):
        """Initializes the map, loading any necessary resources or resetting state."""
        print(f"Initializing map for level {self.level}")

    def find_tile_by_pos(self, x_pos, y_pos):
        """Finds and returns the tile at the given x and y position."""
        row = y_pos // TILE_SIZE  # Assuming TILE_SIZE is a predefined constant
        col = x_pos // TILE_SIZE
        if 0 <= row < len(self.maap_tile_base) and 0 <= col < len(self.maap_tile_base[row]):
            return self.maap_tile_base[row][col]
        return None

    def render_all(self, screen):
        """Renders the entire map to the screen."""
        for row in self.maap_tile_base:
            for tile in row:
                if tile:
                    tile.render(screen)  # Assuming each tile has a render method

# Constants for the game
TILE_SIZE = 32  # Example tile size, can be changed based on the game's design
