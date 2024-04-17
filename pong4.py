import pygame

pygame.init()

WIDTH = 300
HEIGHT = 200
screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption('My Game')

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 255)

screen.fill(RED)
pygame.display.update()

radius = 25
x = WIDTH//2
y = HEIGHT//2
pygame.draw.circle(screen, WHITE, (x, y), radius)  # Position is the center of the circle.

speed = 1
x_sens = y_sens = 1
auto = True
end = False

while not end:
    SCREEN.fill(RED)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            end = True

    key = pygame.key.get_pressed()

    if key[pygame.K_o]:
        auto = True

    if key[pygame.K_m]:
        auto = False

    if not auto:
        # Manual mode :
        #  - use A, Z, Q, S to move circle on the corners
        #  - use UP, DOWN, LEFT, RIGHT to move circle by <speed> pixel


    else:
        # if the circle touches the right and left edges
        # reverse direction on x-axis
        if ____:
            x_sens = -1

        # if the circle touches the lower and upper edges
        # reverse direction on y-axis
        if ___:
            y_sens = -1

        # compute new coordonates
        x = x + ___
        y = y + ___


    pygame.draw.circle(SCREEN, WHITE, (x, y), radius)

    pygame.display.update()

    # wait before trying it again
    pygame.time.delay(10)

pygame.quit()
