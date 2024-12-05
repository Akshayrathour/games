#importing stuff
import pygame 
pygame.init()

#game variables
fps=60
width,height=650,500
clock=pygame.time.Clock()
exit_screen=False
bg_color="#36454F" #charcoal color
p_width,p_height=5,50
p_color="#ED7014"
p1_pos=p2_pos=height/2
p1_pos_x=10
p2_pos_x=width-15
p1_vel=0
p2_vel=0
ball_color='#FFFFFF'
ball_radius=8
ball_vel=5
ball_x=width/2
ball_y=height/2
ball_vel_x=ball_vel
ball_vel_y=0
#game screen
screen=pygame.display.set_mode((width,height))
pygame.display.set_caption("Pong")

# class Ball:
#         ball_vel=5
        
#         def __init__(self,x,y,radius) -> None:
#             self.x=x
#             self.y=y
#             self.radius=radius
#             self.vel_x=self.ball_vel
#             self.vel_y=0
       
#         def draw(self):
#             pygame.draw.circle(screen,ball_color, (self.x, self.y),self.radius)
        
#         def move(self):
#               self.x+=self.vel_x
#               self.y+=self.vel_y

#game loop
while not exit_screen:
    screen.fill(bg_color)
    pygame.draw.rect(screen,p_color,[p1_pos_x,p1_pos,p_width,p_height])
    pygame.draw.rect(screen,p_color,[p2_pos_x,p2_pos,p_width,p_height])
    pygame.draw.circle(screen,ball_color, (ball_x, ball_y),ball_radius)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit_screen=True
        # if event.type==pygame.KEYDOWN:  # event handling
    keys=pygame.key.get_pressed()
    if keys[pygame.K_w]:
                if p1_pos-5>=0 and p1_pos-5<=height-p_height:
                    p1_pos-=5
                    p1_vel=-4
    elif keys[pygame.K_s]:
                if p1_pos+5>=0 and p1_pos+5<=height-p_height:
                    p1_pos+=5
                    p1_vel=4
    elif keys[pygame.K_UP]:
                if p2_pos-5>=0 and p2_pos-5<=height-p_height:
                    p2_pos-=5
                    p2_vel=-4
    elif keys[pygame.K_DOWN]:
                if p2_pos+5>=0 and p2_pos+5<=height-p_height:
                    p2_pos+=5
                    p2_vel=4
    if p1_pos+p1_vel>=0 and p1_pos-p1_vel<=height-p_height:
           p1_pos+=p1_vel
           p1_vel=0
    if p2_pos+p2_vel>=0 and p2_pos-p2_vel<=height-p_height:
           p2_pos+=p2_vel
           p2_vel=0
    ball_x+=ball_vel_x
    ball_y+=ball_vel_y
    # if (ball_x==p2_pos_x and ball_y>=p2_pos and ball_y<=p2_pos+p_height) or (ball_x==p1_pos_x and ball_y>=p1_pos and ball_y<=p1_pos+p_height):
    #        ball_vel_x*=-1
    if ball_x<0 or ball_x>width:
           ball_x=width/2
           ball_y=height/2
           ball_vel_x*=-1
           ball_vel_y=0
    if ball_y + ball_radius >= height:
        ball_vel_y *= -1
    elif ball_y - ball_radius <= 0:
        ball_vel_y *= -1

    if ball_vel_x < 0:
        if ball_y >= p1_pos and ball_y <= p1_pos + p_height:
            if ball_x - ball_radius <= p1_pos_x + p_width:
                ball_vel_x *= -1

                middle_y = p1_pos + p_height / 2
                difference_in_y = middle_y - ball_y
                reduction_factor = (p_height / 2) / ball_vel
                y_vel = difference_in_y / reduction_factor
                ball_vel_y = -1 * y_vel

    else:
        if ball_y >= p2_pos and ball_y <= p2_pos + p_height:
            if ball_x + ball_radius >= p2_pos_x:
                ball_vel_x *= -1

                middle_y = p2_pos + p_height / 2
                difference_in_y = middle_y - ball_y
                reduction_factor = (p_height / 2) / ball_vel
                y_vel = difference_in_y / reduction_factor
                ball_vel_y = -1 * y_vel

    # pygame.draw.rect(screen,p_color,[p1_pos_x,p1_pos,p_width,p_height])
    # pygame.draw.rect(screen,p_color,[p2_pos_x,p2_pos,p_width,p_height])
    # pygame.draw.circle(screen,ball_color, (ball_x, ball_y),ball_radius)
    pygame.display.update()
    clock.tick(fps)

pygame.quit()
quit()