import sys

import pygame

#Importa os metodos da classe Settings
from settings import Settings

#Importa os métodos da classe ship
from ship import Ship

from pygame.sprite import Group
from alien import Alien

#Gerencia os eventos do game
import game_functions as gf

#Gerencia as estatisticas do game
from game_stats import GameStats

#Gerencia a classe button
from button import Button

from scoreboard import ScoreBoard

def run_game():
	
		#Inicializa o jogo e cria um objeto para a tela
		pygame.init()
		ai_settings = Settings()
		
		screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
		pygame.display.set_caption("Alien Ivasion")
		
		#Cria o botão play
		play_button = Button(ai_settings, screen, "Play")
		
		#Cria uma espaçonave
		ship = Ship(ai_settings, screen)
		
		#Cria um grupo no qual serão armazenados os projeteis 
		bullets = Group()
		aliens = Group()
				
		#Cria uma frota de aienígenas
		gf.create_fleet(ai_settings, screen, ship, aliens)
		
		#Cria uma instancia para armazenar estatisticos do jogo  e cria painel de  pontuação
		stats = GameStats(ai_settings)
		sb = ScoreBoard(ai_settings, screen, stats)
		
		#Inicia o laço principal do jogo
		while True:
			
			#Observa eventos de teclado e de mouse
			gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
			
			if stats.game_active:
				ship.update()
			
				gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
				
				gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
				
				#Redesenha a tela a cada passagem pelo laço
				gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)
						
run_game()
