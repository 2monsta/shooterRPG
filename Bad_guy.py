import pygame
from math import hypot
from pygame.sprite import Sprite

class Bad_Guy(Sprite):
	def __init__(self, screen, x ,y ):
		super(Bad_Guy, self).__init__();
		self.image = pygame.image.load("./images/monster1.tiff")
		self.image_group = []
		self.image_group.append(self.image);
		self.image_group.append(pygame.image.load("./images/monster2.tiff"))
		self.index = 0;
		self.x = x;
		self.y = y;
		self.screen = screen;
		self.speed = 4;
	def update_me(self, the_player):
		dx = self.x - the_player.x
		dy = self.y - the_player.y
		dist = hypot(dx,dy)
		dx = dx / dist
		dy = dy / dist
		self.x -= dx * self.speed
		self.y -= dy * self.speed
	def draw_me(self):
		# self.rect.left = self.x
		# self.rect.top = self.y
		self.index +=1;
		if(self.index >= len(self.image_group)):
			self.index = 0;
		self.image = self.image_group[self.index]
		self.screen.blit(self.image, [self.x, self.y])
