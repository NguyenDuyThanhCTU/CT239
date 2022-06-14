from turtle import Screen
import pygame

pygame.init()

screen = pygame.display.set_mode((1000,600))

GREY = (120,120,120)

running = True
while running:
    screen.fill(GREY)

    mouse_x, mouse_y = pygame.mouse.get_pos()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                print(mouse_x, mouse_y)
        pass
    pygame.display.flip()
    

