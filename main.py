import pygame
import random

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Wireless Pointing Controller")
pygame.mouse.set_visible(False)
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)

target_radius = 40
target_x = random.randint(50, 750)
target_y = random.randint(50, 550)

score = 0


def get_mouse_position():
    x, y = pygame.mouse.get_pos()
    return x, y


running = True

while running:
    fire = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                fire = True
                fire_x, fire_y = event.pos

    if fire:
        dx = fire_x - target_x
        dy = fire_y - target_y

        if dx * dx + dy * dy <= target_radius * target_radius:
            score += 1
            target_x = random.randint(50, 750)
            target_y = random.randint(50, 550)

    crosshair_x, crosshair_y = get_mouse_position()
    screen.fill((30, 30, 30))

    pygame.draw.circle(screen, (255, 80, 80), (target_x, target_y), target_radius)

    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (20, 20))

    crosshair_color = (255, 255, 255)
    crosshair_radius = 12
    crosshair_gap = 6
    crosshair_length = 20

    pygame.draw.circle(
        screen, crosshair_color, (crosshair_x, crosshair_y), crosshair_radius, 2
    )

    pygame.draw.line(
        screen,
        crosshair_color,
        (crosshair_x - crosshair_length, crosshair_y),
        (crosshair_x - crosshair_gap, crosshair_y),
        2,
    )

    pygame.draw.line(
        screen,
        crosshair_color,
        (crosshair_x + crosshair_gap, crosshair_y),
        (crosshair_x + crosshair_length, crosshair_y),
        2,
    )

    pygame.draw.line(
        screen,
        crosshair_color,
        (crosshair_x, crosshair_y - crosshair_length),
        (crosshair_x, crosshair_y - crosshair_gap),
        2,
    )

    pygame.draw.line(
        screen,
        crosshair_color,
        (crosshair_x, crosshair_y + crosshair_gap),
        (crosshair_x, crosshair_y + crosshair_length),
        2,
    )
    pygame.display.flip()
    clock.tick(60)


pygame.quit()
