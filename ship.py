class Ship:
	"""
	Superclase para las naves del juego (jugador y enemigos).
	
	Parámetros:
	- x: Posición horizontal de la nave
	- y: Posición vertical de la nave
	- salud: Puntos de vida de la nave
	"""
	
	def __init__(self, x, y, salud):
		# Posición de la nave
		self.x = x
		self.y = y
		
		# Salud de vida
		self.salud = salud
		
		# Imágenes de la nave y balas
		self.ship_img = None
		self.bullet_img = None
		
		# Sistema de balas
		self.bullets = 0
		self.fired_bullets = []
		self.bullet_cooldown_counter = 0
		self.cool_down = 120

	def draw(self, window):
		"""Dibuja la nave en la ventana dada."""
		window.blit(self.ship_img, (self.x, self.y))
	def get_width(self):
		return self.ship_img.get_width()
	def get_height(self):
		return self.ship_img.get_height()