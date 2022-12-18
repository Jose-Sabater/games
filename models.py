import pygame
from dataclasses import dataclass
import random


# Player
@dataclass
class Player:
    """
    Dataclass for storing new player information

    Attributes:
        - img: Spaceship image
        - x: horizontal coordinate
        - y: vertical coordinate
        - xchange: the value of change in x
    """

    img: pygame.Surface = pygame.image.load(
        "./static/icons/space-invaders.png"
    )
    x: int = 368
    y: int = 500
    xchange: float = 0


@dataclass
class PlayerFast(Player):
    """
    Player class with faster move speed
    """

    speed: float = 0.5
    bullet_speed: float = 0.5
    health: int = 3


@dataclass
class PlayerStrong(Player):
    """
    Player class with more health
    """

    speed: float = 0.3
    bullet_speed: float = 0.5
    health: int = 5


@dataclass
class PlayerFastShot(Player):
    """
    Player class with faster guns
    """

    speed: float = 0.3
    bullet_speed: float = 0.7
    health: int = 2


# Enemy
@dataclass
class Enemy:
    """
    Dataclass for storing new enemy information

    Attributes:
        - img: Enemy image
        - x: horizontal coordinate
        - y: vertical coordinate
        - xchange: the value of change in x
        - ychange: the value of change in y
    """

    img = pygame.image.load("./static/icons/alien64.png")
    x: int = None
    y: int = None
    xchange: float = 0.1
    ychange: int = 40

    def __post_init__(self):
        if self.x is None:
            self.x = random.randint(0, 735)
        if self.y is None:
            self.y = random.randint(50, 150)
