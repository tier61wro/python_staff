import pygame
import logging
import os
import sys
import time


clock = pygame.time.Clock()

# background music
pygame.mixer.init()
pygame.mixer.music.load("music/sonar.mp3.mpg")
# pygame.mixer.music.load("music/sonar2.mp3.mpg")
# pygame.mixer.music.load("music/expl.mp3.mpg")

pygame.mixer.music.play(1000, 0)

# логгирование
logging.basicConfig(filename='logfile.log', level=logging.INFO)
logging.info('==============================')
logging.info('GAME STARTED')

# подгружаем изображения
images_folder = './images'
cargoStand = pygame.image.load(os.path.join(images_folder, 'cargo.png'))
lodkaStand = pygame.image.load(os.path.join(images_folder, 'submarine.png'))
planeStand = pygame.image.load(os.path.join(images_folder, 'plane.png'))


pygame.init()
run = True
win_width = 1000
win_height = 500
win = pygame.display.set_mode((win_width, win_height))
bg = pygame.image.load(os.path.join(images_folder, 'bg.png'))

pygame.display.set_caption("submarine game")
myfont = pygame.font.SysFont("monospace", 16)


clock = pygame.time.Clock()


# submarine params
x = 50
y = 425
width = 130
height = 39
speed = 10
alive = 1
double_speed = speed * 2


class Torpeda():
    def __init__(self, x, y, type):
        self.x = x
        self.y = y
        self.vel = 8

    def draw(self, win):
        pygame.draw.rect(win, (0, 0, 0), (self.x, self.y, 2, 5))


class Bomb():
    def __init__(self, x, y, type):
        self.x = x
        self.y = y
        self.vel = 10

    def draw(self, win):
        pygame.draw.rect(win, (0, 0, 0), (self.x, self.y, 2, 5))


class Enemy():
    def __init__(self, x, y, type):
        self.x = x
        self.y = y
        self.type = type
        self.size = 30
        if self.type == 'ordinary':
            self.vel = 5
            self.size = 130
        else:  # fast
            self.vel = 10
            self.size = 130

    def draw(self, win):
        #pygame.draw.rect(win, (0, 0, 0), (self.x, self.y, self.size, 8))
        win.blit(cargoStand, (self.x, self.y))


class Plane():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 50
        self.height = 100
        self.vel = 8  # TODO make it random (5 - 10)
        self.last_bomb = pygame.time.get_ticks()

    def draw(self, win):
        #pygame.draw.rect(win, (0, 0, 0), (self.x, self.y, self.size, 8))
        win.blit(planeStand, (self.x, self.y))

    def create_bomb(self):
        curr_time = pygame.time.get_ticks()
        if (curr_time - self.last_bomb) > 1000:
            logging.info('we created bomb')
            self.last_bomb = curr_time
            file = 'music/1_torpeda.mp3'
            pygame.mixer.music.load(file)
            pygame.mixer.music.set_volume(0.1)
            pygame.mixer.music.play()
            logging.info('we created bomb sound')
            bombs.append(Bomb(self.x + self.width/2, self.y + self.height, 'ordinary'))



def drawWindow():
    #win.blit(bg, (0, 0))
    for torpeda in torpedos:
        torpeda.draw(win)

    for enemy in enemies:
        enemy.draw(win)

    for plane in planes:
        plane.create_bomb()
        plane.draw(win)

    for bomb in bombs:
        bomb.draw(win)

    pygame.display.update()

def drawBg():
    win.blit(bg, (0, 0))


torpedos = []
enemies = []
planes = []
bombs = []
score = 0

# MAIN LOOP START
while run:
    clock.tick(10)  # better then : pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    disclaimertext = myfont.render("Round 1", 1, (0, 0, 0))
    gameovertext = myfont.render("GAME OVER", 1, (0, 0, 0))
    scoretext = myfont.render("Score {0}".format(score), 1, (0,0,0))
    reloadtext = myfont.render("Reloading in {0}".format('3'), 1, (0, 0, 0))
    currentColor = (255, 255, 255)

    #drawBg()
    if alive == 0:
        #currentColor = (255, 255, 255)
        win.fill(currentColor)
        win.blit(gameovertext, (5, 480))
        pygame.display.update()
        time.sleep(3)
        run = False
        break

    else:
        drawBg()
        win.blit(disclaimertext, (5, 480))
        win.blit(scoretext, (5, 10))
        win.blit(reloadtext, (win_width - 150, win_height - 20))
        #win.blit(planeStand, (100, 10))
        win.blit(lodkaStand, (x, y))

        for torpeda in torpedos:
            for enemy in enemies:
                if (torpeda.y < 95) and ((torpeda.x > enemy.x) and (torpeda.x < enemy.x + enemy.size)):
                    logging.info('enemy was killed')
                    score += 1
                    enemies.pop(enemies.index(enemy))

            if torpeda.y < win_height and torpeda.y > 95:
                torpeda.y -= 10
            else:
                torpedos.pop(torpedos.index(torpeda))

        for bomb in bombs:
            logging.debug("bombx = {}, bomby = {}".format(bomb.x, bomb.y))
            logging.debug("x = {}, y = {}".format(x, y))
            if (bomb.x < x + width) and (bomb.x > x) and (bomb.y > y) and (bomb.y < y + height):
            #if (torpeda.y < 95) and ((torpeda.x > enemy.x) and (torpeda.x < enemy.x + enemy.size)):
                logging.info('submarine was killed')
                #pygame.mixer.music.load("music/expl.mp3")
                #pygame.mixer.music.play(1, 0)
                alive = 0
                win.fill(currentColor)
                break
            elif bomb.y > win_height:
                logging.info('bomb was popped')
                bombs.pop(bombs.index(bomb))

        for enemy in enemies:
            if enemy.x < win_width and enemy.y > 0:
                # logging.info("we moved enemy")
                enemy.x += enemy.vel
            else:
                enemies.pop(enemies.index(enemy))

        for plane in planes:
            if plane.x < win_width and plane.y > 0:
                plane.x -= plane.vel
                cur_time = pygame.time.get_ticks()
                #logging.info("current time  = " + str(cur_time))
            else:
                enemies.pop(planes.index(plane))

        for bomb in bombs:
            if bomb.y < win_height:
                bomb.y += bomb.vel
                # logging.info("we moved bomb")
            else:
                bombs.pop(bombs.index(bomb))


        #pygame.display.update()
        keys = pygame.key.get_pressed()

        if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and x > 0:
            x -= speed
        if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and x < win_width - width - 5:
            x += speed
        if (keys[pygame.K_UP] or keys[pygame.K_w]) and y > 5:
            y -= speed
        if (keys[pygame.K_DOWN] or keys[pygame.K_s]) and y < win_height - height - 5:
            y += speed
        if keys[pygame.K_SPACE]:
            # launch torpedo
            torpedos.append(Torpeda(round(x + width // 2), round(y + height // 2), 'ordinary'))
        if keys[pygame.K_o]:
            # create Enemy
            # logging.info("we added enemy to list")
            enemies.append(Enemy(20, 87, 'ordinary'))
        if keys[pygame.K_f]:
            # create Enemy
            # logging.info("we added enemy to list")
            enemies.append(Enemy(20, 87, 'fast'))
        if keys[pygame.K_p]:
            # create Plane
            logging.info("we added plane to list")
            planes.append(Plane(win_width - 10, 10))

        drawWindow()

pygame.quit()