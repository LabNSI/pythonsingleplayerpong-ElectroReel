import pygame

pygame.init()

WIDTH = 1500
HEIGHT = 1000
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

speed = 5
x_sens = y_sens = 1
auto = True
end = False

while not end:
    screen.fill(RED)
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

        if key[pygame.K_a]:
          x = radius
          y = radius

        if key[pygame.K_z]:
            x = WIDTH-radius
            y = radius

        if key[pygame.K_q]:
            x = radius
            y = HEIGHT-radius

        if key[pygame.K_s]:
            x = WIDTH-radius
            y = HEIGHT-radius

        if key[pygame.K_UP]:
            x = x
            y = y - 5
        if key[pygame.K_DOWN]:
            x = x
            y = y + 5

        if key[pygame.K_RIGHT]:
            x = x + 5
            y = y
        if key[pygame.K_LEFT]:
            x = x - 5
            y = y

    else:
        # if the circle touches the right and left edges
        # reverse direction on x-axis
        if x + radius >= WIDTH:
            x_sens = -1

        # if the circle touches the lower and upper edges
        # reverse direction on y-axis
        if y + radius == HEIGHT:
            y_sens = -1

        # compute new coordonates
        x = x + 5
        y = y + 5


    pygame.draw.circle(screen, WHITE, (x, y), radius)

    pygame.display.update()

    # wait before trying it again
    pygame.time.delay(20)

pygame.quit()
