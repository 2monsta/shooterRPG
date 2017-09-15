# We have access to pygame because we sintalled it in  $ pip install pygame
import pygame
from Player import Player #custom classes here
from Bad_guy import Bad_Guy; 

pygame.init();

screenx = 1000;
screeny = 800;
screen_size =(screenx, screeny);
background_color = (82, 111, 53) # it's because we are going to pain abckground , we need a tuple
screen = pygame.display.set_mode(screen_size);
pygame.display.set_caption("Hi");
the_player = Player("./images/tidus.jpg", 800, 100, screen) # dont need the image, the x or the y
bad_guy = Bad_Guy(screen);


game_on = True;
while game_on: #will run forever until break
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
		elif(event.type ==pygame.KEYUP): 
			if(event.key == 273):	# user pressed up	
				the_player.should_move("up", False);
			elif(event.key == 274):
				the_player.should_move("down", False);
			if(event.key == 275):	
				the_player.should_move("right", False);
			elif(event.key == 276):
				the_player.should_move("left", False);
	screen.fill(background_color); #pain the screen, no need for blit because we are not drawing over another picture
	bad_guy.update_me(the_player)
	bad_guy.draw_me();
	the_player.draw_me(); # this method draws himself in it's own method instead of bliting on the main game screen
	pygame.display.flip(); #flip the screen so we can draw again and again






