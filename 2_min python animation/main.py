import pygame
import random
import math

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Particle System")

# Colors
BLACK = (0, 0, 0)

# Particle class
class Particle:
    def _init_(self, x, y):
        self.x = x
        self.y = y
        self.size = random.randint(4, 6)
        self.color = [random.randint(0, 255) for _ in range(3)]
        self.speed = random.uniform(2, 5)
        self.angle = random.uniform(0, 2 * math.pi)

    def move(self):
        self.x += self.speed * math.cos(self.angle)
        self.y += self.speed * math.sin(self.angle)
        self.size -= 0.05
        if self.size <= 0:
            self.size = 0

    def draw(self, screen):
        if self.size > 0:
            pygame.draw.circle(screen, self.color,
                               (int(self.x), int(self.y)), int(self.size))

def main():
    clock = pygame.time.Clock()
    particles = []

    running = True
    while running:
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        mouse_x, mouse_y = pygame.mouse.get_pos()

        particles.append(Particle(mouse_x, mouse_y))

        for particle in particles:
            particle.move()
            particle.draw(screen)
            if particle.size == 0:
                particles.remove(particle)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "_main_":
    main()