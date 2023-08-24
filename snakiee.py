import pygame
import time
import random

pygame.init()

# Set the display window size
width = 500
height = 500

# Set the color of the window and the snake
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

# Create the window
gameDisplay = pygame.display.set_mode((width, height))

# Set the title of the window
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()

block_size = 10

font = pygame.font.SysFont(None, 25)


def message_to_screen(msg, color):
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text, [width / 2 - len(msg) * 5, height / 2])


def gameLoop():
    gameExit = False
    gameOver = False
    lead_x = width / 2
    lead_y = height / 2
    lead_x_change = 0
    lead_y_change = 0

    # Create the food for the snake
    foodx = round(random.randrange(0, width - block_size) / 10.0) * 10.0
    foody = round(random.randrange(0, height - block_size) / 10.0) * 10.0

    # Create the snake
    snakeList = []
    snakeLength = 1

    # Main game loop
    while not gameExit:

        while gameOver:
            gameDisplay.fill(white)
            message_to_screen("Game over, press Q to quit or C to play again", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True

            # Get the direction of the snake using arrow keys
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    lead_x_change = -block_size
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    lead_x_change = block_size
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    lead_y_change = -block_size
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    lead_y_change = block_size
                    lead_x_change = 0

        # Check if the snake hits the edges of the window
        if lead_x >= width or lead_x < 0 or lead_y >= height or lead_y < 0:
            gameOver = True

        lead_x += lead_x_change
        lead_y += lead_y_change

        gameDisplay.fill(white)

        # Draw the food
        pygame.draw.rect(gameDisplay, red, [foodx, foody, block_size, block_size])

        # Create the snake's head
        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)

        # Check if the snake eats the food
        if lead_x == foodx and lead_y == foody:
            foodx = round(random.randrange(0, width - block_size) / 10.0) * 10.0
            foody = round(random.randrange(0, height - block_size) / 10.0) * 10.0
            snakeLength += 1

        # Remove the tail of the snake if it's too long
        if len(snakeList) > snakeLength:
            del snakeList[0]

        # Check if the snake collides with itself
        for segment in snakeList[:-1]:
            if segment == snakeHead:
                gameOver = True

        # Draw the snake
        for segment in snakeList:
            pygame.draw.rect(gameDisplay, black, [segment[0], segment[1], block_size, block_size])

        pygame.display.update()

        # Set the game speed
        clock.tick(15)

    pygame.quit()
    quit()


# Start the game loop
gameLoop()
