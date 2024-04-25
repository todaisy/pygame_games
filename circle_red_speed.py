import pygame
pygame.init()
win = pygame.display.set_mode((500, 500))

x = 250
y = 250

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    if x > 500:
        x = -100

    if y > 500:
        y = -100

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x = x - 3
    elif keys[pygame.K_RIGHT]:
        x += 3
    elif keys[pygame.K_UP]:
        y -= 3
    elif keys[pygame.K_DOWN]:
        y += 3
    else:
        if x < 250:
            x += 1
        elif x > 250:
            x -= 1

        if y < 250:
            y += 1
        elif y > 250:
            y -= 1

    if x < 100 or y < 100 or x > 400 or y > 400:
        color = 0
        pygame.time.delay(20)
    else:
        color = 255
        pygame.time.delay(6)

    win.fill((255, 255, 255))
    pygame.draw.circle(win, (255, 0, color), (x, y), 30)
    pygame.display.update()

    pygame.time.delay(0)
