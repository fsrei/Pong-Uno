# setup
import pygame, sys

def ball_animation():
    global ball_speed_x, ball_speed_y
    
    ball.x += ball_speed_x
    ball.y += ball_speed_y
    
    if (ball.top <= 0) or (ball.bottom >= screh):
        ball_speed_y *= -1
        
    if (ball.left <= 0) or (ball.right >= screw):
        ball_speed_x *= -1
        
    if ball.colliderect(player1) or ball.colliderect(player2):
        ball_speed_x *= -1

def player1_animation():
    player1.y += player1_speed
    
    if player1.top <= 0:
        player1.top = 0
    if player1.bottom >= screh:
        player1.bottom = screh

def player2_animation():
    player2.y += player2_speed
    
    if player2.top <= 0:
        player2.top = 0
    if player2.bottom >= screh:
        player2.bottom = screh

pygame.init()
clock = pygame.time.Clock()

screw = 600; screh = 400
screen = pygame.display.set_mode((screw, screh))
pygame.display.set_caption('Pong')

# Colors
light_grey = (200, 200, 200)
bg_color = pygame.Color('gray15')
cyan = (0,255,127)
green = (173,255,47)

# Game rectangles
left_ball = (screw / 2 ) - 10
top_ball = (screh / 2 ) - 10
witdh_ball = 20
height_ball = 20

height_player = 80
witdh_player = 5

left_player1 = 50 
top_player1 = (screh / 2 ) - 20

left_player2 = screw - 50
top_player2 = (screh / 2 ) - 20


ball = pygame.Rect(left_ball, top_ball, witdh_ball, height_ball)
player1 = pygame.Rect(left_player1, top_player1, witdh_player, height_player)
player2 = pygame.Rect(left_player2, top_player2, witdh_player, height_player)

# Game variables

ball_speed_x = 4
ball_speed_y = 4
player1_speed = 0
player2_speed = 0

control = True
while control:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player1_speed -= 7
            if event.key == pygame.K_DOWN:
                player1_speed += 7
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                player1_speed += 7
            if event.key == pygame.K_DOWN:
                player1_speed -= 7
                
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player2_speed -= 7
            if event.key == pygame.K_s:
                player2_speed += 7
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                player2_speed += 7
            if event.key == pygame.K_s:
                player2_speed -= 7
    # Game logic
    ball_animation()
    player1_animation()
    player2_animation()

    # Elements
    screen.fill(bg_color)
    pygame.draw.ellipse(screen, light_grey, ball)
    pygame.draw.rect(screen, green, player1)
    pygame.draw.rect(screen, cyan, player2)
    # Central line
    pygame.draw.aaline(screen, light_grey, (screw / 2, 0), (screw / 2, screh))
    
    pygame.display.flip()
    clock.tick(60)