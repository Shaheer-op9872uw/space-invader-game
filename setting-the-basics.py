import math
import random
import pygame 

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500
PLAYER_START_X = 370
PLAYER_START_Y = 380
ENEMY_START_Y_MIN = 50
ENEMY_START_Y_MAX = 150
ENEMY_START_X = 4
ENEMY_START_Y = 40
BULLET_START_Y = 10
COLLISION_DISTANCE = 27
pygame.init()
screen = pygame.display.set_model((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

playerImg = pygame.image.load('player.png')
playerX = PLAYER_START_X
playerY = PLAYER_START_Y
playerX_change = 0

enemyImge = []
enemyX = []
enemyY = []
for i in range(6):
    enemyImg.append(pygame.image.load('enemy.png'))
    enemyX.append(random.randint(0, 736))
    enemyY.append(random.randint(ENEMY_START_Y_MIN, ENEMY_START_Y_MAX))
    enemyY_change.append(ENEMY_SPEED_Y)

bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = BULLET_START_Y
bulletY_change = BULLET_SPEED_Y
bullet_state = "ready"