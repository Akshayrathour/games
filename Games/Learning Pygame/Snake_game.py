import pygame
import random
import os

x=pygame.init()  #load all the modules inside pygame

#creating the screen for game, but it apperas only for a second
screen=pygame.display.set_mode((700,500))
pygame.display.set_caption("snake game")

font=pygame.font.SysFont(None,55)
#game variables
# exit_game=False
# game_over=False
# snake_x=50
# snake_y=50
# vel_x=0
# vel_y=0
# init_vel=10
# food_x=random.randint(50,250)
# food_y=random.randint(50,250)
# score=0
# snk_list=[]
# snk_len=1
# snake_size=10
# clock=pygame.time.Clock()
# fps=60

def score_display(text,color,x,y):
    txt=font.render(text,True,color)
    screen.blit(txt,[x,y])

def plot_snake(screen,snkl,snks):
    # print(snkl) 
    for x,y in snkl:
        pygame.draw.rect(screen,'#000000',[x,y,snks,snks])

# screen.fill('#4092c2')
# pygame.draw.rect(screen,'#000000',[snake_x,snake_y,10,10])
# pygame.display.update()

# game loop
def game_loop():
    exit_game=False
    game_over=False
    snake_x=50
    snake_y=50
    vel_x=0
    vel_y=0
    init_vel=3
    food_x=random.randint(50,250)
    food_y=random.randint(50,250)
    score=0
    snk_list=[]
    snk_len=1
    snake_size=20
    clock=pygame.time.Clock()
    fps=60
    if (not(os.path.exists("highscore.txt"))):
        with open("highscore.txt",'w') as f:
            f.write("0")
    with open("highscore.txt",'r') as f:
        hscore=f.read()
    while not exit_game:
        if game_over:
                screen.fill('#4092c2')
                score_display("Game Over, press enter to continue",'#FFFFFF',40,225)

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        exit_game = True

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            game_loop()
        else:
            for event in pygame.event.get():
                # print(event)
                if event.type==pygame.QUIT:   # to quit the game window
                    exit_game=True
                if event.type==pygame.KEYDOWN:  # event handling
                    if event.key==pygame.K_RIGHT:
                        # print("pressed right arrow key")
                        vel_x=init_vel
                        vel_y=0
                    elif event.key==pygame.K_LEFT:
                        # print("pressed left arrow key")
                        vel_x=-init_vel
                        vel_y=0
                    elif event.key==pygame.K_UP:
                        # print("pressed up arrow key")
                        vel_y=-init_vel
                        vel_x=0
                    elif event.key==pygame.K_DOWN:
                        # print("pressed down arrow key")
                        vel_y=init_vel
                        vel_x=0
                    if abs(snake_x-food_x)<=30 and abs(snake_y-food_y)<=30:
                        score+=10
                        snk_len+=2
                        # print("score:",score)
                        food_x=random.randint(50,250)
                        food_y=random.randint(50,250)
            snake_x+=vel_x
            snake_y+=vel_y
            screen.fill('#4092c2') 
            if score>int(hscore):
                with open("highscore.txt",'w') as f:
                    f.write(str(score))
                    hscore=str(score)
            score_display("Score:"+str(score),'#FFFFFF',5,5)

            score_display("HighScore:"+hscore,'#FFFFFF',430,5)
            pygame.draw.rect(screen,'#ff0000',[food_x,food_y,15,15])

            snk_list.append([snake_x,snake_y])
            if len(snk_list)>snk_len:
                del snk_list[0]
            if [snake_x,snake_y] in snk_list[:-1]:
                game_over = True

            if snake_x<0 or snake_x>700 or snake_y<0 or snake_y>500:
                game_over = True
            plot_snake(screen,snk_list,snake_size)
            # pygame.draw.rect(screen,'#000000',[snake_x,snake_y,10,10])
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()

exit_screen=False
while not exit_screen:
    screen.fill('#4092c2')
    score_display("Snakes Game",'#FFFFFF',210,210)
    score_display("Press Enter to continue",'#FFFFFF',140,255)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:   # to quit the game window
           exit_screen=True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                game_loop()