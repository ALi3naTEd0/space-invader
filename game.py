import pygame


class Game:
	"""
	Clase principal del juego que inicializa los atributos solicitados.

	Atributos (exactamente como pidió):
	- Font
	- FPS
	- lives
	- Window
	- Screen_width
	- screen_height
	- bullets
	- clock
	- Nivel
	- Contador (para frames)
	"""

	def __init__(self, screen_width: int = 800, screen_height: int = 600, fps: int = 60,
				 lives: int = 3, font_name: str | None = None, nivel: int = 1,
				 caption: str = "Space Invader"):
		# Inicializa pygame si no está inicializado
		if not pygame.get_init():
			pygame.init()

		# Asegura que el módulo de fuentes esté listo
		if not pygame.font.get_init():
			pygame.font.init()

		# Dimensiones de pantalla
		self.Screen_width = screen_width
		self.screen_height = screen_height

		# Frames por segundo
		self.FPS = fps

		# Vidas del jugador
		self.lives = lives

		# Fuente (Font)
		# Si se pasa font_name se intenta cargar como Font, si no se usa SysFont por defecto
		try:
			if font_name:
				# Intentamos cargar una fuente desde archivo o nombre
				self.Font = pygame.font.Font(font_name, 24)
			else:
				self.Font = pygame.font.SysFont(None, 24)
		except Exception:
			# Fallback a la fuente por defecto si falla
			self.Font = pygame.font.SysFont(None, 24)

		# Ventana principal
		self.Window = pygame.display.set_mode((self.Screen_width, self.screen_height))
		pygame.display.set_caption(caption)

		# Contador de balas actualmente en pantalla
		self.bullets = 0

		# Reloj para controlar FPS
		self.clock = pygame.time.Clock()

		# Nivel
		self.Nivel = nivel

		# Contador de frames (para llevar la cuenta de frames transcurridos)
		self.Contador = 0

	def tick(self):
		"""Avanza un frame: incrementa contador y limita al FPS configurado.

		Llamar a este método dentro del bucle principal para mantener el reloj y
		contar frames.
		"""
		self.Contador += 1
		self.clock.tick(self.FPS)

	def drawHud(self):
		"""Dibuja el HUD (Heads-Up Display) con información del juego.
		
		Muestra:
		- Vidas disponibles (self.lives) - Arriba derecha
		- Balas disponibles (self.bullets) - Debajo de vidas (derecha)
		- Nivel actual (self.Nivel) - Arriba izquierda
		- Tiempo de juego (calculado desde self.Contador y self.FPS) - Debajo de nivel (izquierda)
		"""
		# Color del texto (blanco)
		text_color = (255, 255, 255)
		
		# Márgenes responsivos
		margin = 10
		spacing = 5
		
		# --- ARRIBA IZQUIERDA: Nivel ---
		level_label = self.Font.render(f"Nivel: {self.Nivel}", 1, text_color)
		nivel_x = margin
		nivel_y = margin
		self.Window.blit(level_label, (nivel_x, nivel_y))
		
		# --- DEBAJO DE NIVEL: Tiempo ---
		tiempo_segundos = self.Contador // self.FPS
		minutos = tiempo_segundos // 60
		segundos = tiempo_segundos % 60
		time_label = self.Font.render(f"Tiempo: {minutos:02d}:{segundos:02d}", 1, text_color)
		tiempo_x = margin
		tiempo_y = nivel_y + level_label.get_height() + spacing
		self.Window.blit(time_label, (tiempo_x, tiempo_y))
		
		# --- ARRIBA DERECHA: Vidas ---
		lives_label = self.Font.render(f"Vidas: {self.lives}", 1, text_color)
		vidas_x = self.Screen_width - lives_label.get_width() - margin
		vidas_y = margin
		self.Window.blit(lives_label, (vidas_x, vidas_y))
		
		# --- DEBAJO DE VIDAS: Balas ---
		bullets_label = self.Font.render(f"Balas:", 1, text_color)
		balas_x = self.Screen_width - bullets_label.get_width() - margin
		balas_y = vidas_y + lives_label.get_height() + spacing
		self.Window.blit(bullets_label, (balas_x, balas_y))
		
		# Offset y ciclo for para mostrar las balas disponibles
		bullet_offset = 20  # Espacio horizontal entre cada bala
		bullet_start_x = self.Screen_width - margin - (self.bullets * bullet_offset)
		bullet_y = balas_y + bullets_label.get_height() + spacing
		
		# Dibuja cada bala disponible como un símbolo
		for i in range(self.bullets):
			bullet_icon = self.Font.render("•", 1, text_color)  # Símbolo de bala
			bullet_x = bullet_start_x + (i * bullet_offset)
			self.Window.blit(bullet_icon, (bullet_x, bullet_y))

def escape(self):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return True
        else:
            return False
		
def over(self):
	if self.lives <= 0:
		self.contador = 0
		while True:
			self.clock.tick(self.FPS)
			gameover_label = self.Font.render("GAME OVER", 1, (255, 255, 255))
			self.Window.blit(gameover_label,(self.Screen_width-gameover_label.get_width()/2),(self.screen_height-gameover_label.get_height()/2))
			pygame.display.update()
			self.Contador += 1
			if self.Contador == self.FPS * 3:
				break
		return True
	else:
		return False
	
def reload_bullet(self, bullet):
	self.bullets = bullet