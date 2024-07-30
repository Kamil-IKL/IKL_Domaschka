import pygame
import random
import time

# Инициализация Pygame
pygame.init()

# Настройки экрана
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("РИСОВАНИЕ КРУГОВ")

# Основные цвета
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255), (0, 255, 255), (255, 165, 0)]
shapes = ['circle']

# Включаем основной цикл
running = True
last_draw_time = 0 # время последнего рисунка

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN: #and time.time() - last_draw_time > 1:
            # Получаем координаты нажатия мыши
            x, y = event.pos

            # Генерируем случайный цвет и размер
            color = random.choice(colors)
            radius = random.randint(10, 100)  # Радиус от 10 до 100

            # Рисуем круг
            pygame.draw.circle(screen, color, (x, y), radius)
            pygame.display.flip()  # Обновляем экран
            # last_draw_time = time.time()  # Обновляем время последнего рисования

    # Фоновый цвет экрана
    screen.fill((100, 20, 50))
    # screen.fill((255, 255, 255))

# Завершение работы Pygame
pygame.quit()


