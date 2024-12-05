'''
not so cool and missing a lot of functionalities such as menu,setting,superpoers and crazy mode(not really). But it is a decent game.
'''
#imports
import pygame
from pygame import mixer
pygame.init()
mixer.init()

#setting the window
Width,Height=714,385
screen=pygame.display.set_mode((Width,Height))
pygame.display.set_caption("Fighter_Goku")

#variables
fps=60
clock=pygame.time.Clock()
exit_window=False
p_width,p_height=20,80
bg_img=pygame.image.load(r'E:\projects\Games\fighter_goku\assets\primary_bg_img.png').convert_alpha()
bg_img2=pygame.image.load(r'E:\projects\Games\fighter_goku\assets\eric-_j-08213.jpg').convert_alpha()
p1_start_x,p1_start_y=100,265
p2_start_x,p2_start_y=Width-100,265
p1_width,p1_height=30,100
p2_width,p2_height=30,100
p_mov_speed=5
gravity=3
health_bar_width,health_bar_height=325,30
p1_health_bar_x,p1_health_bar_y=10,10
p2_health_bar_x,p2_health_bar_y=380,10
p1_size=162
p1_scale=3
p1_offset=[77,62]
p1_data=[p1_size,p1_scale,p1_offset]
p2_size=250
p2_scale=2
p2_offset=[120,110]
p2_data=[p2_size,p2_scale,p2_offset]
p1_sheet=pygame.image.load(r'E:\projects\Games\brawler_tut-main\assets\images\warrior\Sprites\warrior.png').convert_alpha()
p2_sheet=pygame.image.load(r'E:\projects\Games\brawler_tut-main\assets\images\wizard\Sprites\wizard.png').convert_alpha()
p1_steps=[10,8,1,7,7,3,7]
p2_steps=[8,8,1,8,8,3,7]
intro_count=3
last_count_update=pygame.time.get_ticks()
p_font=pygame.font.SysFont(None,35)
c_font=pygame.font.SysFont(None,75)

