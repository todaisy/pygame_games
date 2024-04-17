import pygame
pygame.init()
win = pygame.display.set_mode((500, 500))

x_c = 250
y_c = 30
dir_c = -1

x_r = 100
y_r = 300
dir_r = 1

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    # передвижение круга
    if dir_c == -1:
        y_c += 1
    else:
        y_c -= 1

    if y_c > 500:
        dir_c = 1
    if y_c < 0:
        dir_c = -1

    # передвижение прямоугольника
    if dir_r == 1:
        x_r += 1
    else:
        x_r -= 1

    if x_r > 500:
        dir_r = -1
    if x_r < 0:
        dir_r = 1

    win.fill((255, 255, 255))
    pygame.draw.rect(win, (255, 255, 0), (x_r, y_r, 100, 60))
    pygame.draw.circle(win, (255, 0, 255), (x_c, y_c), 30)
    pygame.display.update()

    pygame.time.delay(10)
