class Settings():
	"""Uma classe para armazenar todas as configurações da Invasão Alienígena."""
	
	def __init__(self):
		"""Inicializa as configurações do jogo."""
		#Configurações da tela
		self.screen_width = 1600
		self.screen_height = 900
		self.bg_color = (230,230,230)
		
		#Configurações da espaçonave
		self.ship_speed_factor = 1.5
		
		#Configurações dos projeteis
		self.bullet_speed_factor = 3
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = 60,60,60
		self.bullets_alowed = 3
		
		#Configurações dos alienígenas
		self.alien_speed_factor = 1
		self.fleet_drop_speed = 10
		#fleet_direction igual a 1 representa a direita; -1 representa a esquerda
		self.fleet_direction = 1
