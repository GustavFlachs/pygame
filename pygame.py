import pygame

# inicializace pygame
pygame.init()


#vytvořit obrazovky
clock = pygame.time.Clock()
width = 600
height = 300
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Naše první hra")
player = pygame.Rect((300,250,50,50))

#hlavní herní cyklus
lets_continue = True


while lets_continue:
    screen.fill((0,0,0))
    pygame.draw.rect(screen, (255, 0, 0), player)

    key = pygame.key.get_pressed()
    if key[pygame.K_a] == True:
        player.move_ip(-1,0)
    elif key[pygame.K_d] == True:
        player.move_ip(1,0)
    elif key[pygame.K_s] == True:
        player.move_ip(0,1)
    elif key[pygame.K_w] == True:
        player.move_ip(0,-1)



    for event in pygame.event.get():
        print(event)

        if event.type == pygame.QUIT:
            lets_continue = False
    pygame.display.update()


    clock.tick(30) #uprav aby fungovala aka: koukni na to jak to má učitel a pak to oprav

#ukončení pygame
pygame.quit()