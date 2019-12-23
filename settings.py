class Settings():
	"""Uma classe para armazenar todas as configurações da Invasão Alienígena."""
	
	def __init__(self):
		"""Inicializa as configurações do jogo."""
		#Configurações da tela
		self.screen_width = 1600
		self.screen_height = 800
		self.bg_color = (230,230,230)
		
		#Configurações da espaçonave
		self.ship_speed_factor = 0.8
		
		#Configurações dos projeteis
		self.bullet_speed_factor = 1
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = 60,60,60
		self.bullets_alowed = 3
