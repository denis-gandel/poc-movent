import pygame
import sys

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Movimiento y Salto")

black = (0, 0, 0)
red = (255, 0, 0)

square_size = 50
square_x = 100
square_y = screen_height - square_size
square_speed = 5
jump_height = 10
gravity = 1

is_jumping = False
jump_count = jump_height

clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        square_x -= square_speed
    if keys[pygame.K_RIGHT]:
        square_x += square_speed

    if not is_jumping:
        if keys[pygame.K_SPACE]:
            is_jumping = True
    else:
        if jump_count >= -jump_height:
            neg = 1 if jump_count > 0 else -1
            square_y -= (jump_count ** 2) * 0.5 * neg
            jump_count -= 1
        else:
            is_jumping = False
            jump_count = jump_height

    if square_x < 0:
        square_x = 0
    if square_x > screen_width - square_size:
        square_x = screen_width - square_size
    if square_y > screen_height - square_size:
        square_y = screen_height - square_size

    screen.fill(black)

    pygame.draw.rect(screen, red, (square_x, square_y, square_size, square_size))

    pygame.display.flip()

    clock.tick(30)

pygame.quit()
sys.exit()
