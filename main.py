import pygame
import random

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Wireless Pointing Controller")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)

target_radius = 40
target_x = random.randint(50, 750)
target_y = random.randint(50, 550)

score = 0

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            dx = mouse_x - target_x
            dy = mouse_y - target_y
            if dx * dx + dy * dy <= target_radius * target_radius:
                target_x = random.randint(50, 750)
                target_y = random.randint(50, 550)
                score += 1

    screen.fill((30, 30, 30))

    pygame.draw.circle(screen, (255, 80, 80), (target_x, target_y), target_radius)

    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (20, 20))

    pygame.display.flip()
    clock.tick(60)


pygame.quit()
