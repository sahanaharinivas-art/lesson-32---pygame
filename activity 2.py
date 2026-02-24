import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((600,400))
pygame.display.set_caption("image and label example")

WHITE =(225, 225, 225)
BLACK = (0,0,0)

image = pygame.image.load("sunset.jpg")
image = pygame.transform.scale(image, (150,150))

font = pygame.font.Font(None,36)
text = font.render("hello pygame!", True, BLACK)

running = True
while running:
    screen.fill(WHITE)

    screen.blit(image, (225,80))

    screen.blit(text,(220,250))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()

pygame.quit()
sys.exit()
