# We have access to pygame because we sintalled it in  $ pip install pygame
import pygame
import time
from pygame.sprite import Group, groupcollide; #group is the same as list for pygame
from Player import Player #custom classes here
from Bad_guy import Bad_Guy; 
from Bullet import Bullet
from Text import Text;

pygame.init();
screenx = 1000;
screeny = 800;
screen_size =(screenx, screeny);
black = (170, 238, 187)
background_image = pygame.image.load("./images/space.jpg")
background_image_two = pygame.image.load("./images/background2.png");
background_image_two_resized = pygame.transform.scale(background_image_two, [1000,800])
screen = pygame.display.set_mode(screen_size);
pygame.display.set_caption("Hi");
the_player = Player("./images/ff1.tiff", 800, 100, screen) # dont need the image, the x or the y
bad_guy = Bad_Guy(screen, 200, 400);
bad_guy_two = Bad_Guy(screen, 500, 400)
bullets = Group(); #make a new group called bullets, it's a pygame "list";

def message_display(text): #display what kind of text you want
	largeText = pygame.font.Font(None ,115)
	start_text = largeText.render(text, True, (170, 238, 187));
	screen.blit(start_text, [100, 100]);
	pygame.display.update()
def message_players_name(text, name):
	largeText = pygame.font.Font(None ,70)
	story = largeText.render(text, True, (170, 238, 187));
	start_text = largeText.render(name, True, (170, 238, 187));
	screen.blit(start_text, [screenx/2 -125, screeny/2]);
	screen.blit(story, [screenx/2 -350, screeny/2 -50]);
	pygame.display.update()
def game_loop():
	starting_text = True;
	game_on = True;
	tick = 0;
	while game_on: #will run forever until break
		tick+=1; #keeps track of seconds/frames per second
		for event in pygame.event.get(): #loop through all the pygame events, gave it a escape patch
			if event.type == pygame.QUIT:
				game_on = False;
			elif(event.type ==pygame.KEYDOWN): # print("user pressed a key");
				if(event.key == 273):	# user pressed up
					the_player.should_move("up", True);
				elif(event.key == 274):
					the_player.should_move("down", True);
				if(event.key == 275):
					the_player.should_move("right", True);
				elif(event.key == 276):
					the_player.should_move("left", True);
					the_player.transform_image();
				elif(event.key == 32):
					# new_bullet = Bullet(screen, the_player);
					# bullets.add(new_bullet);
					the_player.update();
			elif(event.type ==pygame.KEYUP): 
				if(event.key == 273):	# user pressed up
#================================================================================
#check the goblin game to see how to keep the hero inbound		
					the_player.should_move("up", False);
				elif(event.key == 274):
					the_player.should_move("down", False);
				if(event.key == 275):	
					the_player.should_move("right", False);
				elif(event.key == 276):
					the_player.should_move("left", False);
					the_player.transform_image();
		screen.blit(background_image, [0,0])
		if(starting_text == True): #added welcome player logo at the start of the game.
			message_display("WELCOME PLAYER");
			message_players_name("Welcome Brave Adventurer", "Zack")
			if(tick % 30 == 0):	
				starting_text = False;
		else:

			screen.blit(background_image_two_resized, [0,0])
			bad_guy.update_me(the_player)
#================================================================================
		#need to work on drawing them after and keeps them that way as well as gifing the monster
			bad_guy.draw_me();
		#checking if the player is left or right side, flip the image accordingly
			the_player.draw_me(); # this method draws himself in it's own method instead of bliting on the main game screen
		# for bullet in bullets:
		# 	bullet.update()
		# 	bullet.draw_bullet();
		pygame.display.flip(); #flip the screen so we can draw again and again





game_loop();




