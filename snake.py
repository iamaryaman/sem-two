import sys
import random

try:
    import pygame
except ModuleNotFoundError:
    print("Pygame is not installed. Please install it using 'pip install pygame'")
    sys.exit()

pygame.init()

WIDTH, HEIGHT = 500, 500
GRID_SIZE = 20
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Create game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()

# Snake and Food
snake = [(100, 100), (90, 100), (80, 100)]  # Initial snake position
snake_dir = (GRID_SIZE, 0)  # Initial direction (moving right)
food = (random.randint(0, WIDTH // GRID_SIZE - 1) * GRID_SIZE,
        random.randint(0, HEIGHT // GRID_SIZE - 1) * GRID_SIZE)

def draw_snake():
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (segment[0], segment[1], GRID_SIZE, GRID_SIZE))

def draw_food():
    pygame.draw.rect(screen, RED, (food[0], food[1], GRID_SIZE, GRID_SIZE))

def move_snake():
    global food
    new_head = (snake[0][0] + snake_dir[0], snake[0][1] + snake_dir[1])
    
    #wall
    if (new_head[0] < 0 or new_head[0] >= WIDTH or
        new_head[1] < 0 or new_head[1] >= HEIGHT or
        new_head in snake):
        return False  
    
    snake.insert(0, new_head)
    
    # Check if snake eats food
    if new_head == food:
        food = (random.randint(0, WIDTH // GRID_SIZE - 1) * GRID_SIZE,
                random.randint(0, HEIGHT // GRID_SIZE - 1) * GRID_SIZE)
    else:
        snake.pop()
    
    return True  # Game continues

# Main loop
running = True
while running:
    screen.fill(BLACK)
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_dir != (0, GRID_SIZE):
                snake_dir = (0, -GRID_SIZE)
            elif event.key == pygame.K_DOWN and snake_dir != (0, -GRID_SIZE):
                snake_dir = (0, GRID_SIZE)
            elif event.key == pygame.K_LEFT and snake_dir != (GRID_SIZE, 0):
                snake_dir = (-GRID_SIZE, 0)
            elif event.key == pygame.K_RIGHT and snake_dir != (-GRID_SIZE, 0):
                snake_dir = (GRID_SIZE, 0)
    
    # Move snake
    if not move_snake():
        running = False  # Game over
    
    draw_snake()
    draw_food()
    pygame.display.update()
    clock.tick(10)  # Control snake speed

pygame.quit()
