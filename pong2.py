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
pygame.draw.circle(screen, WHITE, (WIDTH/2, HEIGHT/2), radius)

end = False
while not end:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            end = True

    pygame.display.update()

pygame.quit()
