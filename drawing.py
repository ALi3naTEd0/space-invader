import pygame
import os 

# Cargar la imagen de fondo
BACKGROUND_IMAGE = pygame.image.load(os.path.join('assets', 'background.png'))

class Drawing:
    def __init__(self, window):
        self.window = window
    def drawing(self, game, player, enemies, FPS):
        # Dibujar fondo
        self.draw_background()
        
        # Dibujar enemigos
        for enemy in enemies[:]:
            enemy.draw(self.window)
        
        # Dibujar jugador
        player.draw(self.window)
        
        # Dibujar HUD
        game.drawHud()

        pygame.display.update()

def draw_background(window):
    window.blit(BACKGROUND_IMAGE, (0, 0))