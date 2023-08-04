import pygame.image

SIZE = (1280, 720)
FPS = 60

BACKGROUND_COLOR = (86, 151, 191)
BACKGROUND_IMAGE = pygame.transform.scale(
    pygame.image.load(r"C:\Git\AAW\Assets\background.jpg"), SIZE
)

BULLET_SPEED = 15
BULLET_SIZE = 5

PLANE_SIZE = (150, 75)
PLANE_IMAGE = pygame.transform.scale(
    pygame.image.load("C:\Git\AAW\Assets\plane.png"), PLANE_SIZE
)
PLANE_SPEED = 1

MODELS_FOLDER = "C:\Git\AAW\Models"

GUN_SIZE = (50, 100)
GUN_IMAGE = pygame.transform.scale(pygame.transform.rotate(
    pygame.image.load("C:\Git\AAW\Assets\gun.png"), 90
), GUN_SIZE)
