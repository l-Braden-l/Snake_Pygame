#Braden Leach
#April 22 2025
#Pygame Snake Game

# -- Imports -- # 
import pygame 
import random 
import sys
from pygame.locals import *

# -- Intilizers -- #
pygame.init()
pygame.mixer.init()

# -- Window Parameters -- # 
SCREEN_HEIGHT = 800
SCREEN_WIDTH = 600
TITLE = "Snake Game"

# -- Create Game Window -- # 
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(TITLE)

# -- Game Variables and Constants -- # 
CELL_SIZE = 10 
direction = 1 # - 1 is up, 2 is right, 3 is down, 4 is left
update_snake = 0 
score = 0 # - Init Score

# -- Base Snake -- #
snake_pos = [[int(SCREEN_WIDTH / 2), int(SCREEN_HEIGHT / 2)]] # - Snake Head
snake_pos.append([int(SCREEN_WIDTH / 2), int(SCREEN_HEIGHT / 2) + CELL_SIZE]) # - Body Segment
snake_pos.append([int(SCREEN_WIDTH / 2), int(SCREEN_HEIGHT / 2) + CELL_SIZE * 2]) # - Body Segment
snake_pos.append([int(SCREEN_WIDTH / 2), int(SCREEN_HEIGHT / 2) + CELL_SIZE * 3]) # - Body Segment

# -- Constant Colors -- #
BG = (255, 200, 150)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
BODY_INNER = (50, 175, 25)
BODY_OUTER = (10, 100, 200)
APPLE_COLOR = (255, 0, 0)

# -- Define Apple Position -- # 
apple_pos = [random.randint(0, SCREEN_WIDTH // CELL_SIZE - 1) * CELL_SIZE, random.randint(0, SCREEN_HEIGHT // CELL_SIZE - 1) * CELL_SIZE]

# -- Font for Score -- # 
font = pygame.font.SysFont(None, 35)

# -- Load and Play Background Music -- # 
pygame.mixer.music.load("C:\Project-Text-Menu\mixkit-infected-vibes-157.mp3") # - Loads Music
pygame.mixer.music.set_volume(0.5) # - Set volume to 50%
pygame.mixer.music.play(-1) # - Plays Music in Loop


# -- Draw Screen Function -- #
def draw_screen(): 
    screen.fill(BG)


# -- Draw Apple Function -- # 
def draw_apple(): 
    pygame.draw.rect(screen, APPLE_COLOR, (apple_pos[0], apple_pos[1], CELL_SIZE, CELL_SIZE))


# -- Draw Score Function -- # 
def draw_score():
    score_text = font.render(f'Score: {score}', True, BLACK)
    screen.blit(score_text, [10, 10])

running = True 
while running:
    draw_screen()
    draw_apple()
    draw_score()

    # -- Loop Through Events -- # 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != 3: # - Up
                direction = 1
            elif event.key == pygame.K_RIGHT and direction != 4: # - Right
                direction = 2
            elif event.key == pygame.K_DOWN and direction != 1: # - Down
                direction = 3
            elif event.key == pygame.K_LEFT and direction != 2: # - Left 
                direction = 4
    # -- Add Timer -- # 
    if update_snake > 99: 
        update_snake = 0 

        # -- Move The Snake -- # 
        head_x, head_y = snake_pos[0]

        if direction == 1: # - Up 
            head_y -= CELL_SIZE
        elif direction == 2: # - Right  
            head_x += CELL_SIZE
        elif direction == 3: # - Down
            head_y += CELL_SIZE
        elif direction == 2: # - Left  
            head_x -= CELL_SIZE

        # -- Update Snake Position -- # 
        snake_pos.insert(0, [head_x, head_y]) # - Add New Head 
        snake_pos.pop() # - Remove Last Segment 

        # -- Check For Collision (Apple) -- # 
        if snake_pos[0] == apple_pos: 
            apple_pos[random.randint(0, SCREEN_WIDTH // CELL_SIZE - 1) * CELL_SIZE, random.randint(0, SCREEN_HEIGHT // CELL_SIZE - 1)]
            snake_pos.append(snake_pos[-1]) # -  Add New Segment to Snake 
            score += 1  # - Increase Score When Apple Eaten 
        
        # -- Check for Collision (Walls) -- #
        if head_x < 0 or head_x >= SCREEN_WIDTH or head_y < 0 or head_y >= SCREEN_HEIGHT: 
            running = False # - Exit game 

        # -- Draw Snake -- # 
        for i in range(len(snake_pos)): 
            segment = snake_pos[i]
            if i == 0: # - Head 
                pygame.draw.rect(screen, BODY_OUTER, (segment[0], segment[1], CELL_SIZE, CELL_SIZE))
                pygame.draw.rect(screen, RED, (segment[0] + 1, segment[1] + 1, CELL_SIZE - 2, CELL_SIZE - 2))
            else: # - Body 
                pygame.draw.rect(screen, BODY_OUTER, (segment[0], segment[1], CELL_SIZE, CELL_SIZE))
                pygame.draw.rect(screen, BODY_INNER, (segment[0] + 1, segment[1] + 1, CELL_SIZE - 2, CELL_SIZE - 2))

        # -- Update Display -- # 
        pygame.display.flip()

        update_snake += 1 

# -- Exit Pygame -- # 
pygame.quit()
sys.exit()

        
        
