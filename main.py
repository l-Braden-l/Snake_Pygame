import pygame
import sys
import random

# Constants used throughout the game
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
TITLE = "Snake Game"
CELL_SIZE = 10 # Size of each cell in the grid (used for snake and apple)
BG = (255, 200, 150) # Background color (RGB format)
RED = (255, 0, 0) # Color for the snake's head
BLACK = (0, 0, 0) # Color for text (score display)
BODY_INNER = (50, 175, 25) # Inner color for snake body
BODY_OUTER = (100, 100, 200) # Outer color for snake body
APPLE_COLOR = (255, 0, 0)

FPS = 10 # Frames per second for game updates

def draw_snake(screen, snake_pos):
    """
    Draw the snake on the screen using the positions stored in snake_pos.
    Each segment of the snake is represented by a rectangle.
    The head of the snake is drawn in RED to distinguish it from the green body.
    """
    index = 0 # Used to differentiate the head (index 0) from the body (index > 0)
    for segment in snake_pos:
        # Draw the outer rectangle for each segment
        pygame.draw.rect(screen, BODY_OUTER, (segment[0], segment[1], CELL_SIZE, CELL_SIZE))
        if index == 0: # Head of the snake
            # Draw the inner rectangle with the head color (red)
            pygame.draw.rect(screen, RED, (segment[0] + 1, segment[1] + 1, CELL_SIZE - 2, CELL_SIZE - 2))
        else: # Body of the snake 
            # Draw the inner rectangle with the body color (green)
            pygame.draw.rect(screen, BODY_INNER, (segment[0] + 1, segment[1] + 1, CELL_SIZE - 2, CELL_SIZE - 2))

        index += 1

# Function to draw the apple on the screen
def draw_apple(screen, apple_pos):
   # The apple is a small rectangle placed at its position on the grid
   pygame.draw.rect(screen, APPLE_COLOR, (apple_pos[0], apple_pos[1], CELL_SIZE, CELL_SIZE))

# Function to draw the current score on the screen
def draw_score(screen, score, font):
    # Render the score text
    score_text = font.render(f"Score: {score}", True, BLACK)
    # Draw the score text at the top-left corner of the screen
    screen.blit(score_text, [10, 10])


