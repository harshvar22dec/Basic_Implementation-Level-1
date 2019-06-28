try:
    background_image_filename = input('Paste here the location of image\t')
    import pygame;import cv2
    from pygame.locals import *
    from sys import exit
    pygame.init()
    screen = pygame.display.set_mode((1360,690), 0, 32);pygame.display.set_caption("Harsh's Image Editor")
    background = pygame.image.load(background_image_filename).convert()
    x, y = 0, 0 ;move_x, move_y = 0, 0;slic=10
    print('\n Use Arrows to move the image')
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:exit()
            if event.type == KEYDOWN:
                if event.key == K_LEFT:
                    move_x = +slic
                elif event.key == K_RIGHT:
                    move_x = -slic
                elif event.key == K_UP:
                    move_y = +slic
                elif event.key == K_DOWN:
                    move_y = -slic
            elif event.type == KEYUP:
                if event.key == K_LEFT: move_x = 0
                elif event.key == K_RIGHT: move_x = 0
                elif event.key == K_UP: move_y = 0
                elif event.key == K_DOWN: move_y = 0

        x += move_x
        y += move_y
        screen.fill((0, 0, 0))
        screen.blit(background, (x, y))
        pygame.display.update()
except:
    print('Not, Found!\t Check Again  ')
