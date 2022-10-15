import pygame

WINDOW_SIZE = [750, 750]  # TODO create a dynamic way of arranging window size right now it is not one to one with grid size

GRID_SIZE = 30

# Cell Properties
WIDTH = 20
HEIGHT = 20
MARGIN = 5

# Color Codes
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

grid = []

def init_grid(grid, size):
    for row in range(size):
        # Add an empty array that will hold each cell
        # in this row
        grid.append([])
        for column in range(size):
            grid[row].append(0)  # Append a cell


def update_rect_mouse_input(screen, color, pos):
    column = pos[0] // (WIDTH + MARGIN)
    row = pos[1] // (HEIGHT + MARGIN)

    if grid[row][column] != 1:
        grid[row][column] = 1
        # add if color is not already green
        rect = pygame.Rect(((MARGIN + WIDTH) * column + MARGIN,
                            (MARGIN + HEIGHT) * row + MARGIN),
                           (WIDTH, HEIGHT))
        pygame.draw.rect(screen,
                         color, rect)
        pygame.display.update(rect)


def update_grid():
    # Set the screen background
    screen.fill(BLACK)
    # Draw the grid
    for row in range(GRID_SIZE):
        for column in range(GRID_SIZE):
            color = BLACK
            if grid[row][column] == 1:
                color = GREEN
            pygame.draw.rect(screen,
                             color,
                             [(MARGIN + WIDTH) * column + MARGIN,
                              (MARGIN + HEIGHT) * row + MARGIN,
                              WIDTH,
                              HEIGHT])
    pygame.display.update()

def get_neighbour_count(row,col):
    count = 0
    for neigh_row in range(row - 1,row + 2):
        for neigh_col in range(col - 1, col + 2):
            if neigh_row != row or neigh_col != col:
                if neigh_row >= 0 and neigh_row < GRID_SIZE and neigh_col >= 0 and neigh_col < GRID_SIZE and  grid[neigh_row][neigh_col] == 1:
                    count += 1
    return count

def simulation_loop():
    done = False
    end_sim = False
    while not done and not end_sim:
        for event in pygame.event.get():  # User did something
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_x:
                    end_sim = True
            elif event.type == pygame.QUIT:  # If user clicked close
                done = True  # Flag that we are done so we exit this loop

        neighbour_count_grid = []
        for row in range(GRID_SIZE):
            neighbour_count_grid.append([])
            for col in range(GRID_SIZE):
                neighbour_count_grid[row].append(get_neighbour_count(row,col))

        for row in range(GRID_SIZE):
            for col in range(GRID_SIZE):
                if grid[row][col] == 1 and neighbour_count_grid[row][col] != 3 and neighbour_count_grid[row][col] != 2:
                    grid[row][col] = 0
                elif grid[row][col] == 0 and neighbour_count_grid[row][col] == 3:
                    grid[row][col] = 1
        update_grid()

        clock.tick(10)
    return done
if __name__ == '__main__':

    init_grid(grid, GRID_SIZE)

    pygame.init()

    screen = pygame.display.set_mode(WINDOW_SIZE)

    pygame.display.set_caption("Game Of Life")

    # Loop until the user clicks the close button.
    done = False

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    # -------- Main Program Loop -----------
    myfont = pygame.font.SysFont('Comic Sans MS', 30)
    textsurface = myfont.render('Press X to change between simulation and drawing.', False, WHITE)

    screen.blit(textsurface, (0, 0))#print at the middle
    pygame.display.update()
    has_text = True

    mouse_down = False
    while not done:
        for event in pygame.event.get():  # User did something
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_x:
                    done = simulation_loop()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if has_text:
                    screen.fill(BLACK)
                    pygame.display.update()
                    has_text = False

                mouse_down = True
                update_rect_mouse_input(screen, GREEN, pygame.mouse.get_pos())

            elif event.type == pygame.MOUSEBUTTONUP:
                mouse_down = False

            elif event.type == pygame.MOUSEMOTION:
                if mouse_down:
                    update_rect_mouse_input(screen, GREEN, pygame.mouse.get_pos())

            elif event.type == pygame.QUIT:  # If user clicked close
                done = True  # Flag that we are done so we exit this loop

        clock.tick(60)

    pygame.quit()
