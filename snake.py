import pygame
import random
import time 
import asyncio 
import logic  
pygame.init()
clock=pygame.time.Clock()
pygame.font.init() 
c_time=time.ctime()
m_time=time.perf_counter()
framerate=60
running=True 
screen=pygame.display.set_mode((500,400), pygame.RESIZABLE)
bg_color="teal"
grid={} 
score=0
speed=0.1 
game_mode="df" 
gam_modes=["df","df(again)","still df","always df"]
game_size= 8
game_color="df" 
snake_color="df"
flags=["home_screen"]
apples=[]
max_apples=5 
snake={"2,3":1,"2,4":1,"2,5":1}
player_square=pygame.Rect(50,50,50,50)

# ---importing images 

try:  
	##snake_tital= pygame.image.load("").convert_alpha()
	cheacker_bg=  pygame.image.load("pygame-snake\green_grid -1.png.png").convert_alpha()
	#snake_head= pygame.image.load("").convert_alpha()
	#snake_body= pygame.image.load("").convert_alpha()
	#snake_tail= pygame.image.load("").convert_alpha()
	apple=pygame.image.load("pygame-snake/apple-1.png.png").convert_alpha()
except:
	print("a image could not be found :(")
#screen.blit(player_sprite, (100, 150)) 

#         ----------functions 

def reset_snake (): 
	# sets the defalt vaules of the eviroment and snake 
	pygame.time.wait(300)
	global grid  
	global snake       
	grid={} #empty to be set later 
	snake={"2,3":1,"2,4":1,"2,5":1}
	#  pair of numbers are coordiates, the number represents the direction of 
	# the snake segments  
  
def reset_grid (grid):    
	#  makes emity coordinate vaules to fill the grid 
	for I in range(int((screen.width/50*(screen.height/50)))) :
		item={f"{I%10},{int(I/10)}":""} 
		grid.update(item)
	#product of snake/grid indision

def reset_apple ():
	global apples
	apples=[]
	for i in range(max_apples):
		apples.append(f"{random.randrange(0,int(screen.width/50))},{random.randrange(0,int(screen.height/50))}")
   
	print(f"max apples {max_apples}")

def add_apple (snake, apples):
	# takes random cordinates and adds it to the grid
	coordinates= f"{random.randrange(0,int(screen.width/50))},{random.randrange(0,int(screen.height/50))}"  
	i=0 
	while coordinates in snake or coordinates in apples:
		coordinates= f"{random.randrange(0,int(screen.width/50))},{random.randrange(0,int(screen.height/50))}"  
		i+=1
		print(f"try: {i}")
	else: 
		print (f"new apple: {coordinates}")
		return apples.append(coordinates)
 
def pos_get(stre):   
	 # used to  convert the coordinate string into intergers for rendering  
	x_y=[0,0]
	L=""# a portion of the string containg the numbers 
	#Another varable may not be needed to solve the problems
	for i in stre: 

		if not i == ",":
			L=L+i  
		else: 
			x_y[0]=int(L)
			x_y[1]=int(stre[len(str(x_y[0]))+1:len(stre)])
			#print (x_y)  
			return x_y

# logic functions

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

def draw_text(text, x, y, color=(0, 0, 0),font="df"):
    n_font=fonts_li(font) 
    print(f" text: { text }")
    text_surface = n_font.render(text, True, color)  
    screen.blit(text_surface, (x,y)) 


def button(x, y, width, height, text, color=(0, 0, 0), text_color=(255, 255, 255),font="df"):
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

def per2pix (percent,whole="s_w"):
	m_whole=whole
	
	if whole == "s_w":
		m_whole=screen.get_width()
	elif whole == "s_h":
		m_whole = screen.get_height()
	else: 
		print(f" {whole} is an invalid input ")
		
	print (f" per: {percent} m_whole ")
	return int( (percent / 100) * m_whole)

reset_grid(grid)# makes the grid 
reset_apple()
#       --------- game loop 

