import pygame 
import logic 
pygame.init()
pygame.font.init()
clock=pygame.time.Clock() 
#screen = pygame.display.set_mode((800, 600),pygame.RESIZABLE)
screen = pygame.display.set_mode((500,400),pygame.RESIZABLE)

running=True 
frame_rate=10  
#Setting varables 
bg_color=((100,100,100))

# functions  
#def buttion (x,y,rect, ) : 
 
#def per2pix (part,whole): 
        
def square (x=100,y=100,width=100,height=100,color=(150,150,150)): 
    
    #square = pygame.Rect(x,y,height,width)
    pygame.draw.rect(screen,color,(x,y,height,width)) 
    #    pygame.draw.rect(screen, color, (x, y, width, height))

while running:  
    print(screen) 
    screen.fill(bg_color) 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 

# screen dimetions, 500,400

    #bg color squares for each segment of the program
    # snake preview, arrow array, tital     
    square(10,70,200,370,(10,240,200))
    
    #top right exit button 
    square(100,100,100,100,(10,240,200))    
    #large start button bottom left   
    square(450,350,100,100,(190,255,190))    
    #top right  array of sliders for color  
    square(10,10,30,20,(220,170,190))    
    #and then addes the arrow buttons   

    square(213,32,10,10,(230,25,190))
    square(213,32,10,10,(230,25,190)) 

    # arrows for:
    # mode, color of gb and snake, costumes, gm speed, gm mode,   

    # left has snake 

    # top right shows the gamemode and color 
  
    # draw text 

    logic.draw_text(screen,"round the chesse",80,139) 

    pygame.display.update()
    clock.tick(frame_rate)
pygame.quit() 