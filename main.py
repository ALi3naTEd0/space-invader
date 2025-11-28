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

# Usar el nombre correcto del archivo de la bala
BULLET_IMAGE = safe_load_image(os.path.join('assets', 'bullet_image.png'))

def main():
    pygame.init()
    game = Game(screen_width=800, screen_height=600, fps=60, lives=3, nivel=1)
    game.bullets = 5

    # Crear jugador
    from player import Player
    player = Player(x=game.Screen_width // 2, y=game.screen_height - 80, health=100)
    player.x_speed = 5
    player.y_speed = 5

    # Parámetros para olas
    enemigos = []
    enemigos_en_ola = 0
    tiempo_ola = 0
    tiempo_entre_olas = 120  # frames
    ola_activa = False

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        game.Window.fill((20, 20, 30))
        # Dibujar fondo
        draw_background(game.Window)
        game.drawHud()

        # Olas de enemigos
        if not ola_activa:
            tiempo_ola += 1
            if tiempo_ola >= tiempo_entre_olas:
                enemigos_en_ola = random.randint(3, 7)
                enemigos = []
                for i in range(enemigos_en_ola):
                    enemigo = Enemy(
                        x=random.randrange(20, game.Screen_width-80),
                        y=random.randrange(-300, -40),
                        color=random.choice(["blue", "green", "purple"]),
                        speed=random.randint(1, 2)  # bajan poco a poco
                    )
                    enemigos.append(enemigo)
                ola_activa = True
                tiempo_ola = 0
        else:
            # Mover y dibujar todos los enemigos
            for enemigo in enemigos[:]:
                enemigo.move()
                enemigo.draw(game.Window)
                # Si el enemigo sale de la pantalla, lo elimina
                if enemigo.y > game.screen_height:
                    enemigos.remove(enemigo)
            # Si no quedan enemigos, preparar siguiente ola
            if len(enemigos) == 0:
                ola_activa = False

        # Mover y dibujar jugador
        player.move(game.Screen_width, game.screen_height)
        player.draw(game.Window)
        # Actualizar cooldowns
        player.cooldown()
        # Crear balas si es posible
        player.create_bullets()
        # Disparar y mover balas
        player.fire(game.Window)
        # Verificar impacto de balas con enemigos
        player.hit(enemigos)

        pygame.display.flip()
        game.tick()

    pygame.quit()

if __name__ == "__main__":
    main()