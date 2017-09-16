import pygame
from pygame.sprite import Sprite
class Player(Sprite):
	def __init__(self, image,start_x, start_y, screen):
		super(Player,self).__init__(); #because it's a subclass, you have to call the parent class Sprite
		self.image = pygame.image.load(image);
		self.x = start_x;
		self.y = start_y;
		self.speed = 10;
		self.screen = screen;
		self.should_move_up = False;
		self.should_move_down = False;
		self.should_move_left = False;
		self.should_move_right = False;
		self.image_group = [];
		self.index = 0;
		self.image_group.append(pygame.image.load("./images/ff2.tiff"))
		self.image_group.append(pygame.image.load("./images/ff3.tiff"))
		self.image_group.append(pygame.image.load("./images/ff4.tiff"))
		self.image_group.append(pygame.image.load("./images/ff5.tiff"))

	def draw_me(self):
		if(self.should_move_up):
			self.y -= self.speed;
		elif(self.should_move_down):
			self.y += self.speed;
		if(self.should_move_left):
			self.x -= self.speed;
		elif(self.should_move_right):
			self.x += self.speed;
		self.screen.blit(self.image, [self.x, self.y]);

	def should_move(self, direction, yes_or_no):
		if(direction =="up"):
			self.should_move_up = yes_or_no; #the key is down, update itself;
		if(direction =="down"):
			self.should_move_down = yes_or_no;
		if(direction =="left"):
			self.should_move_left = yes_or_no;
		if(direction =="right"):
			self.should_move_right = yes_or_no;
	def transform_image(self):
		self.image = pygame.transform.flip(self.image, True, False);
		self.screen.blit(self.image, [self.x, self.y])

	def update(self): #change directions!
		self.index +=1;
		if(self.index >= len(self.image_group)):
			self.index = 0;
		self.image = self.image_group[self.index]
		self.screen.blit(self.image, [self.x, self.y])


