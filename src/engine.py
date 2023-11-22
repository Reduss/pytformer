from globals import *


class Entity:
    def render(self):
        return


class Character(Entity):
    def __init__(self) -> None:
        self.position: tuple[int, int] = (0, 0)
        self.velocity2d: tuple[float, float] = (0, 0)
        self.width = 10
        self.height = 10
    
    def render(self):
        rectangle_surface = pygame.Surface((self.width, self.height))
        rectangle_surface.fill(WHITE)

        SCREEN.blit(rectangle_surface, self.position)
