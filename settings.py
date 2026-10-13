import pygame 
import math
pygame.init()
running=True 
time=pygame.time.Clock() 
screen=pygame.screen.setmode(500,400)
# makes window scalable

#setting varables 
def_text=pygame.font 
settings={"s_color":(120,240,120),"sn_cost":"def","gm_speed":1,"ap_fre":0.5, "gm_size":5,"gm_color":(200,250,200),"gm_angle":90,"gm_zoom":1,"gm_mode","gm_x":0,"gm_y":0}
          

#functtions
def buttions (x,y,rect,color):

# checks if using an image 
# creates the rect
# checks for collision 
# renders acordenly 


#array of if conditions for font
# makes the text object
#renders the text using pyagme

def draw_text (x,y,text="",type="def", size=5):

def animation (x,y,type, strength,offset ):
    global time
    # array of if conditons 
    # uses time and math to get a movement
    # in addtion to a offset
    # returnes xy vaules intrelation to the originobal xy

def per2pix (vaule,whole="h_l"):

# checks what type of vaule is used for whole
# then reasines the vaule for whole 
# divides the whole by a portion,
# rember to turn it into a int
#

def  


while running :

    for event in pygame.event.get():
        if event.type == pyagme.quit():
            running = False 
        
    # loads background
    screen.fill(bg_color)
    # use shaders? to make bg image 

    #loads images and buttons
    #renders text
    #arrow buttons
    
    # array of 


pygame.clock.
pygame.screen.flip()

    