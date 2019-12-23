import sys

import pygame

#Importa os metodos da classe Settings
from settings import Settings

#Importa os métodos da classe ship
from ship import Ship

from pygame.sprite import Group


#Gerencia os eventos do game
import game_functions as gf

def run_game():
	
		#Inicializa o jogo e cria um objeto para a tela
		pygame.init()
		ai_settings = Settings()
		
		screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
		pygame.display.set_caption("Alien Ivasion")
		
		#Cria uma espaçonave
		ship = Ship(ai_settings, screen)
		
		#Cria um grupo no qual serão armazenados os projeteis 
		bullets = Group()
		
		#Inicia o laço principal do jogo
		while True:
			
			#Observa eventos de teclado e de mouse
			gf.check_events(ai_settings, screen, ship, bullets)
			
			ship.update()
			gf.update_bullets(bullets)
			
			#Redesenha a tela a cada passagem pelo laço
			gf.update_screen(ai_settings, screen, ship, bullets)
						
			#Deixa a tela mais recente visivel
			pygame.display.flip()
			
run_game()
