import pygame

# Screen resolution is 1280x720. 
# Using 5x5 blocks gives us a 256x144 physics simulation grid.
GRID_WIDTH = 256   # 1280 / 5
GRID_HEIGHT = 144  # 720 / 5
BLOCK_SIZE = 5

class SandManager:
    def __init__(self):
        # Create a grid where None is empty air, and a tuple (R,G,B) is sand
        self.grid = [[None for _ in range(GRID_HEIGHT)] for _ in range(GRID_WIDTH)]
        self.frame_count = 0

    def add_rect(self, color, mouse_x, mouse_y):
        """Converts mouse pixels into grid index coordinates and places sand."""
        grid_x = mouse_x // BLOCK_SIZE
        grid_y = mouse_y // BLOCK_SIZE

        # Ensure placement coordinates are within our array boundaries
        if 0 <= grid_x < GRID_WIDTH and 0 <= grid_y < GRID_HEIGHT:
            self.grid[grid_x][grid_y] = color

    def update_physics(self):
        """Processes the falling behavior. Loops backwards through Y rows."""
        # Start at row before bottom (HEIGHT - 2) and move up to 0 (-1)
        for y in range(GRID_HEIGHT - 2, -1, -1):
            for x in range(GRID_WIDTH):
                
                # Check if there is sand occupying this cell
                if self.grid[x][y] is not None:
                    color = self.grid[x][y]

                    # 1. Check straight down
                    if self.grid[x][y + 1] is None:
                        self.grid[x][y + 1] = color
                        self.grid[x][y] = None
                    
                    # 2. Check down-left diagonal
                    elif x > 0 and self.grid[x - 1][y + 1] is None:
                        self.grid[x - 1][y + 1] = color
                        self.grid[x][y] = None
                        
                    # 3. Check down-right diagonal
                    elif x < GRID_WIDTH - 1 and self.grid[x + 1][y + 1] is None:
                        self.grid[x + 1][y + 1] = color
                        self.grid[x][y] = None

    def draw_all(self, surface):
        """Iterates through active cells and draws them back as screen blocks."""
        for x in range(GRID_WIDTH):
            for y in range(GRID_HEIGHT):
                if self.grid[x][y] is not None:
                    pygame.draw.rect(
                        surface, 
                        self.grid[x][y], 
                        (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)
                    )