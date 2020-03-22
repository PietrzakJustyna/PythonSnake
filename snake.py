import pygame
import random
import ptext

pygame.init()

grey = (138, 147, 166)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

window_width = 400
window_height = 400

window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Snake Game by Justyna')

clock = pygame.time.Clock()

snake_block = 20

rows = window_height // snake_block

font_style = pygame.font.SysFont("Arial", 25)


def draw_grid(width, surface, rows):
    gap_size = width // rows

    x = 0
    y = 0
    for line_ in range(rows):
        x = x + gap_size
        y = y + gap_size

        pygame.draw.line(surface, grey, (x, 0), (x, width))
        pygame.draw.line(surface, grey, (0, y), (width, y))


def player_score(score):
    value = font_style.render("Your Score: " + str(score), True, yellow)
    window.blit(value, [0, 0])


def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(window, blue, [x[0], x[1], snake_block, snake_block])


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    window.blit(mesg, [0, window_height / 3])


def draw_food():
    foodx = round(random.randrange(0, window_width - snake_block) / snake_block) * snake_block
    foody = round(random.randrange(0, window_width - snake_block) / snake_block) * snake_block
    return foodx, foody


def game_intro():
    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
                if event.key == pygame.K_s:
                    snake_speed = 5
                    game_loop(snake_speed)
                if event.key == pygame.K_m:
                    snake_speed = 10
                    game_loop(snake_speed)
                if event.key == pygame.K_f:
                    snake_speed = 15
                    game_loop(snake_speed)

        window.fill(blue)
        ptext.draw("Python-Snake", (window_width/3, window_height/20), sysfontname='Arial', fontsize=25, bold=True,
                   color=black)
        ptext.draw("""Options (click on your keyboard):
                    
                    s - slow
                    m - medium
                    f - fast
                    q - quit
                    """, (window_width/12, window_height/4), sysfontname='Arial', fontsize=25)

        pygame.display.update()
        clock.tick(15)


def game_loop(snake_speed):
    game_close = False
    game_over = False

    x1 = window_width / 2
    y1 = window_height / 2

    x1_change = 0
    y1_change = 0

    snake_list = []
    length_of_snake = 1

    foodx, foody = draw_food()

    while not game_close:

        while game_over:
            window.fill(blue)
            ptext.draw("You lost!", (window_width / 3, window_height / 5), color=red, sysfontname='Arial', fontsize=25,
                       bold=True)
            ptext.draw("""Options (click on your keyboard):
            c - try again
            q - quit
                        """, (window_width / 12, window_height / 3), sysfontname='Arial', fontsize=25)
            player_score(length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_close = True
                        game_over = False
                    if event.key == pygame.K_c:
                        game_intro()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= window_width or x1 < 0 or y1 >= window_height or y1 < 0:
            game_over = True

        x1 += x1_change
        y1 += y1_change
        window.fill(black)
        draw_grid(width=window_width, surface=window, rows=rows)
        pygame.draw.rect(window, green, [foodx, foody, snake_block, snake_block])
        snake_head = [x1, y1]
        snake_list.append(snake_head)

        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_over = True

        our_snake(snake_block, snake_list)
        player_score(length_of_snake - 1)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx, foody = draw_food()
            length_of_snake += 1

        clock.tick(snake_speed)


game_intro()