pygame.mixer.music.load(r"E:\projects\Games\fighter_goku\assets\Dragon Ball Z.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1,0.0,5000)
sword_music=pygame.mixer.Sound(r"E:\projects\Games\brawler_tut-main\assets\audio\sword.wav")
sword_music.set_volume(0.5)
magic_music=pygame.mixer.Sound(r"E:\projects\Games\brawler_tut-main\assets\audio\magic.wav")
magic_music.set_volume(0.5)

class player:
    def __init__(self, x, y, width, height,health_bar_x,health_bar_y,data,sheet,steps):
        self.size=data[0]
        self.img_scale=data[1]
        self.offset=data[2]
        self.anim_list=self.load_img(steps,sheet)
        self.action=0   # 0:idle,1:run,2:jump,3:attack,4:attack,5:hit,6:death
        self.frame_index=0
        self.img=self.anim_list[self.action][self.frame_index]
        self.flip=False
        self.x = self.original_x = x
        self.y = self.original_y = y
        self.width = width
        self.height = height
        self.jump=False
        self.vel_y=0
        self.attacking=False
        self.attack_type=0
        self.mov_dir=0
        self.health=100
        self.health_bar_y=health_bar_y
        self.health_bar_x=health_bar_x
        self.update_time=pygame.time.get_ticks()
        self.running=False
        self.attack_cooldown=0
        self.hitted=False
        self.alive=True

    def reset(self):
        self.x = self.original_x
        self.y = self.original_y 
        self.jump=False
        self.vel_y=0
        self.attacking=False
        self.attack_type=0
        self.mov_dir=0
        self.health=100
        self.update_time=pygame.time.get_ticks()
        self.running=False
        self.attack_cooldown=0
        self.hitted=False
        self.alive=True
        self.action=0   # 0:idle,1:run,2:jump,3:attack,4:attack,5:hit,6:death
        self.frame_index=0

    def load_img(self,ani_steps,sheet):
        ani_list=[]
        for y,ani in enumerate(ani_steps):
            temp_img_list=[]
            for x in range(ani):
                temp_img=sheet.subsurface(x*self.size,y*self.size,self.size,self.size)
                temp_img_list.append(pygame.transform.scale(temp_img,(self.size *self.img_scale,self.size *self.img_scale)))
            ani_list.append(temp_img_list)
        return ani_list

    def update_action(self,new_action):
        if self.action!=new_action:
            self.action=new_action
            self.frame_index=0
            self.update_time=pygame.time.get_ticks()

    def update_ani(self):
        cooldown=50
        if self.running==True:
            self.update_action(1)
        elif self.jump==True:
            self.update_action(2)
        elif self.attacking==True:
            if self.attack_type==1:
                self.update_action(3)
            else:
                self.update_action(4)
        elif self.hitted==True:
                self.update_action(5)
        elif self.alive==False:
            self.update_action(6)
        else:
            self.update_action(0)
        self.img=self.anim_list[self.action][self.frame_index]
        if pygame.time.get_ticks()-self.update_time> cooldown:
            if self.alive==False:
                self.frame_index=len(self.anim_list[self.action])-1
            else:
                self.frame_index=(self.frame_index+1)%len(self.anim_list[self.action])
                self.update_time=pygame.time.get_ticks()
                if self.action==3 or self.action==4:
                    self.attacking=False
                if self.hitted==True:
                    self.hitted=False

    def draw(self):

        ratio=self.health/100
        pygame.draw.rect(screen,"#36454F",(self.health_bar_x-3,self.health_bar_y-3,health_bar_width+6,health_bar_height+6))
        pygame.draw.rect(screen,"#FF5733",(self.health_bar_x,self.health_bar_y,health_bar_width*ratio,health_bar_height))

        # pygame.draw.rect(screen, '#ff0000', (self.x, self.y, self.width, self.height))
        img=pygame.transform.flip(self.img,self.flip,False)
        screen.blit(img,(self.x-(self.offset[0]*self.img_scale),self.y-(self.offset[1]*self.img_scale)))
    
    def attack(self,p,flip_dir,target):
        self.attacking=True
        if p==1 and self.attack_cooldown==0:
            self.attack_cooldown=30
            sword_music.play()
            if(flip_dir==False):
                # attack_rect=pygame.Rect(screen,"#00FF00",(self.rect.x+self.width,self.y,2*self.width,self.height))
                attack_rect=pygame.Rect((self.x+self.width,self.y,3.5*self.width,self.height))
                
            else:
                attack_rect=pygame.Rect((self.x-3.5*self.width,self.y,3.5*self.width,self.height))
            
            target_rect=pygame.Rect((target.x, target.y, target.width, target.height))
            if attack_rect.colliderect(target_rect):
                    # print("hit")
                    target.health-=10
                    if target.health<=0:
                        target.alive=False
                    else:
                        target.hitted=True
        
        elif p==2 and self.attack_cooldown==0:
            self.attack_cooldown=30
            magic_music.play()
            if(flip_dir==False):
                attack_rect=pygame.Rect((self.x+self.width,self.y,3.5*self.width,self.height))
            else:
                attack_rect=pygame.Rect((self.x-3.5*self.width,self.y,3.5*self.width,self.height))
            
            target_rect=pygame.Rect((target.x, target.y, target.width, target.height))
            if attack_rect.colliderect(target_rect):
                    # print("hit")
                    target.health-=10
                    if target.health<=0:
                        target.alive=False
                    else:
                        target.hitted=True

#functions
def draw(p):
    # scaled_bg=pygame.transform.scale(bg_img2,(Width,Height))   #using this you can change the size of your image.
    screen.blit(bg_img,(0,0))
    for i in p:
        i.update_ani()
        i.draw()
    display_txt("P2",p2_health_bar_x,p2_health_bar_y,'#FFFF00','p')
    display_txt("P1",p1_health_bar_x,p1_health_bar_y,'#FFFF00','p')
    pygame.display.update()

def movement(keys,p1,p2):
    p1.running=False
    p2.running=False
    #player_1 controls
    if p1.attacking==False and p1.alive:
        if keys[pygame.K_d] and p1.x+p_mov_speed<=Width-p1_width:
            p1.x+=p_mov_speed
            p1.mov_dir=1
            p1.running=True
        if keys[pygame.K_a] and p1.x-p_mov_speed>=0:
            p1.x-=p_mov_speed
            p1.mov_dir=-1
            p1.running=True
        if keys[pygame.K_w] and p1.jump==False:
            p1.vel_y=-30
            p1.jump=True
        if keys[pygame.K_s] and p1.y+p_mov_speed<=p1_start_y:
            p1.y+=p_mov_speed
        if keys[pygame.K_u] or keys[pygame.K_i]:   #attacking features
            if keys[pygame.K_u]:
                p1.attack_type=1
            else:
                p1.attack_type=2
            p1.attack(1,p1.flip,p2)
    #player_2 controls
    if p2.attacking==False and p2.alive:
        if keys[pygame.K_LEFT] and p2.x-p_mov_speed>=0:
            p2.x-=p_mov_speed
            p2.mov_dir=1
            p2.running=True
        if keys[pygame.K_RIGHT] and p2.x+p_mov_speed<Width-p2_width:
            p2.x+=p_mov_speed
            p2.mov_dir=-1
            p2.running=True
        if keys[pygame.K_UP] and p2.jump==False:
            p2.vel_y=-30
            p2.jump=True
        if keys[pygame.K_DOWN] and p2.y+p_mov_speed<=p2_start_y:  #attacking features
            p2.y+=p_mov_speed
        if keys[pygame.K_n] or keys[pygame.K_m]:
            if keys[pygame.K_n]:
                p1.attack_type=1
            else:
                p1.attack_type=2
            p2.attack(2,p2.flip,p1)
    
    if p1.x>p2.x:
        if p1.alive:
            p1.flip=True
        if p2.alive:
            p2.flip=False
    else:
        if p1.alive:
            p1.flip=False
        if p2.alive:
            p2.flip=True
    if p1.attack_cooldown>0:
        p1.attack_cooldown-=1
    if p2.attack_cooldown>0:
        p2.attack_cooldown-=1
    #setting up the jumping and gravity for player_1
    p1.y+=p1.vel_y
    p1.vel_y+=gravity
    if p1.y>p1_start_y:
        p1.vel_y=0
        p1.y=p1_start_y
    #setting up the jumping and gravity for player_2
    p2.y+=p2.vel_y
    p2.vel_y+=gravity
    if p2.y>p2_start_y:
        p2.vel_y=0
        p2.y=p2_start_y
    #changing the jump state for the players , this instance variable and statements were added so that double jump do not happen.
    if p1.y>=p1_start_y:
        p1.jump=False
    if p2.y>=p2_start_y:
        p2.jump=False
    # p1.attacking=False
    # p2.attacking=False

def display_txt(text,x,y,color,f):
    if f=='c':
        txt=c_font.render(text,True,color)
    elif f=='p':
        txt=p_font.render(text,True,color)
    screen.blit(txt,[x,y])

#game loop
p2=player(p2_start_x,p2_start_y,p2_width,p2_height,p2_health_bar_x,p2_health_bar_y,p2_data,p2_sheet,p2_steps) 
p1=player(p1_start_x,p1_start_y,p1_width,p1_height,p1_health_bar_x,p1_health_bar_y,p1_data,p1_sheet,p1_steps)
while not exit_window:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit_window=True
    draw([p1,p2])
    if p1.alive==False or p2.alive==False:
        display_txt("victory",Width/2-70,Height/2-50,"#FFFF00",'c')
        display_txt("press enter to continue",Width/2-290,Height/2,"#FFFF00",'c')
        press=pygame.key.get_pressed()
        if press[pygame.K_RETURN]:
            intro_count=3
            p1.reset()
            p2.reset()
        
    elif intro_count<=0:
        keys=pygame.key.get_pressed()
        movement(keys,p1,p2)
        # p1.draw()
    else:
        display_txt(str(intro_count),Width/2-5,Height/2,'#FF0000','c')
        if(abs(pygame.time.get_ticks()-last_count_update)>=1000):
            # print(intro_count)
            intro_count-=1
            last_count_update=pygame.time.get_ticks()
    pygame.display.update()
    clock.tick(fps)

pygame.quit()
quit()