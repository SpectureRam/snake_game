"""SNAKE GAME
    CODED WITH PYTHON
     BY SPECTURE RAM"""


import random
import sys
import time
import pygame

#Ingame Difficulty Level
#Difficulty Increases, then Game Toughens :(
difficulty = 20

#Game Window Size
frame_x = 800
frame_y = 500

#Starting Game Window...
pygame.display.set_caption("Snake Game")
game_window = pygame.display.set_mode((frame_x,frame_y))

#Error Checks...
check_errors = pygame.init()
if check_errors[1] > 0:
    print(check_errors,"error occured when game runned, exiting...")
else:
    print("Game is running successfully.")

#Colors of Snake
black = pygame.Color(0,0,0)
white = pygame.Color(255,255,255)
blue = pygame.Color(0,255,255)
red = pygame.Color(255,0,0)
green = pygame.Color(0,255,0)
yellow = (255,255,0)
cyan = (0,255,255)

#FPS
fps_controller = pygame.time.Clock()

#Snake Dimensions

snake_pos = [100,50]
snake_body = [[100,50], [100-10,50], [100-(2*10), 50]]
food_pos = [random.randrange(1, (frame_x//10)) *10, random.randrange(1, (frame_y//10))*10]
food_spawn = True
direction = 'RIGHT'
change_to = direction

score = 0

#Game Over
def game_over():
    my_font = pygame.font.SysFont('calibri', 100)
    game_over_surface = my_font.render('GAME OVER', True, red)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (frame_x/2,frame_y/2)
    game_window.fill(black)
    game_window.blit(game_over_surface, game_over_rect)
    show_score(0, red, 'times', 20)
    pygame.display.flip()
    time.sleep(3)
    pygame.quit()
    sys.exit()

#Score
def show_score(choice,color,font,size):
    score_font = pygame.font.SysFont(font,size)
    score_surface = score_font.render('Score:' +str(score),True,color)
    score_rect = score_surface.get_rect()
    if choice ==1:
        score_rect.midtop = (frame_x/10,15)
    else:
        score_rect.midtop = (frame_x/2,frame_y/1.25)
    game_window.blit(score_surface,score_rect)
    #pygame.display.flip()

#Game Controls
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
#Keys
        elif event.type == pygame.KEYDOWN:
            # W -> Up; S -> Down; A -> Left; D -> Right
            if event.key == pygame.K_UP or event.key == ord('w'):
                change_to = 'UP'
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                change_to = 'RIGHT'
# Esc -> Create event to quit the game
            if event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(pygame.QUIT))

    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    if direction == 'UP':
        snake_pos[1] -= 10
    if direction == 'DOWN':
        snake_pos[1] += 10
    if direction == 'LEFT':
        snake_pos[0] -= 10
    if direction == 'RIGHT':
        snake_pos[0] += 10

    snake_body.insert(0, list(snake_pos))
    if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
        score += 1
        food_spawn = False
    else:
        snake_body.pop()
#FOOD
    if not food_spawn:
        food_pos = [random.randrange(1, (frame_x // 10)) * 10, random.randrange(1, (frame_y // 10)) * 10]
    food_spawn = True

#GFX
    game_window.fill(black)
    for pos in snake_body:
        pygame.draw.rect(game_window, cyan, pygame.Rect(pos[0], pos[1], 10, 10))

    pygame.draw.rect(game_window, white, pygame.Rect(food_pos[0], food_pos[1], 10, 10))

    if snake_pos[0] < 0 or snake_pos[0] > frame_x - 10:
        game_over()
    if snake_pos[1] < 0 or snake_pos[1] > frame_y - 10:
        game_over()

    for block in snake_body[1:]:
        if snake_pos[0] == block[0] and snake_pos[1] == block[1]:
            game_over()

    show_score(1, white, 'consolas', 20)
    pygame.display.update()
    fps_controller.tick(difficulty)












