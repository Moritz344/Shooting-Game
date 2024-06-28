import time
import sys
import random
import pygame

clock = pygame.time.Clock()
screen_width = 800
screen_height = 500
screen = pygame.display.set_mode((800, 500))
pygame.display.set_caption("Game")


def timer():
    for i in range(4):
        time.sleep(0.5)
        print("Timer:", i)


timer()

# background_image = pygame.image.load("space.jpg")
# background_image = pygame.transform.scale(background_image,
# (screen_width, screen_height))

WEISS = (255, 255, 255)

player_size = 10
player_pos = [screen_width // 2, screen_height - 2 * player_size]
player_speed = 0.1

bullet_size = 5
bullet_color = WEISS
bullet_speed = 0.1

bullets = []
enemy_killed = 0

enemy_x = random.randint(50, 300)
enemy_y = random.randint(50, 300)

enemy_size = 50
enemy_speed = 0.1

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            sys.exit(0)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullet_pos = [
                    player_pos[0] + player_size // 2 - bullet_size // 2,
                    player_pos[1]
                ]

                bullets.append(bullet_pos)

    screen.fill("black")

    # print("X:", player_pos[0])
    # print("Y:", player_pos[1])

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_d]:
        player_pos[0] += player_speed
    elif pressed[pygame.K_a]:
        player_pos[0] -= player_speed
    elif pressed[pygame.K_w]:
        player_pos[1] -= player_speed
    elif pressed[pygame.K_s]:
        player_pos[1] += player_speed

    for bullet in bullets:
        bullet[1] -= bullet_speed

        if bullet[1] < 0:
            bullets.remove(bullet)

    player = pygame.draw.rect(
        screen, WEISS,
        [player_pos[0], player_pos[1], player_size, player_size])
    # for i in range(1):
    enemy = pygame.draw.rect(screen, "red",
                             [enemy_x, enemy_y, enemy_size, enemy_size])

    # enemy_x += enemy_speed

    enemy_dead = False

    for bullet in bullets:
        player_bullet = pygame.draw.rect(
            screen, WEISS, (bullet[0], bullet[1], bullet_size, bullet_size))
        if player_bullet.colliderect(enemy):
            enemy_dead = True
            enemy_killed += 1
            enemy_x = random.randint(0, 600)
            enemy_y = random.randint(0, 300)

            print(enemy_killed)

            if enemy_killed == 10:
                print("LEVEL 1 COMPLETED!")
                enemy_size = 15

    def coll():
        if player_pos[0] <= 0:
            player_pos[0] = 0

        elif player_pos[1] <= 0:
            player_pos[1] = screen_height

        elif player_pos[0] >= 800:
            player_pos[0] = 790

        elif player_pos[1] >= 500:
            player_pos[1] = 6

    coll()
    pygame.display.flip()
