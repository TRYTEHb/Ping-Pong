import pygame, sys
pygame.init()

clock = pygame.time.Clock()

win_width = 1280
win_height = 960

window = pygame.display.set_mode((win_width, win_height))

pygame.display.set_caption('Ping-pong')

ball = pygame.Rect(win_width/2 -15, win_height/2 - 15,30,30)
player1 = pygame.Rect(win_width-20, win_height/2 - 70,10,140)
opponent = pygame.Rect(20, win_height/2 - 70,10,140)

def player_animation():
    player1.y += player_speed
    if player1.top <= 0:
        player1.top = 0
    if player1.bottom >= win_height:
        player1.bottom = win_height

def opponent_ai():
	if opponent.top < ball.y:
		opponent.y += opponent_speed
	if opponent.bottom > ball.y:
		opponent.y -= opponent_speed

	if opponent.top <= 0:
		opponent.top = 0
	if opponent.bottom >= win_height:
		opponent.bottom = win_height

def ball_animation():
    global ball_speed_x, ball_speed_y
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= win_height:
        ball_speed_y *= -1
    if ball.left <= 0 or ball.right >= win_width:
        ball_speed_x *= -1

    if ball.colliderect(player1) or ball.colliderect(opponent):
        ball_speed_x *= -1

ball_speed_x = 7
ball_speed_y = 7
player_speed = 0
opponent_speed = 7

score1 = 0
score2 = 0

bg_color = pygame.Color('grey12')
light_gray = (200,200,200)
red = (255,0,0)
blue = (0,0,255)
run = True

while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False

        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_DOWN:
                player_speed += 7
            if e.key == pygame.K_UP:
                player_speed -= 7
        if e.type == pygame.KEYUP:
            if e.key == pygame.K_DOWN:
                player_speed -= 7
            if e.key == pygame.K_UP:
                player_speed += 7

    ball_animation()
    player_animation()
    opponent_ai()

    window.fill(bg_color)
    pygame.draw.rect(window,red,player1)
    pygame.draw.rect(window,blue,opponent)
    pygame.draw.ellipse(window,light_gray,ball)
    pygame.draw.aaline(window,light_gray,(win_width/2,0),(win_width/2,win_height))

    
    pygame.display.update()
    clock.tick(60)