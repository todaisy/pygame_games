import pygame
pygame.init()
win = pygame.display.set_mode((500, 500))

x_c = 250
y_c = 250

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    # передвижение круга
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x_c -= 3
    elif keys[pygame.K_RIGHT]:
        x_c += 3
    elif keys[pygame.K_UP]:
        y_c -= 3
    elif keys[pygame.K_DOWN]:
        y_c += 3

    else:
        if x_c < 250:
            x_c += 1
        elif x_c > 250:
            x_c -= 1

        if y_c < 250:
            y_c += 1
        elif y_c > 250:
            y_c -= 1
            
    win.fill((255, 255, 255))
    pygame.draw.circle(win, (255, 0, 255), (x_c, y_c), 30)
    pygame.display.update()

    pygame.time.delay(10)
