import sys

import pygame
from settings import Settings
from ship import Ship
from pygame.sprite import Group
from alien import Alien
import game_functions as gf
from game_stats import GameStats
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
		
		#Cria instancia para armazenar estatisticas do jogo  e cria painel de  pontuação
		stats = GameStats(ai_settings)
		sb = ScoreBoard(ai_settings, screen, stats)
		
		#Inicia o laço principal do jogo
		while True:
			
			#Observa eventos de teclado e de mouse
			gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
			
			if stats.game_active:
				ship.update()
			
				gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
				
				gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)
				
				gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)
						
run_game()
