import pygame.image

SIZE = (1280, 720)
FPS = 60

BACKGROUND_COLOR = (86, 151, 191)

BULLET_SPEED = 10
BULLET_SIZE = 5

PLANE_SIZE = (100, 25)
PLANE_SPEED = 1

MODELS_FOLDER = "C:\Git\AAW\Models"

GUN_SIZE = (50, 100)
GUN_IMAGE = pygame.transform.scale(pygame.transform.rotate(
    pygame.image.load("C:\Git\AAW\Assets\gun.png"), 90
), GUN_SIZE)
