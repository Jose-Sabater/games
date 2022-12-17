import pygame
import random
import math

pygame.init()

screen = pygame.display.set_mode((800, 600))


# Background
background = pygame.image.load("background_resized.jpg")

# Title and icon
pygame.display.set_caption("Space invaders")
icon = pygame.image.load("spaceship.png")
pygame.display.set_icon(icon)

# Score
score = 0

# Player
playerImg = pygame.image.load("space-invaders.png")
playerX = 368
playerY = 500
playerX_change = 0

# Enemy
enemyImg = pygame.image.load("enemy.png")
enemyX = random.randint(0, 735)
enemyY = random.randint(50, 150)
enemyX_change = 0.1
enemyY_change = 40

# Bullet
bulletImg = pygame.image.load("bullet.png")
bulletX = random.randint(0, 800)
bulletY = 500
bulletY_change = 0.5
bullet_state = "ready"


def player(x: int, y: int) -> None:
    screen.blit(playerImg, (x, y))


def enemy(x: int, y: int) -> None:
    screen.blit(enemyImg, (x, y))


def fire_bullet(x: int, y: int) -> None:
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))


def isCollision(enemyX: int, enemyY: int, bulletX: int, bulletY: int) -> bool:
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
                playerX_change = -0.3
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.3
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bulletX = playerX
                    fire_bullet(playerX, bulletY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    # Spaceship boundries
    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    # Enemy movement
    enemyX += enemyX_change

    if enemyX <= 0:
        enemyX_change = 0.1
        enemyY += enemyY_change
    elif enemyX >= 736:
        enemyX_change = -0.1
        enemyY += enemyY_change

    # Bullet movement
    if bulletY <= 0:
        bulletY = 500
        bullet_state = "ready"

    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    # Collision
    collision = isCollision(enemyX, enemyY, bulletX, bulletY)
    if collision:
        enemyX = random.randint(0, 735)
        enemyY = random.randint(50, 150)
        bulletY = 480
        bullet_state = "ready"
        score += 1
        print(score)

    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()
