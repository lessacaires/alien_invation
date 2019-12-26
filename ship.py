import pygame
from settings import Settings

class Ship():
	
	def __init__(self, ai_settings, screen):
		"""Inicializa a  espaçonave e define sua posição inicial."""
		self.screen = screen
		self.ai_settings = ai_settings
		
		#Carrega a imagem da espaçonave e obtém seu rect
		self.image = pygame.image.load('images/ship.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		
		#Inicia cada nova espaçonave na parte inferior da tela
		self.rect.centerx = self.screen_rect.bottom
		self.rect.bottom = self.screen_rect.bottom
		
		#Armazena um valor decimal para o centro da espaçonave
		self.centerx = float(self.rect.centerx)
		self.centery = float(self.rect.centery)
		
		
		#Flag de movimento
		self.moving_right = False
		self.moving_left = False
		self.moving_up = False
		self.moving_down = False		
		
	def update(self):
		"""Atualiza a posição da espaçonave de acordoc com a flag de movimento."""
		#Atualiza o  valor do centro da espaçonave, e não o retângulo
		#Limita a movimentação da espaçonave o final do lado direito da tela
		if self.moving_right and self.rect.right < self.screen_rect.right:
			if self.moving_right:
				self.centerx += self.ai_settings.ship_speed_factor
		#Limita a movimentação da espaçonave até o final do lado esquerdo da tela
		if self.moving_left and self.rect.left > 0:
			if self.moving_left:
				self.centerx -= self.ai_settings.ship_speed_factor	
		#Limita a movimentação da espaçonave até o final da parte superior da tela
		if self.moving_up and self.rect.top > 0:
			if self.moving_up:
				self.centery -= self.ai_settings.ship_speed_factor
		#Limita a movimentação da espaçonave até o final da tela
		if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
			if self.moving_down:
				self.centery += self.ai_settings.ship_speed_factor	
		
		#Atualiza o objeto rect de acordo com o self.center
		self.rect.centerx = self.centerx
		self.rect.centery = self.centery
		
	def blitme(self):
		"""Resdesenha a espaçonave em sua posição atual."""
		self.screen.blit(self.image, self.rect)

	def center_ship(self):
		"""Centraliza a espaçonave na tela."""
		self.center = self.screen_rect.centerx
