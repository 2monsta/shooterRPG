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
		self.last_bullet_drop = time.time();
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
	def add_bullets(self):
		if(time.time() > last_bullet_drop + 1):
			bullets.add(new_bullet);
			last_bullet_drop = time.time()
