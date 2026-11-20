import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
background = pygame.image.load("E.jpeg").convert()

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.fill((135, 206, 235))    
    screen.blit(background, (0, 0))
    pygame.display.flip()