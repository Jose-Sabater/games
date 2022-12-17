import pygame
import random
import math

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
playerImg = pygame.image.load("./static/icons/space-invaders.png")
playerX = 368
playerY = 500
playerX_change = 0

# Enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load("./static/icons/enemy.png"))
    enemyX.append(random.randint(0, 735))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(0.1)
    enemyY_change.append(40)

# Bullet
bulletImg = pygame.image.load("./static/icons/bullet.png")
bulletX = random.randint(0, 800)
bulletY = 500
bulletY_change = 0.5
bullet_state = "ready"

# Score
score_value = 0
font = pygame.font.Font("freesansbold.ttf", 32)
scoreX = 10
scoreY = 10


def show_score(x: int, y: int) -> None:
    score = font.render(f"Score: {str(score_value)}", True, (255, 255, 255))
    screen.blit(score, (x, y))


def player(x: int, y: int) -> None:
    screen.blit(playerImg, (x, y))


def enemy(x: int, y: int, i: int) -> None:
    screen.blit(enemyImg[i], (x, y))


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
    for i in range(num_of_enemies):

        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 0.1
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -0.1
            enemyY[i] += enemyY_change[i]

        # Collision
        collision = is_collision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            enemyX[i] = random.randint(0, 735)
            enemyY[i] = random.randint(50, 150)
            bulletY = 480
            bullet_state = "ready"
            score_value += 1
            print(score_value)

        enemy(enemyX[i], enemyY[i], i)

    # Bullet movement
    if bulletY <= 0:
        bulletY = 500
        bullet_state = "ready"

    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    player(playerX, playerY)
    show_score(scoreX, scoreY)
    pygame.display.update()
