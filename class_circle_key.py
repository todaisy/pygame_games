import pygame
pygame.init()
win = pygame.display.set_mode((500, 500))


class Circle:
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r

    def draw(self):
        win.fill((255, 255, 255))
        pygame.draw.circle(win, (255, 0, 255), (self.x, self.y), self.r)
        pygame.display.update()

    def move_by_keys(self, keys):
        if keys[pygame.K_LEFT]:
            self.x -= 3
        elif keys[pygame.K_RIGHT]:
            self.x += 3
        elif keys[pygame.K_UP]:
            self.y -= 3
        elif keys[pygame.K_DOWN]:
            self.y += 3

    def jump(self, key):
        if key[pygame.K_SPACE]:
            self.y -= 15
        else:
            if self.y < 400:
                self.y += 15

    
circle1 = Circle(250, 400, 30)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    # передвижение круга
    keys1 = pygame.key.get_pressed()
    circle1.move_by_keys(keys1)
    circle1.jump(keys1)
    circle1.draw()
    pygame.time.delay(10)
