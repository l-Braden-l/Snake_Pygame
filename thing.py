# Braden Leach
# April 22 2025
# Pygame Snake Game

import pygame
import random
import sys

# Initialize Pygame
pygame.init()
pygame.mixer.init()

# Window Parameters
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
CELL_SIZE = 10
TITLE = "Snake Game"

# Create window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(TITLE)

# Colors
BG = (255, 200, 150)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
BODY_INNER = (50, 175, 25)
BODY_OUTER = (10, 100, 200)
APPLE_COLOR = (255, 0, 0)

# Font
font = pygame.font.SysFont(None, 35)

# Music
try:
    pygame.mixer.music.load("C:\\Project-Text-Menu\\mixkit-infected-vibes-157.mp3")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)
except:
    print("Music file not found. Continuing without sound.")

# Snake Initial State
snake_pos = [
    [SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2],
    [SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + CELL_SIZE],
    [SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + CELL_SIZE * 2],
    [SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + CELL_SIZE * 3]
]
direction = 1  # 1 = Up, 2 = Right, 3 = Down, 4 = Left
score = 0

# Apple Position
apple_pos = [
    random.randint(0, (SCREEN_WIDTH // CELL_SIZE) - 1) * CELL_SIZE,
    random.randint(0, (SCREEN_HEIGHT // CELL_SIZE) - 1) * CELL_SIZE
]

# Draw Functions
def draw_screen():
    screen.fill(BG)

def draw_score():
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

def draw_apple():
    pygame.draw.rect(screen, APPLE_COLOR, (*apple_pos, CELL_SIZE, CELL_SIZE))

def draw_snake():
    for i, segment in enumerate(snake_pos):
        pygame.draw.rect(screen, BODY_OUTER, (*segment, CELL_SIZE, CELL_SIZE))
        if i == 0:
            pygame.draw.rect(screen, RED, (segment[0] + 1, segment[1] + 1, CELL_SIZE - 2, CELL_SIZE - 2))
        else:
            pygame.draw.rect(screen, BODY_INNER, (segment[0] + 1, segment[1] + 1, CELL_SIZE - 2, CELL_SIZE - 2))

# Main Loop
clock = pygame.time.Clock()
running = True
tick_count = 0

while running:
    draw_screen()
    draw_apple()
    draw_score()
    draw_snake()

    # Input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != 3:
                direction = 1
            elif event.key == pygame.K_RIGHT and direction != 4:
                direction = 2
            elif event.key == pygame.K_DOWN and direction != 1:
                direction = 3
            elif event.key == pygame.K_LEFT and direction != 2:
                direction = 4

    # Move snake every 100ms (roughly)
    tick_count += 1
    if tick_count > 10:
        tick_count = 0
        head_x, head_y = snake_pos[0]
        if direction == 1:
            head_y -= CELL_SIZE
        elif direction == 2:
            head_x += CELL_SIZE
        elif direction == 3:
            head_y += CELL_SIZE
        elif direction == 4:
            head_x -= CELL_SIZE

        new_head = [head_x, head_y]
        snake_pos.insert(0, new_head)

        # Apple collision
        if new_head == apple_pos:
            score += 1
            apple_pos = [
                random.randint(0, (SCREEN_WIDTH // CELL_SIZE) - 1) * CELL_SIZE,
                random.randint(0, (SCREEN_HEIGHT // CELL_SIZE) - 1) * CELL_SIZE
            ]
        else:
            snake_pos.pop()  # Remove tail unless growing

        # Wall collision
        if (head_x < 0 or head_x >= SCREEN_WIDTH or
            head_y < 0 or head_y >= SCREEN_HEIGHT):
            running = False

    pygame.display.flip()
    clock.tick(60)

# Quit
pygame.quit()
sys.exit()
