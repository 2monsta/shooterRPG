import pygame # We have access to pygame because we sintalled it in  $ pip install pygame
import time
from pygame.sprite import Group, groupcollide; 
from Player import Player #custom classes here
from Bad_guy import Bad_Guy; 
from Bullet import Bullet
from Latios import Latios
import random
import sys


#====================INITING Everything==============================
pygame.init();
pygame.mixer.init()
pygame.mixer.music.load("./music/price_of_freedom.mp3")
pygame.mixer.music.play()
#====================================================================
#====================All the Variables===============================
#====================================================================
back_image_long = pygame.image.load("./images/space_long.png");
bomb_sound= pygame.mixer.Sound("./music/bomb.wav")
bomb_sound.set_volume(0.25);
screenx = 500;
screeny = 400;
screen_size =(screenx, screeny);
black = (170, 238, 187)
background_image = pygame.image.load("./images/space.jpg")
background_image_two = pygame.image.load("./images/background3.png");

background_image_two_resized = pygame.transform.scale(background_image_two, [500,400])
screen = pygame.display.set_mode(screen_size);
pygame.display.set_caption("Hi");
the_player = Player("./images/ff1.tiff", 100, 300, screen) # dont need the image, the x or the y
bad_guy = Bad_Guy(screen, 300, 335);
latios = Latios(screen, 300, 50);
latios_two = Latios(screen, 100, 50);

#====================All the Groups for sprites====================
bullets = Group(); #make a new group called bullets, it's a pygame "list";
hero_group = Group();
enemy_group = Group();
hero_group.add(the_player);
enemy_group.add(bad_guy);

#====================All the functions==============================
def message_display(text): #display what kind of text you want
	largeText = pygame.font.Font(None ,30)
	start_text = largeText.render(text, True, (170, 238, 187));
	screen.blit(start_text, [100, 100]);
	pygame.display.update()

def message_players_name(text, name):
	largeText = pygame.font.Font(None ,30)
	story = largeText.render(text, True, (170, 238, 187));
	start_text = largeText.render(name, True, (170, 238, 187));
	screen.blit(start_text, [screenx/2 -125, screeny/2]);
	screen.blit(story, [screenx/2 -100, screeny/2 -50]);
	pygame.display.update()
def check_collision():
	pygame.sprite.groupcollide(hero_group, enemy_group, False, True);
	col = pygame.sprite.groupcollide(hero_group, bullets, True, False);
	# if col:
	# 	sys.exit();
		
def health():
	text = pygame.font.Font(None, 20);
	healt_c = text.render("HEALTH_COUNT: %d" % the_player.health, True, (0, 0, 0))
	monster_killed = text.render("Monster Killed: %d" %bad_guy.bad_guy_count, True, (0, 0, 0));
	screen.blit(healt_c, [100, 50])
	screen.blit(monster_killed, [100, 70])


#====================================================================
#====================Main Game Function==============================
#====================================================================
def game_loop():
	starting_text = True;
	game_on = True;
	tick = 0;
	last_bullet_drop = time.time()
	x = 0;
	while game_on: #will run forever until break
		tick+=1; #keeps track of seconds/frames per second
#====================Event Handling==============================		
		for event in pygame.event.get(): #loop through all the pygame events, gave it a escape patch
			if event.type == pygame.QUIT:
				game_on = False;
			elif(event.type ==pygame.KEYDOWN): 
				# if(event.key == pygame.K_w):
				# 	the_player.should_move("up", True);
				# elif(event.key == pygame.K_s):
				# 	the_player.should_move("down", True);
				if(event.key == pygame.K_d):
					the_player.should_move("right", True);
				elif(event.key == pygame.K_a):
					the_player.should_move("left", True);
					the_player.transform_image();
				elif(event.key == 32): # this use to be elif
					the_player.jump(True);
				elif(event.key == pygame.K_c):
					the_player.swinging = True;
			elif(event.type ==pygame.KEYUP): 
				# if(event.key == pygame.K_w):	
				# 	the_player.should_move("up", False);
				# elif(event.key == pygame.K_s):
				# 	the_player.should_move("down", False);  
				if(event.key == pygame.K_d):	
					the_player.should_move("right", False);
				elif(event.key == pygame.K_a):
					the_player.should_move("left", False);
					the_player.transform_image();
				elif(event.key == 32): # this use to be elif
					the_player.jump(False);
				elif(event.key == pygame.K_c):
					the_player.swinging = False;
#====================================================================
#====================Drawing Everything==============================
#====================================================================					
		screen.blit(background_image, [0,0])
		if(starting_text == True): #added welcome player logo at the start of the game.
			message_display("WELCOME PLAYER");
			message_players_name("Welcome Brave Adventurer", "Zack")
			if(tick % 30 == 0):	
				starting_text = False;
		else:
#====================Image Moving========================================
			rel_x = x % back_image_long.get_rect().width;
			screen.blit(back_image_long, [rel_x - back_image_long.get_rect().width, 0])
			if( rel_x < 500):
				screen.blit(back_image_long, [rel_x, 0])
			x -= 1
#====================Looping through enemy group========================================
			for i in enemy_group: #this moves the bad_guy in the enemy group towards the hero
				i.update_me(the_player)
			if(len(enemy_group)== 0): #checks to see if anyone is in the enemy group
				bad_guy.bad_guy_count+=1;
				bad_guy_new = Bad_Guy(screen, 300, 335) #if there isnt, make a new bad guy
				bad_guy_new.draw_me(); #draw him
				enemy_group.add(bad_guy_new); #add him to the bad guy group
			else:
				for bad in enemy_group: #checks the enemy group, for anyhting
					bad.draw_me(); #if there is, draw something, if not don't draw.
#====================Drawing the bullets and have latios drop them====================			
			new_bullet = Bullet(screen, latios);
			new_bullet_2 = Bullet(screen, latios_two);
			if(time.time() > last_bullet_drop + 2):
				bullets.add(new_bullet);
				bullets.add(new_bullet_2);
				last_bullet_drop = time.time()
#====================Draw the player and check for collision====================
			the_player.update()
			the_player.draw_me();
			check_collision();
			health();
#====================Draws latios========================================
			if(latios.x < 0 ):
				latios.x = 900;
			else:
				latios.fly();
				latios.draw_me();
			if(latios_two.x > 500):
				latios_two.x = 0;
			else:
				latios_two.fly_two();
#====================Lopping Through bullets and drop them====================				
		for bullet in bullets:
			bullet.update()
			bullet.draw_bullet();
			check_collision();
			#if bullet's y is > 550, and the bullet index is at 14 meaning the explosion reached the last image, then remove the bullets from
			#the group
			if(bullet.y >= 250 and bullet.index ==14): #keeping the bullets at the stop    
				if(bullet.y == 250):
					bomb_sound.play();
				bullets.remove(bullet);
		pygame.display.flip();
game_loop();




#TODO: make collision between hero pixels correct
#TODO: check the image for flipping