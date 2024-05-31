import pygame

# inicializace pygame
pygame.init()


#vytvořit obrazovky
width = 600
height = 300
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Naše první hra")


#hlavní herní cyklus
lets_continue = True

while lets_continue:
    for event in pygame.event.get():
        print(event)

        if event.type == pygame.QUIT:
            lets_continue = False

#ukončení pygame
pygame.quit()