# Main function to run the Snake game
def run_snake_game():
    # Initialize the game window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption(TITLE) # Set the title of the game window
    clock = pygame.time.Clock() # Create a clock object to control the frame rate

    direction = 1 # Initial direction of the snake (1=Up, 2=Right, 3=Down, 4=Left)
    score = 0 # Initialize the score
    snake_pos = [[int(SCREEN_WIDTH / 2), int(SCREEN_HEIGHT / 2)]] # Initial position of the snake's head
    # Add body segments to the snake
    snake_pos.extend([[int(SCREEN_WIDTH / 2), int(SCREEN_HEIGHT / 2) + CELL_SIZE * i] for i in range(1, 4)])
    apple_pos = [random.randint(0, SCREEN_WIDTH // CELL_SIZE - 1) * CELL_SIZE, random.randint(0, SCREEN_HEIGHT // CELL_SIZE - 1) * CELL_SIZE] # Random position for the apple
    font = pygame.font.SysFont(None, 35) # Font used for displaying the score

    try:
        # Attempt to load and play background music
        pygame.mixer.music.load('background_music.mp3')
        pygame.mixer.music.set_volume(0.5) # Set the music volume
        pygame.mixer.music.play(-1) # Play the music in a loop
    except pygame.error as e:

        # Handle the error if the background music file is not found or cannot be played
        print(f"Error loading or playing music in Snake game: {e}")

    running_game = True # Variable to control the main game loop
    while running_game:
        screen.fill(BG) # Fill the screen with the background color
        draw_apple(screen, apple_pos) # Draw the apple
        draw_score(screen, score, font) # Draw the score
        draw_snake(screen, snake_pos) # Draw the snake

        # Handle user input (keyboard events)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running_game = False # Exit the game if the user closes the window
            elif event.type == pygame.KEYDOWN:
                # Change the direction of the snake based on user input
                new_direction = direction
                if event.key == pygame.K_UP and direction != 3: new_direction = 1
                elif event.key == pygame.K_RIGHT and direction != 4: new_direction = 2
                elif event.key == pygame.K_DOWN and direction != 1: new_direction = 3
                elif event.key == pygame.K_LEFT and direction != 2: new_direction = 4
                direction = new_direction

        # Update the snake's position
        head_x, head_y = snake_pos[0] # Get the current position of the snake's head
        if direction == 1: head_y -= CELL_SIZE # Move up
        elif direction == 2: head_x += CELL_SIZE # Move right
        elif direction == 3: head_y += CELL_SIZE # Move down
        elif direction == 4: head_x -= CELL_SIZE # Move left

        snake_pos.insert(0, [head_x, head_y]) # Add the new head position to the snake

        # Check for collision between snake and apple
        if snake_pos[0] == apple_pos:
            while apple_pos in snake_pos:
                # Reposition the apple to a random location that is not inside the snake
                apple_pos = [random.randint(0, SCREEN_WIDTH // CELL_SIZE - 1) * CELL_SIZE, random.randint(0, SCREEN_HEIGHT // CELL_SIZE - 1) * CELL_SIZE]
            score += 1 # Increment the score
        else: 
            snake_pos.pop() # Remove the last segment of the snake

        # If the snake's head collides with the walls or itself, end the game
        if head_x < 0 or head_x >= SCREEN_WIDTH or head_y < 0 or head_y >= SCREEN_HEIGHT or snake_pos[0] in snake_pos[1:]:
            running_game = False # Exit the game loop
        
        pygame.display.flip() # Update the display
        clock.tick(FPS) # Limit frame rate to 10 updates per second

    pygame.mixer.music.stop() # Stop the background music

def main_menu():
    # Initialize the menu window
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Main Menu")
    font = pygame.font.SysFont("Arial", 40)
    button_color = (100, 100, 200)
    text_color = (255, 255, 255)
    
    # Define the "PLAY" button
    play_button_rect = pygame.Rect(0, screen_height // 3, 200, 50)
    play_button_rect.centerx = screen_width // 2 # Center the button horizontally
    play_text = font.render("PLAY", True, text_color) # Create the button text
    play_text_rect = play_text.get_rect(center=play_button_rect.center) # Center the text inside the button
   
    # Define the "EXIT" button
    exit_button_rect = pygame.Rect(0, screen_height // 2, 200, 50)
    exit_button_rect.centerx = screen_width // 2 # Center the button horizontally
    exit_button_rect.y = screen_height // 2 + 20 # Adjust vertical position
    exit_text = font.render("EXIT", True, text_color) # Create the button text
    exit_text_rect = exit_text.get_rect(center=exit_button_rect.center) # Center the text inside the button


    running_menu = True # Variable to control the menu loop
    while running_menu:
        screen.fill((50, 50, 50)) # Fill the screen with a dark background

        pygame.draw.rect(screen, button_color, play_button_rect) # Draw the "PLAY" button
        screen.blit(play_text, play_text_rect) # Draw the "PLAY" button text

        pygame.draw.rect(screen, button_color, exit_button_rect) # Draw the "EXIT" button
        screen.blit(exit_text, exit_text_rect) # Draw the "EXIT" button text

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running_menu = False # Exit the menu if the user closes the window
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: # Check for left mouse button click
                    mouse_pos = pygame.mouse.get_pos() # Get the position of the mouse click
                    if play_button_rect.collidepoint(mouse_pos): # Check if "PLAY" button was clicked
                        run_snake_game() # Start the Snake game
                    elif exit_button_rect.collidepoint(mouse_pos): # Check if "EXIT" button was clicked
                        running_menu = False # Exit the menu

        pygame.display.flip() # Update the display


    pygame.quit()
    sys.exit()



if __name__ == "__main__":
    pygame.init() # Initialize Pygame
    pygame.mixer.init() # Initialize Pygame mixer for audio
    main_menu()
