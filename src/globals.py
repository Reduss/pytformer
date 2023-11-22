import pygame
from scene import Scene, SceneManager, MainMenuScene
from input_stream import InputStream

SCREEN_SIZE = (800, 800)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARK_GREY = (50,50,50)

pygame.init()

CLOCK: pygame.time.Clock = pygame.time.Clock()
FONT = pygame.font.Font(None, 36)
SCREEN = pygame.display.set_mode(SCREEN_SIZE)

INPUT_STREAM = InputStream()
SCENE_MANAGER = SceneManager()

SCENE_MANAGER.push(MainMenuScene())