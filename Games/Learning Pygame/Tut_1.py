import pygame 
from sys import exit    
'''
so, pygame is a module which basically helps us to draw various images on the screen(just like in animation there   are various frames), take user input. so it can draw a scene on the screen and then take input from the user and then update the screen with a new frame entirely. In a sense pygame can also be used as to create animations or films. The only difference in pygame is that here every frame is not static but dynamic.
''' 

pygame.init()                                 #using this we are calling the pygame class and all of its functions here
screen=pygame.display.set_mode((800,400))     #sets the window size and sets up the window intialization but it is like only one frame or a image so, it disappers after a second

pygame.display.set_caption('My Game')    #sets the title for the window

clock=pygame.time.Clock()                #make a clock obj to set framerates and anything to deal with time

test_surface=pygame.Surface((800,400))   #this is just like label or frame in tkinter

test_surface.fill('#4092c2')               #this is to fill  bg color inside a frame


sky=pygame.image.load(r"C:\Users\Akshay Rathour\Downloads\Untitled design (28).png")   #load the image into window

txt_font=pygame.font.Font(None,50)                       #write a text on the screen
txt_surface=txt_font.render("High Score",False,'red')

chr_img=pygame.image.load(r'C:\Users\Akshay Rathour\Downloads\cartoon-characters-simpsons-png-16.png')  #in these surfaces concert should be used as it makes the game slightly faster by converting the file given into the one compatible with pygame 
c=70
while True:     
    for event in pygame.event.get():     #this line get the condition of the system/game
        if event.type==pygame.QUIT:      
            # pygame.quit()------>       #this line or this whole loop is used to get the screen close,but this gives an error as pyame,quit means that we are cancelling the whole class and thus next line will give error 
            exit() 
    screen.blit(txt_surface,(90,190))
    screen.blit(test_surface,(90,0)) 
    screen.blit(sky,(0,0))              # this is the same as place or pack in tkinter
    screen.blit(chr_img,(c,0))
    c+=10
    if c>=800:
        c=0
    pygame.display.update()             #this updates the whole system window
    clock.tick(60)             #this is used to set the max frame rate on the screen,it means that this while loop will not work more then 60 times a second. 