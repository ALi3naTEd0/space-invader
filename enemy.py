from ship import Ship
import pygame
import random
import os

# Obtener el directorio actual y la carpeta de assets
current_dir = os.path.dirname(os.path.abspath(__file__))
assets_dir = os.path.join(current_dir, 'assets')

# Cargar imágenes de enemigos
def safe_load_image(filename, size=(64, 64)):
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'assets', filename)
    try:
        return pygame.image.load(path)
    except FileNotFoundError:
        surf = pygame.Surface(size)
        surf.fill((255,0,0))
        return surf

Enemy_Blue = safe_load_image('enemy_blue_image.png')
Enemy_Green = safe_load_image('enemy_green_image.png')
Enemy_Purple = safe_load_image('enemy_purple_image.png')

# Cargar imágenes de disparos
SHOT_BLUE_IMAGE = safe_load_image('shot_blue.png', size=(32,32))
SHOT_GREEN_IMAGE = safe_load_image('shot_green.png', size=(32,32))
SHOT_PURPLE_IMAGE = safe_load_image('shot_purple.png', size=(32,32))

class Enemy(Ship):
    """Clase para los enemigos del juego.

    Parámetros:
    - x: Posición horizontal del enemigo
    - y: Posición vertical del enemigo
    - tipo: Tipo de enemigo ('blue', 'green', 'purple')
    - salud: Puntos de vida del enemigo
    """

    COLOR = {
        "blue": (Enemy_Blue, SHOT_BLUE_IMAGE),
        "green": (Enemy_Green, SHOT_GREEN_IMAGE),
        "purple": (Enemy_Purple, SHOT_PURPLE_IMAGE)
    }

    def __init__(self, x=50, y=50, salud=100, color="blue", speed=10):
        super().__init__(x, y, salud)
        self.ship_img, self.bullet_img = self.COLOR[color]
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.speed = speed
    def move(self):
        """Mueve el enemigo hacia abajo en la pantalla."""
        self.y += self.speed
    def create(self, amount):
        """Crea una lista de enemigos con posiciones y tipos aleatorios.

        Parámetros:
        - amount: Cantidad de enemigos a crear

        Retorna:
        - Lista de objetos Enemy
        """
        enemies = []
        for i in range(amount):
            enemy = Enemy(
                x=random.randrange(20, 1920-Enemy_Blue.get_width()-20),
                y=random.randrange(-1500, -100),
                color=random.choice(["blue", "green", "purple"]),
                speed=random.randrange(-1000, -100)
            )
            enemies.append(enemy)
        return enemies