import pygame

pygame.init()

win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("sasha game")

x = 50
y = 425

width = 40
height = 60
speed = 10
double_speed = speed * 2

last_col = 155
run = True

isJump = False
jumpCount = 10

while run:
    pygame.time.delay(100)  # 100 mseks
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    win.fill((0, 0, 0))
    perp = pygame.draw.rect(win, (255, 255, 0), (180, 260, 10, 50))
    rect1 = pygame.draw.rect(win, (0, 0, last_col), (x, y, width, height))


    pygame.display.update()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LSHIFT]:
        if last_col == 255:
            speed = speed / 2
            last_col = 155
        else:
            speed = double_speed
            last_col = 255

    if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and x > 0:
        x -= speed
    if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and x < 500 - width - 5:
        x += speed
    if not isJump:
        if (keys[pygame.K_UP] or keys[pygame.K_w]) and y > 5:
            y -= speed
        if (keys[pygame.K_DOWN] or keys[pygame.K_s]) and y < 500 - height - 5:
            y += speed
        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCount >= -10:
            if jumpCount < 0:
                y += (jumpCount ** 2) / 2
            else:
                y -= (jumpCount ** 2) / 2
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10

pygame.quit()

