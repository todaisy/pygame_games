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

        else:
            if self.x < 250:
                self.x += 1
            elif self.x > 250:
                self.x -= 1

            if self.y < 250:
                self.y += 1
            elif self.y > 250:
                self.y -= 1

    def jump(self):

    

circle1 = Circle(250, 250, 30)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()


    # передвижение круга
    keys1 = pygame.key.get_pressed()
    circle1.move_by_keys(keys1)
    circle1.draw()
    pygame.time.delay(10)
