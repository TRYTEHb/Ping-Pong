import pygame, sys
pygame.init()

clock = pygame.time.Clock()

win_width = 1280
win_height = 960

window = pygame.display.set_mode((win_width, win_height))

pygame.display.set_caption('Ping-pong')

ball = pygame.Rect(win_width/2 -15, win_height/2 - 15,30,30)
player1 = pygame.Rect(win_width-20, win_height/2 - 70,10,140)
player2 = pygame.Rect(20, win_height/2 - 70,10,140)

bg_color = pygame.Color('grey12')
light_gray = (200,200,200)
red = (255,0,0)
blue = (0,0,255)
run = True

while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False

    pygame.draw.rect(window,red,player1)
    pygame.draw.rect(window,blue,player2)
    pygame.draw.rect(window,light_gray,ball)
    pygame.display.update()
    clock.tick(60)