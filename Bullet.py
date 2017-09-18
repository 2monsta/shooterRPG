import pygame
from pygame.sprite import Sprite
import time;

class Bullet(Sprite):
	def __init__(self,screen, the_player):
		super(Bullet,self).__init__();
		self.screen = screen;
		self.image_original = pygame.image.load("./images/tordepdo.png");
		self.image = pygame.transform.scale(self.image_original, [70,70])
		self.rect = pygame.Rect(0,0,5,20);
		self.color= (0,0,0);
		self.speed = 15;
		self.direction = 3;
		self.rect.centerx = the_player.x
		self.rect.top = the_player.y
		self.x = self.rect.x;
		self.y = self.rect.y;
		self.index =0;
		self.explosion_list = []
		self.image_exposion_one = pygame.image.load("./images/exp1.png")
		self.explosion_list.append(self.image_exposion_one);
		self.image_exposion_two = pygame.image.load("./images/exp2.png")
		self.explosion_list.append(self.image_exposion_two);
		self.image_exposion_three = pygame.image.load("./images/exp3.png")
		self.explosion_list.append(self.image_exposion_three);
		self.image_exposion_four = pygame.image.load("./images/exp4.png")
		self.explosion_list.append(self.image_exposion_four);
		self.image_exposion_five = pygame.image.load("./images/exp5.png")
		self.explosion_list.append(self.image_exposion_five);
		self.image_exposion_six = pygame.image.load("./images/exp6.png")
		self.explosion_list.append(self.image_exposion_six);
		self.image_exposion_seven = pygame.image.load("./images/exp7.png")
		self.explosion_list.append(self.image_exposion_seven);
		self.image_exposion_eight = pygame.image.load("./images/exp8.png")
		self.explosion_list.append(self.image_exposion_eight);
		self.image_exposion_nine = pygame.image.load("./images/exp9.png")
		self.explosion_list.append(self.image_exposion_nine);
		self.image_exposion_ten = pygame.image.load("./images/exp10.png")
		self.explosion_list.append(self.image_exposion_ten);
		self.image_exposion_eleven = pygame.image.load("./images/exp11.png")
		self.explosion_list.append(self.image_exposion_eleven);
		self.image_exposion_twlve = pygame.image.load("./images/exp12.png")
		self.explosion_list.append(self.image_exposion_twlve);
		self.image_exposion_thridteen = pygame.image.load("./images/exp13.png")
		self.explosion_list.append(self.image_exposion_thridteen);
		self.image_exposion_fourteen = pygame.image.load("./images/exp14.png")
		self.explosion_list.append(self.image_exposion_fourteen);
		self.image_exposion_fithteen = pygame.image.load("./images/exp15.png")
		self.explosion_list.append(self.image_exposion_fithteen);
		self.explosion_bool = False;

	def update(self):
		if self.direction == 1: #up
			self.y -= self.speed #change the y, each time update is run, by bullet speed
			self.rect.y = self.y #update rect position
		elif self.direction == 2: #right
			self.x += self.speed #change the y, each time update is run, by bullet speed
			self.rect.x = self.x #update rect position
		elif self.direction == 3: #down
			self.y += self.speed #change the y, each time update is run, by bullet speed
			self.rect.y = self.y #update rect position
		else: #left
			self.x -= self.speed #change the y, each time update is run, by bullet speed
			self.rect.x = self.x #update rect position
	def draw_bullet(self):
		#pygame.draw.rect(self.screen, self.color, self.rect) #draw the bullet!
		self.screen.blit(self.image, [self.x, self.y])
		if(self.y > 600):
			self.y = 600
			self.index +=1;
			if(self.index>=len(self.explosion_list)):
				self.index =0;
			self.image = self.explosion_list[self.index]
			self.screen.blit(self.image, [self.x, self.y])
			self.screen.blit(self.image, [-100, -10 ]);