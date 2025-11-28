import pygame
from ship import Ship
import main
from bullet import Bullet

class Player(Ship):
    def __init__(self, x, y, health):
        # Hereda posición y salud desde Ship
        super().__init__(x, y, health)

        # Velocidades de movimiento
        self.x_speed = 0
        self.y_speed = 0

        # Carga de imágenes desde main
        self.ship_img = main.player_image
        self.bullet_img = main.BULLET_IMAGE

        # Velocidad de las balas
        self.bullet_speed = 10

        # Máscara de colisión
        self.mask = pygame.mask.from_surface(self.ship_img)

        # Máximo de balas activas
        self.max_bullets = 3

        # Lista de balas activas
        self.bullets = []

        # Contadores para cooldown de disparo y creación de balas
        self.creation_cooldown_counter = 0
        self.bullet_cooldown_counter = 0

    def move(self, screen_width, screen_height):
        key = pygame.key.get_pressed()
        # Arriba
        if (key[pygame.K_w] or key[pygame.K_UP]) and self.y > 0:
            self.y -= self.y_speed
        # Abajo
        if (key[pygame.K_s] or key[pygame.K_DOWN]) and self.y + self.get_height() + self.y_speed <= screen_height:
            self.y += self.y_speed
        # Izquierda
        if (key[pygame.K_a] or key[pygame.K_LEFT]) and self.x > 0:
            self.x -= self.x_speed
        # Derecha
        if (key[pygame.K_d] or key[pygame.K_RIGHT]) and self.x + self.get_width() + self.x_speed <= screen_width:
            self.x += self.x_speed

    def create_bullets(self):
        # Permite crear balas si no se ha alcanzado el máximo y no hay cooldown
        if (len(self.bullets) < self.max_bullets) and (self.creation_cooldown_counter == 0):
            bullet = Bullet(self.x, self.y, self.bullet_img)
            self.bullets.append(bullet)
            self.creation_cooldown_counter = 1

    def cooldown(self):
        if self.bullet_cooldown_counter >= 20:
            self.bullet_cooldown_counter = 0
        elif self.bullet_cooldown_counter > 0:
            self.bullet_cooldown_counter += 1

        if self.creation_cooldown_counter >= self.cool_down :
            self.creation_cooldown_counter = 0
        elif self.creation_cooldown_counter > 0:
            self.creation_cooldown_counter += 1

    def fire(self, window):
        keys = pygame.key.get_pressed()
        # Solo dispara si hay balas en self.bullets y no hay cooldown
        if keys[pygame.K_SPACE] and len(self.bullets) > 0 and self.bullet_cooldown_counter == 0:
            bullet = self.bullets.pop()
            bullet.x = self.x + (self.ship_img.get_width() - self.bullet_img.get_width()) // 2
            bullet.y = self.y
            self.fired_bullets.append(bullet)
            self.bullet_cooldown_counter = 1
            self.creation_cooldown_counter = 1
        # Mover y dibujar balas disparadas
        for bullet in self.fired_bullets[:]:
            bullet.move(-self.bullet_speed)  # Mueve hacia arriba
            bullet.draw(window)
            # Eliminar balas fuera de pantalla
            if bullet.y < -40:
                self.fired_bullets.remove(bullet)

    def hit(self, enemies):
        # Verifica si alguna bala impacta un enemigo
        for bullet in self.fired_bullets[:]:
            for enemy in enemies[:]:
                if bullet.collision(enemy):
                    enemies.remove(enemy)
                    self.fired_bullets.remove(bullet)
                    break