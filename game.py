import pygame
import time
import random

pygame.init()

width = 600
height = 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game 🐍')

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

clock = pygame.time.Clock()
speed = 15
block_size = 20

font = pygame.font.SysFont('Arial', 25)
font_large = pygame.font.SysFont('Arial', 40)

high_score = 0

def draw_text(text, color, y, center=True, font_used=font):
    render = font_used.render(text, True, color)
    rect = render.get_rect()
    if center:
        rect.center = (width // 2, y)
    else:
        rect.topleft = (10, y)
    screen.blit(render, rect)

def show_score(score, high_score):
    draw_text(f"Score: {score}", black, 10, center=False)
    draw_text(f"High Score: {high_score}", blue, 40, center=False)

def main_menu():
    while True:
        screen.fill(white)
        draw_text("🐍 Snake Game 🐍", green, 100, font_used=font_large)
        draw_text("Press ENTER to start", black, 180)
        draw_text("Press ESC to quit", black, 220)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()

def game():
    global high_score

    game_over = False
    game_close = False

    x = width / 2
    y = height / 2
    x_change = 0
    y_change = 0

    snake_body = []
    snake_length = 1

    food_x = round(random.randrange(0, width - block_size) / 20.0) * 20.0
    food_y = round(random.randrange(0, height - block_size) / 20.0) * 20.0

    while not game_over:

        while game_close:
            screen.fill(white)
            draw_text("You Lost!", red, 100, font_used=font_large)
            draw_text("Press R to restart or Q to quit", black, 200)
            show_score(snake_length - 1, high_score)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    elif event.key == pygame.K_r:
                        game()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -block_size
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = block_size
                    y_change = 0
                elif event.key == pygame.K_UP:
                    y_change = -block_size
                    x_change = 0
                elif event.key == pygame.K_DOWN:
                    y_change = block_size
                    x_change = 0

        x += x_change
        y += y_change

        if x >= width or x < 0 or y >= height or y < 0:
            game_close = True

        screen.fill(white)
        pygame.draw.rect(screen, green, [food_x, food_y, block_size, block_size])

        head = [x, y]
        snake_body.append(head)

        if len(snake_body) > snake_length:
            del snake_body[0]

        for segment in snake_body[:-1]:
            if segment == head:
                game_close = True

        for segment in snake_body:
            pygame.draw.rect(screen, black, [segment[0], segment[1], block_size, block_size])

        current_score = snake_length - 1
        if current_score > high_score:
            high_score = current_score

        show_score(current_score, high_score)
        pygame.display.update()

        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, width - block_size) / 20.0) * 20.0
            food_y = round(random.randrange(0, height - block_size) / 20.0) * 20.0
            snake_length += 1

        clock.tick(speed)

    pygame.quit()
    quit()

main_menu()
game()