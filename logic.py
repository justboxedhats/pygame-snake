import pygame 
pygame.init()
pygame.font.init()

"""
Containts many functions 
"""

# functions

def button(screen,x, y, width, height, text, color=(0, 0, 0), text_color=(255, 255, 255),font="df"):
    n_font=fonts_li(font)
    pygame.draw.rect(screen, color, (x, y, width, height))
    text_surface = n_font.render(text, True, text_color)
    text_rect = text_surface.get_rect(center=(x + width / 2, y + height / 2))
    button_rect = pygame.Rect(x,y,width,height)
    screen.blit(text_surface, text_rect)
    if button_rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_just_pressed()[0]:
        #if "clicked" not in flags: 
        #    flags.append("clicked")   
        return True
    else: return False   


# checks if using an image 
# creates the rect
# checks for collision 
# renders acordenly 

 
def fonts_li (str="df"):
        #print("loading font fuction") 
    if str == "df":
        return pygame.font.SysFont("Arial", 20)
    elif str == "t1" :
        return pygame.font.SysFont("Arial", 65, True ,False)
    elif str == "t2" :
        return pygame.font.SysFont("Arial", 50, True ,False)
    elif str == "t3" :
        return pygame.font.SysFont("Arial", 30, True ,False)
    elif str == "sp1" :
        return pygame.font.SysFont("Arial", 25, True ,False)
    elif str == "sp2" :
        return pygame.font.SysFont("Arial", 50, True ,False)
    else:
        print(f" {str} not in libary ")

def draw_text(screen,text, x, y, color=(0, 0, 0),font="df"):
    n_font=fonts_li(font) 
    print(f" text: { text }")
    text_surface = n_font.render(text, True, color)  # error here
    screen.blit(text_surface, (x,y)) 
    

#array of if conditions for font
# makes the text object
#renders the text using pyagme



def animation (x,y,type, strength,offset ):
    global time
    if type=="noise": 
        print="noise"
        # return 
    elif type== "sine_sway" :
        print="sine_sway"

    elif type== "sine_bounce":
        print="sine_bounce"
    elif type == "sqush_flip":
        print="squish_flip"
        
    else: 
        print("shader type not reconized")
    
    # array of if conditons 
    # uses time and math to get a movement
    # in addtion to a offset
    # returnes xy vaules intrelation to the originobal xy

def per2pix (percent,whole="h_l"):
    m_whole=whole

    if whole == "s_w":   
        m_whole=screen.get_width()
    elif whole == "s_h":
        m_whole = screen.get_height()
    
    return int( (percent / 100) * m_whole)

# checks what type of vaule is used for whole
# then reasines the vaule for whole 
# divides the whole by a portion,
# rember to turn it into a int
#
