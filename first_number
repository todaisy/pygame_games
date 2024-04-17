import pygame
pygame.init()
win = pygame.display.set_mode((500, 500))

x_r = 100
y_r = 300

x_c = 250
y_c = 30

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    x_r = x_r + 1
    y_c = y_c + 1

    if x_r > 500:
        x_r = -100

    if y_c > 500:
        y_c = -80

    win.fill((255, 255, 255))
    pygame.draw.rect(win, (255, 255, 0), (x_r, y_r, 100, 60))
    pygame.draw.circle(win, (255, 0, 255), (x_c, y_c), 30)
    pygame.display.update()

    pygame.time.delay(10)
