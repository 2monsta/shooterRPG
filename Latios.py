import pygame
from math import hypot
from pygame.sprite import Sprite

class Latios(Sprite):
	def __init__(self, screen, x , y):
		super(Latios, self).__init__();
		self.x = x
		self.y = y
		self.screen = screen;
		self.image_original = pygame.image.load("./images/latios.png");
		self.image = pygame.transform.scale(self.image_original, [50,50]);
		self.image_original_flip = pygame.transform.flip(self.image_original, True, False);
		self.image_original_flip_scale = pygame.transform.scale(self.image_original_flip,[50, 50])
	def fly(self):
		self.x -= 5;
	def draw_me(self):
		self.screen.blit(self.image, [self.x, self.y])
	def fly_two(self):
		self.x +=5
		self.screen.blit(self.image_original_flip_scale, [self.x, self.y])