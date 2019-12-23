import sys

from bullet import Bullet
import pygame

def check_keydown_events(event, ai_settings, screen, ship, bullets):
	"""Responde a pressionamentos de teclas."""
	if event.key == pygame.K_RIGHT:
		#Move a espaçonave para a direita
		ship.moving_right = True
	elif event.key == pygame.K_LEFT:
		#Move a espaçonave para a esquerda
		ship.moving_left = True
	elif event.key == pygame.K_UP:
		#Movimenta a epaçonave para cima
		ship.moving_up = True
	elif event.key ==  pygame.K_DOWN:
		#MOvimenta a espaçonave para baixo
		ship.moving_down = True
	elif event.key == pygame.K_SPACE:
		#Cria um novo projetil e o adiciona ao grupo de projeteis
		if len(bullets) < ai_settings.bullets_alowed:
			new_bullet = Bullet(ai_settings, screen, ship)
			bullets.add(new_bullet)

def check_keyup_events(event, ship):
	"""Responde a solturas de tecla."""
	if event.key == pygame.K_RIGHT:
		ship.moving_right = False
	elif event.key == pygame.K_LEFT:
		ship.moving_left = False
	elif event.key == pygame.K_UP:
		ship.moving_up = False
	elif event.key == pygame.K_DOWN:
		ship.moving_down = False

def check_events(ai_settings, screen, ship, bullets):
	"""Responde a eventos de pressionamento de teclas e de mouse."""
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event, ai_settings, screen, ship, bullets)	
					
		elif event.type == pygame.KEYUP:
			check_keyup_events(event, ship)

def update_screen(ai_settings, screen, ship, bullets):
	"""Atualiza as imagens na tela e alterna para a nova tela."""
	#Redesenha a tela a cada passagem pelo laço
	screen.fill(ai_settings.bg_color)
	
	#Redesenha todos os projeteis atrás da espaçonave e dos alienígenas
	for bullet in bullets.sprites():
		bullet.draw_bullet()
			
	ship.blitme()
	
def update_bullets(bullets):
	"""Atualiza as posições dos projeteis e se livra dos projeteis antigos."""
	#Atualiza as posições dos projeteis
	bullets.update()
	
	#Livra-se dos projeteis que desapareceram
	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)
