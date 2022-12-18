import pygame
import random
import math
from models import Enemy, Player, PlayerFast, PlayerFastShot, PlayerStrong

pygame.init()

screen = pygame.display.set_mode((800, 600))


# Background
background = pygame.image.load("./static/backgrounds/background_resized.jpg")
# Sound
# pygame.mixer.music.load("background.wav")
# pygame.mixer.music.play(-1) #to play on loop

# Title and icon
pygame.display.set_caption("Into space with grace")
icon = pygame.image.load("./static/icons/spaceship.png")
pygame.display.set_icon(icon)


# Player
player = PlayerFastShot()

num_of_enemies = 3
enemies = []


for i in range(num_of_enemies):
    enemies.append(Enemy())

# Bullet
bulletImg = pygame.image.load("./static/icons/bullet.png")
bulletX = random.randint(0, 800)
bulletY = 500
bulletYchange = player.bullet_speed
bullet_state = "ready"

# Score
score_value = 0
font = pygame.font.Font("freesansbold.ttf", 32)
scoreX = 10
scoreY = 10


def show_score(x: int, y: int) -> None:
    score = font.render(f"Score: {str(score_value)}", True, (255, 255, 255))
    screen.blit(score, (x, y))


def render_player(x: int, y: int) -> None:
    screen.blit(player.img, (x, y))


def render_enemy(x: int, y: int, i: int) -> None:
    screen.blit(enemies[i].img, (x, y))


def fire_bullet(x: int, y: int) -> None:
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))


def is_collision(enemyX: int, enemyY: int, bulletX: int, bulletY: int) -> bool:
    distance = math.sqrt((enemyX - bulletX) ** 2 + (enemyY - bulletY) ** 2)
    if distance < 27:
        return True
    else:
        return False


# Game Loop
running = True
while running:
    screen.fill((0, 0, 0))
    # background image
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Keystroke
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.xchange = -player.speed
            if event.key == pygame.K_RIGHT:
                player.xchange = player.speed
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bulletX = player.x
                    fire_bullet(player.x, bulletY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player.xchange = 0

    # Spaceship boundries
    player.x += player.xchange

    if player.x <= 0:
        player.x = 0
    elif player.x >= 736:
        player.x = 736

    # Enemy movement 1 enemy
    # enemya.x += enemya.xchange
    # if enemya.x <= 0:
    #     enemya.xchange = 0.1
    #     enemya.y += enemya.ychange
    # elif enemya.x >= 736:
    #     enemya.xchange = -0.1
    #     enemya.y += enemya.ychange
    # render_enemy(enemya.x, enemya.y)
    # # Collision
    # collision = is_collision(enemya.x, enemya.y, bulletX, bulletY)
    # if collision:
    #     enemya.x = random.randint(0, 735)
    #     enemya.y = random.randint(50, 150)
    #     bulletY = 480
    #     bullet_state = "ready"
    #     score_value += 1
    #     print(score_value)

    for i in range(len(enemies)):
        enemies[i].x += enemies[i].xchange
        if enemies[i].x <= 0:
            enemies[i].xchange = 0.1
            enemies[i].y += enemies[i].ychange
        elif enemies[i].x >= 736:
            enemies[i].xchange = -0.1
            enemies[i].y += enemies[i].ychange

        # Collision
        collision = is_collision(enemies[i].x, enemies[i].y, bulletX, bulletY)
        if collision:
            enemies[i] = Enemy()
            bulletY = 480
            bullet_state = "ready"
            score_value += 1
            print(score_value)

        render_enemy(enemies[i].x, enemies[i].y, i)

    # Bullet movement
    if bulletY <= 0:
        bulletY = 500
        bullet_state = "ready"

    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletYchange

    render_player(player.x, player.y)
    show_score(scoreX, scoreY)
    pygame.display.update()
