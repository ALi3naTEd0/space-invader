import pygame
import os
import random

player_image = pygame.image.load(os.path.join('assets', 'player_image.png'))

from enemy import Enemy
from game import Game
from drawing import draw_background

def safe_load_image(path, size=(16, 16)):
    try:
        return pygame.image.load(path)
    except FileNotFoundError:
        return pygame.Surface(size)

BULLET_IMAGE = safe_load_image(os.path.join('assets', 'bullet.png'))

def main():
    pygame.init()
    game = Game(screen_width=800, screen_height=600, fps=60, lives=3, nivel=1)
    game.bullets = 5

    # Crear jugador
    from player import Player
    player = Player(x=game.Screen_width // 2, y=game.screen_height - 80, health=100)
    player.x_speed = 5
    player.y_speed = 5

    # Crear enemigos
    cantidad_enemigos = 5
    enemigos = []
    for i in range(cantidad_enemigos):
        enemigo = Enemy(
            x=random.randrange(20, game.Screen_width-80),
            y=random.randrange(-300, -40),
            color=random.choice(["blue", "green", "purple"]),
            speed=random.randrange(2, 6)
        )
        enemigos.append(enemigo)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        game.Window.fill((20, 20, 30))
        # Dibujar fondo
        draw_background(game.Window)
        game.drawHud()

        # Mover y dibujar enemigos
        for enemigo in enemigos:
            enemigo.move()
            enemigo.draw(game.Window)
            # Si el enemigo sale de la pantalla, lo reinicia arriba
            if enemigo.y > game.screen_height:
                enemigo.y = random.randrange(-300, -40)
                enemigo.x = random.randrange(20, game.Screen_width-80)

        # Mover y dibujar jugador
        player.move(game.Screen_width, game.screen_height)
        player.draw(game.Window)

        pygame.display.flip()
        game.tick()

    pygame.quit()

if __name__ == "__main__":
    main()