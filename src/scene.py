from typing import List
import pygame

from input_stream import InputStream
from engine import Character
from globals import *

class Scene:
    def __init__(self) -> None:
        pass
    
    def on_enter(self):
        pass
    
    def on_exit(self):
        pass
    
    def input(self):
        """This basically sets the context of input mappings. Though doesn't look like the bas way of doing this."""
        pass
    
    def update(self):
        pass
    
    def render(self):
        pass

class SceneManager:
    def __init__(self) -> None:
        self.scenes: List[Scene] = []
    
    def is_empty(self):
        return len(self.scenes) == 0
    
    def enter_scene(self):
        if not self.is_empty():
            self.scenes[-1].on_enter()
    
    def exit_scene(self):
        if not self.is_empty():
            self.scenes[-1].on_exit()
    
    def push(self, sc: Scene):
        self.exit_scene()
        self.scenes.append(sc)
        self.enter_scene()
    
    def pop(self):
        self.exit_scene()
        self.scenes.pop()
        self.enter_scene()
    
    def update(self):
        self.scenes[-1].update()

    def render(self):
        self.scenes[-1].render()
    
    def input(self):
        self.scenes[-1].input()
    
    def set(self, scs: List[Scene]):
        self.scenes.clear()
        for s in scs:
            self.scenes.append(s)

class MainMenuScene(Scene):
    def render(self):
        SCREEN.fill(DARK_GREY)
        s = 'This is main menu, press SPACE to enter the game'
        menu_text = FONT.render(s, True, WHITE)
        SCREEN.blit(menu_text, (10, 10))
        pygame.display.flip()

    def input(self):
        if INPUT_STREAM.is_key_pressed(pygame.K_SPACE):
            SCENE_MANAGER.push(InGameScene())


class InGameScene(Scene):
    def __init__(self) -> None:
        self.hero = Character()
    
    def render(self):
        SCREEN.fill(DARK_GREY)
        
        fps = int(CLOCK.get_fps())
        fps_text = FONT.render(f'FPS: {fps}', True, 'white')
        SCREEN.blit(fps_text, (10, 10))
        
        self.hero.render()
        pygame.display.flip()
    
    def input(self):
        if INPUT_STREAM.is_key_released(pygame.K_RIGHT):
            self.hero.velocity2d = (0, 0)
        if INPUT_STREAM.is_key_pressed(pygame.K_ESCAPE):
            SCENE_MANAGER.pop()
        if INPUT_STREAM.is_key_down(pygame.K_RIGHT):
            self.hero.velocity2d = (10, 0)

    def update(self):
        pass
