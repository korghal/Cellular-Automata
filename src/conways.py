import pygame, random
 
# Define some colors and other constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (25, 25, 25)
WIN_SIZE = 500

cur_states = [0] * 400
cur_states[9] = 1
cur_states[10] = 1
cur_states[29] = 1
cur_states[30] = 1

next_states = []

pygame.init()

# Set the width and height of the screen [width, height]
size = (WIN_SIZE, WIN_SIZE)
screen = pygame.display.set_mode(size)


# Add a title
pygame.display.set_caption("Conway's Game of Life")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 

# Conway GOL Update
def getNumNeighbors(cur_index):
    '''
    We need to check....
    The grid is setup as a one dimensional array.
    With the current state of the code it calculates in the Y direction before looping back to the top of the screen.
    ____|||||||||||||| Indexes
        0, 20, 40, 60, 80, 100, 120, 140
        1, 21,
        2, 22,
        3
        4
        5
        6
        7
        8
        9,  29, 49,
        10, 30, 50, 70, 90, 110, 130, 150 ->
        11, 31, 51,
        12
        13
        14
        15
        16
        17
        18
        19

        cur_index-1 is North
        cur_index+1 is South
        cur_index-20 is West
        cur_index+20 is East
        cur_index-21 is Northwest
        cur_index+19 is Northeast
        cur_index-19 is Southwest
        cur_index+21 is Southeast
        
    '''
    # Get the 'cardinal directions' of the neighbors based off our cur_index
    neighbors = 0
    cardinalDirections = {
        'north': -1,
        'south': -1,
        'west': -20,
        'east': 20,
        'nw': -21,
        'ne': 19,
        'sw': -19,
        'se': 21
    }
    
    for direction in cardinalDirections:
        if cur_index - cardinalDirections[direction] >= 0 and cur_index - cardinalDirections[direction] <= len(cur_states)-1:
            if cur_states[cur_index - cardinalDirections[direction]] == 1:
                neighbors += 1

    return neighbors

def updateState():
    copy_states = cur_states[:]
    for cur_index in range(len(cur_states)):
        #print(f'neighbors for cell {cur_index} : {getNumNeighbors(cur_index)}')
        neighbors = getNumNeighbors(cur_index)
        if neighbors == 3:
            # Birth
            copy_states[cur_index] = 1
        elif neighbors == 1 or neighbors >= 4:
            # Death
            copy_states[cur_index] = 0
    return copy_states

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    print(getNumNeighbors(30))
    # --- Game logic should go here
    cur_states = updateState()

    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to gray. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(GRAY)
 
    # --- Drawing code should go here
    x = 5
    cur_index = 0
    while x < WIN_SIZE:
        y = 5
        while y < WIN_SIZE:
            
            state = cur_states[cur_index]
            if state == 0:
                pygame.draw.rect(screen, BLACK, pygame.Rect(x, y, 20, 20))
            else:
                pygame.draw.rect(screen, WHITE, pygame.Rect(x, y, 20, 20))
            y += 25
            cur_index += 1
        x += 25

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 5 frames per second
    clock.tick(5)
 
# Close the window and quit.
pygame.quit()
