import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
ANT_SPEED = 5
ENEMY_SPEED = 3
ANT_SIZE = 50

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Ant class
class Ant(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((ANT_SIZE, ANT_SIZE))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT // 2)

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= ANT_SPEED
        if keys[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.x += ANT_SPEED
        if keys[pygame.K_UP] and self.rect.top > 0:
            self.rect.y -= ANT_SPEED
        if keys[pygame.K_DOWN] and self.rect.bottom < HEIGHT:
            self.rect.y += ANT_SPEED

# Enemy class
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))  # Placeholder for enemy image
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(HEIGHT - self.rect.height)

    def update(self):
        self.rect.y += ENEMY_SPEED
        if self.rect.top > HEIGHT:
            self.rect.y = 0
            self.rect.x = random.randrange(WIDTH - self.rect.width)

# Initialize game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Antma Game")
clock = pygame.time.Clock()

# Sprites
all_sprites = pygame.sprite.Group()
ants = pygame.sprite.Group()
enemies = pygame.sprite.Group()

ant = Ant()
all_sprites.add(ant)
ants.add(ant)

for _ in range(5):  # Create 5 enemies as a placeholder
    enemy = Enemy()
    all_sprites.add(enemy)
    enemies.add(enemy)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update
    all_sprites.update()

    # Check for collisions between ant and enemies
    hits = pygame.sprite.spritecollide(ant, enemies, False)
    if hits:
        print("Ant caught by an enemy!")

    # Draw / Render
    screen.fill(BLACK)
    all_sprites.draw(screen)

    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()
sys.exit()
