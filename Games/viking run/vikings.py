#imports
import pygame
pygame.init()

#game variables
exit_window=False
font=pygame.font.SysFont("Comic Sans ms",1)
fps=60
clock=pygame.time.Clock()
Width,Height=700,300
screen=pygame.display.set_mode((Width,Height))
pygame.display.set_caption("Viking Run")
font=pygame.font.SysFont("Comic sans ms",30,False,True)
bg_img=pygame.image.load(r'E:\projects\Games\viking run\assets\gabriel-gabas-x-pmwxv17xss1tctdo6o1-1280.jpg').convert_alpha()
scaled_bg_img=pygame.transform.scale(bg_img,(Width,Height))
p_start_x,p_start_y=10,210
p_width,p_height=20,50
gravity=5
jump_speed=30
score,temp_score=0,0
score_txt_x,score_txt_y=10,10
obstacle_speed=2
obstacle_y=210

class player():
    def __init__(self,x,y,width,height) -> None:
        self.x=self.original_x=x
        self.y=self.original_y=y
        self.width=width
        self.height=height
        self.vel_y=0
        self.jump=False

class obstacle():
    def __init__(self) -> None:
        self.width=[5,10,12,15]
        # self.height=[5,10,15,20]
        self.speed=obstacle_speed
        self.h=50
        self.w=10
        self.x=Width
        self.y=obstacle_y

#functions

def display_text(text,x,y,color):
    txt=font.render(text,True,color)
    screen.blit(txt,[x,y])

def draw(p,score,o1):
    screen.blit(scaled_bg_img,(0,0))
    display_text("Score: "+str(score),score_txt_x,score_txt_y,"#000000")
    pygame.draw.rect(screen,"#FF0000",(p.x,p.y,p.width,p.height))
    pygame.draw.rect(screen,"#FF0000",(o1.x,o1.y,o1.w,o1.h))
    pygame.display.update()

def movement(keys,p,o1):
    #chcking if space is clicked so the player may jump and also jumping only when not already jumping 
    if keys[pygame.K_SPACE] and p.jump==False:
        print("jump")
        p.vel_y=-jump_speed
        p.jump=True
    #setting up the jump and gravity for the player
    p.y+=p.vel_y
    p.vel_y+=gravity
    if p.y>p_start_y:
        p.vel_y=0
        p.y=p_start_y
    #this statement checks so that there is no double jump
    if p.y>=p_start_y:
        p.jump=False
    #setting up the obstacle movement
    o1.x-=o1.speed
    if(o1.x<-o1.w): o1.x=Width

#game loop
p=player(p_start_x,p_start_y,p_width,p_height)
o1=obstacle()
o2=obstacle()
o3=obstacle()
while not exit_window:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit_window=True
    draw(p,score,o1)
    keys=pygame.key.get_pressed()
    movement(keys,p,o1)
    if p.x<300:
        p.x+=1
    temp_score+=1
    if temp_score%10==0:
        score+=1
        temp_score=0
    if(score%200==0 and score>0):
        o1.speed+=1
        o2.speed+=1
        o3.speed+=1
    clock.tick(fps)

pygame.quit()
quit()