import pygame
import sys

# Инициализация Pygame
pygame.init()

# Размеры окна
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Пинг-понг")

# Цвета
yellow = (255, 255, 0)
white = (255, 255, 255)
black = (0, 0, 0)

# Шрифты
font = pygame.font.SysFont(None, 55)

# Координаты и размеры объектов
ball_pos = [screen_width // 2, screen_height // 2]
ball_radius = 15
ball_speed = [3, 3]

paddle_width = 10
paddle_height = 100
paddle_speed = 10

player1_pos = [50, screen_height // 2 - paddle_height // 2]
player2_pos = [screen_width - 50 - paddle_width, screen_height // 2 - paddle_height // 2]

# Счет
player1_score = 0
player2_score = 0

def draw_score():
    player1_text = font.render(str(player1_score), True, white)
    player2_text = font.render(str(player2_score), True, white)
    screen.blit(player1_text, (screen_width // 4, 20))
    screen.blit(player2_text, (screen_width * 3 // 4, 20))

# Основной игровой цикл
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and player1_pos[1] > 0:
        player1_pos[1] -= paddle_speed
    if keys[pygame.K_s] and player1_pos[1] < screen_height - paddle_height:
        player1_pos[1] += paddle_speed
    if keys[pygame.K_UP] and player2_pos[1] > 0:
        player2_pos[1] -= paddle_speed
    if keys[pygame.K_DOWN] and player2_pos[1] < screen_height - paddle_height:
        player2_pos[1] += paddle_speed

    ball_pos[0] += ball_speed[0]
    ball_pos[1] += ball_speed[1]

    if ball_pos[1] - ball_radius <= 0 or ball_pos[1] + ball_radius >= screen_height:
        ball_speed[1] = -ball_speed[1]
    
    # Проверка столкновения мяча с первой ракеткой
    if (ball_pos[0] - ball_radius <= player1_pos[0] + paddle_width and
            player1_pos[1] < ball_pos[1] < player1_pos[1] + paddle_height):
        ball_speed[0] = -ball_speed[0]
        ball_pos[0] = player1_pos[0] + paddle_width + ball_radius  # Коррекция позиции мяча при столкновении

    # Проверка столкновения мяча со второй ракеткой
    if (ball_pos[0] + ball_radius >= player2_pos[0] and
            player2_pos[1] < ball_pos[1] < player2_pos[1] + paddle_height):
        ball_speed[0] = -ball_speed[0]
        ball_pos[0] = player2_pos[0] - ball_radius  # Коррекция позиции мяча при столкновении

    # Проверка пересечения мяча границ экрана
    if ball_pos[0] - ball_radius <= 0:
        player2_score += 1
        ball_pos = [screen_width // 2, screen_height // 2]
        ball_speed = [3, 3]  # Сброс скорости мяча
    if ball_pos[0] + ball_radius >= screen_width:
        player1_score += 1
        ball_pos = [screen_width // 2, screen_height // 2]
        ball_speed = [-3, -3]  # Сброс скорости мяча

    screen.fill(yellow)
    pygame.draw.rect(screen, white, (player1_pos[0], player1_pos[1], paddle_width, paddle_height))
    pygame.draw.rect(screen, white, (player2_pos[0], player2_pos[1], paddle_width, paddle_height))
    pygame.draw.circle(screen, white, ball_pos, ball_radius)
    draw_score()

    pygame.display.flip()
    pygame.time.Clock().tick(60)