while running:
  
	screen.fill(bg_color)
	for event in pygame.event.get(): # -------        event loop
		if event.type==pygame.QUIT: 
			running=False   
   
	if "home_screen" in flags:
		bg_color="lime green"
		try:

			sc_chearker = pygame.transform.scale(cheacker_bg, (screen.width()+ per2pix(1),screen.width()+ per2pix(1)))
			
			chearker_bg_rect=cheacker_bg.get_rect()
			screen.blit(sc_chearker,chearker_bg_rect,screen.get_rect())
		except:
			pass
		draw_text("snake.py",per2pix(20),per2pix(20,"s_h"),(128,230,185),"t1") 
		if button(per2pix(30),per2pix(65,"s_h"),per2pix(30),per2pix(10,"s_h"),"Play!", (20,180,200),(180,250,230)) :
			print("button pressed ")
			flags=[] 
			flags.append("snake")
			reset_apple()
		if button(per2pix(30),per2pix(75,"s_h"),per2pix(30),per2pix(10,"s_h"),"settings",(20,180,200), (180,250,230)):
			flags=[] 
			flags.append("settings")
		if button(per2pix(30),per2pix(85,"s_h"),per2pix(30),per2pix(10,"s_h"),"quit",(255,180,200), (180,250,230)):
			running=False

	elif "settings" in flags:  
		bg_color="khaki"
		draw_text("settings",per2pix(30),per2pix(8,"s_h"))
        # exit button 
		if button(per2pix(1),per2pix(1,"s_h"),per2pix(3),per2pix(3,"s_h"),"<", (250,100,160),(100,100,100)):
			flags=[]
			flags.append("home_screen")

		# max apples 
		draw_text(f"max apples : {max_apples}",per2pix(35) ,per2pix(15,"s_h"))
		if button(per2pix(30),per2pix(15,"s_h"),per2pix(5),per2pix(5,"s_h"), "<", (200,150,200 ),(255,180,180 ) ):
			max_apples-=1
		if button(per2pix(75),per2pix(15,"s_h"),per2pix(5),per2pix(5,"s_h"),">",(200,150,200),(255,180,180)):
			max_apples+=1 

		#modes:
		#- fliping snake - dashed snake  -   	
		if button( per2pix(30),per2pix(60,"s_h"),per2pix(5),per2pix(5,"s_h"),f" snake color: { snake_color }"):
			snake_color="purple"
		if button(per2pix(30),per2pix(75,"s_h"),per2pix(5),per2pix(5,"s_h"),f" grid color: {game_color}"):
			game_color="green"
		#snake color
		#- needs shading

		# game size
		draw_text(f"Game Size : {game_size}",per2pix(35),per2pix(30))
		if button(per2pix(30),per2pix(30,"s_h"),per2pix(5),per2pix(5,"s_h"), "<", (200,150,200 ),(255,180,180 ) ):
			game_size-=1
		if button(per2pix(70),per2pix(30,"s_h"),per2pix(5),per2pix(5,"s_h"), ">", (200,150,200 ),(255,180,180 ) ):
			game_size+=1
		if button(per2pix(30),per2pix(45,"s_h"),per2pix(5),per2pix(5),f"gamemode: {game_mode}"):
			if gam_modes.index(game_mode)== len(gam_modes):
				game_mode = gam_modes[-1]
			else:
				game_mode= gam_modes[gam_modes.index(game_mode)+1]

		# game speed 
		draw_text(f"game speed: {speed}", per2pix(35),per2pix(95,"s_h"))
		if button(per2pix(30),per2pix( 95 ,"s_h"),per2pix(5),per2pix(5,"s_h"),"<"):
			if not speed-0.1 < 0.1 :
				speed+=-0.1
		if button(per2pix(70),per2pix( 95 ,"s_h"),per2pix(5),per2pix(5,"s_h"),">"):
			speed+=0.1
	
	
	elif "game_over" in flags:
		bg_color="orange"
		draw_text("Game Over", per2pix(15), per2pix(10,"s_h"),(130,233,199),"t2")
		draw_text(f"score: {score}",per2pix(5),per2pix(20,"s_h"))

		if button(per2pix(30),per2pix(40,"s_h"),per2pix(25),per2pix(10,"s_h"),"replay?",(34,234,122),(122,34,200)):
			print("retry")
			score=0
			flags=[]
			flags.append("snake") 
			reset_apple()
			reset_snake()
     
		if button(per2pix(30),per2pix(20,"s_h"),per2pix(25),per2pix(10,"s_h"),"settings",(205,123,145),(100,244,253)):
			print("settings") 
			flags=[]
			flags.append("settings")


		if button(per2pix(30),per2pix(80,"s_h"), per2pix(25), per2pix(10, "s_h"), "Quit", (21,123,104),(229,200,135)):
			print("quit")
			flags=[]
			running =False
	
	
	elif "snake" in flags :
		bg_color="teal"
 
		if "begin" in flags:  
			keys=pygame.key.get_pressed() # 	arrow key input 
			if keys[pygame.K_DOWN]and not snake[list(snake.keys())[0]]==1:
				print("down")
				snake[list(snake.keys())[0]]=3
			if keys[pygame.K_UP]and not snake[list(snake.keys())[0]]==3 :
				snake[list(snake.keys())[0]]=1
				print("up")
			if keys[pygame.K_LEFT]and not snake[list(snake.keys())[0]]==2: 
				print("left") 
				snake[list(snake.keys())[0]]=4	
			if keys[pygame.K_RIGHT] and not snake[list(snake.keys())[0]]==4:
				snake[list(snake.keys())[0]]=2
				print("right")

			for x in list(snake.keys()) : # The placement of the snake segments 
				# loops though the snake list and renders it   
				if snake[x] ==1:
					x_y=pos_get(x)
					player_square.x=x_y[0]*50
					player_square.y=x_y[1]*50
					pygame.draw.rect(screen,(30,190,250),player_square)	
				elif snake[x] ==2:
					x_y=pos_get(x)
					player_square.x=x_y[0]*50
					player_square.y=x_y[1]*50
					pygame.draw.rect(screen,(60,150,210),player_square)
				elif snake[x] ==3:
					x_y=pos_get(x)
					player_square.x=x_y[0]*50
					player_square.y=x_y[1]*50
					pygame.draw.rect(screen,(80,110,170),player_square)
				elif snake[x] ==4:
					x_y=pos_get(x)
					player_square.x=x_y[0]*50
					player_square.y=x_y[1]*50
					pygame.draw.rect(screen,(100,70,130),player_square)
 
			x_y=pos_get(list(snake.keys())[0]) 
			#print(list(snake.keys())[0])   
		else:
			keys=pygame.key.get_pressed() # 	arrow key input 
			if keys[pygame.K_DOWN]and not snake[list(snake.keys())[0]]==1: 
				flags.append("begin")
				x_y=pos_get(list(snake.keys())[0]) 
			if keys[pygame.K_UP]and not snake[list(snake.keys())[0]]==3 :
				flags.append("begin")
				x_y=pos_get(list(snake.keys())[0]) 
			if keys[pygame.K_LEFT]and not snake[list(snake.keys())[0]]==2: 
				flags.append("begin")
				x_y=pos_get(list(snake.keys())[0]) 
			if keys[pygame.K_RIGHT] and not snake[list(snake.keys())[0]]==4:
				flags.append("begin")
				x_y=pos_get(list(snake.keys())[0]) 

			draw_text("press a arrow key to start",per2pix(0),per2pix(10,"s_h"),(204,29,123),"t2")
			
   
			# add arrow check
		if "begin" in flags and time.perf_counter() > m_time:
			print(f"c_time: {time.perf_counter()} , speed: {speed}")
			m_time=time.perf_counter()+speed
			#    ---- uses python frount segmnet to move or extend snake 
			if snake[f"{x_y[0]},{x_y[1]}"]==1: 
				#  checks if the snake colides with apple and walls  
				if f"{x_y[0]},{x_y[1]-1}" in list(grid.keys()) and not f"{x_y[0]},{x_y[1]-1}" in list(snake.keys()):
					# the goal is to get the new portion of the snake added and to remove the last portion of the snake
					L={f"{x_y[0]},{x_y[1]-1}":1}
					snake= L | snake  
					if not list(snake.keys())[0] in apples:
						del snake[list(snake.keys())[-1]]  
					else:
						score+=1
						apples.remove(list(snake.keys())[0]) 
						add_apple(snake,apples)
				else:
					flags.append("game_over")

			# repeated from the last 
			elif snake[f"{x_y[0]},{x_y[1]}"]==2:   
				if f"{x_y[0]+1},{x_y[1]}" in list(grid.keys()) and not f"{x_y[0]+1},{x_y[1]}" in list(snake.keys()):
					L={f"{x_y[0]+1},{x_y[1]}":2}
					snake=L | snake
					if not list(snake.keys())[0] in apples:  
						del snake[list(snake.keys())[-1]]
					else:  
						score+=1
						apples.remove(list(snake.keys())[0])
						add_apple(snake,apples)
				else:
					flags.append("game_over") 

			elif snake[f"{x_y[0]},{x_y[1]}"]==3:
				if f"{x_y[0]},{x_y[1]+1}" in list(grid.keys()) and not f"{x_y[0]},{x_y[1]+1}" in list(snake.keys()):
					L={f"{x_y[0]},{x_y[1]+1}":3}
					snake=L | snake
					if not list(snake.keys())[0] in apples:
						del snake[list(snake.keys())[-1]]
					else:
						score+=1
						apples.remove(list(snake.keys())[0])
						add_apple(snake,apples)
				else:
					flags.append("game_over") 

			#repeated for the last type of segment 
			elif snake[f"{x_y[0]},{x_y[1]}"]==4:
				if f"{x_y[0]-1},{x_y[1]}" in list(grid.keys()) and not f"{x_y[0]-1},{x_y[1]}" in list(snake.keys()):
					L={f"{x_y[0]-1},{x_y[1]}":4}
					snake=L | snake
					if not list(snake.keys())[0] in apples: 
						del snake[list(snake.keys())[-1]]
					else: 
						score+=1
						apples.remove(list(snake.keys())[0])
						add_apple(snake,apples)
				else:  
					flags.append("game_over") 
		if "begin" in flags:
			# renders the apples 
			for x in apples: 
				x_y=pos_get(x)
				player_square.x=x_y[0]*50
				player_square.y=x_y[1]*50
				try:  # image 
					sc_apple = pygame.transform.scale(apple, (50,50))
					screen.blit(sc_apple,player_square)
				except:  
					pygame.draw.rect(screen,(240,110,170),player_square)


	pygame.display.flip()
	reset_grid(grid)
	clock.tick(framerate)
pygame.quit()