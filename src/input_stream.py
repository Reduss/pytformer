import pygame

class InputStream:
    def __init__(self) -> None:
        self.previous_key_states = []
        self.current_key_states = []
    
    def process_input(self):
        self.previous_key_states = self.current_key_states
        self.current_key_states = pygame.key.get_pressed()
    
    def is_key_down(self, key_code):
        """Checks wether the key is being held down"""
        if self._is_keyboard_not_pressed():
            return False
        return self.current_key_states[key_code] == True
    
    def is_key_pressed(self, key_code):
        """Checks wether the key has been pressed once"""
        if self._is_keyboard_not_pressed():
            return False
        return self.current_key_states[key_code] == True and self.previous_key_states[key_code] == False
    
    def is_key_released(self, key_code):
        if self._is_keyboard_not_pressed():
            return False
        return self.current_key_states[key_code] == False and self.previous_key_states[key_code] == True
    
    def _is_keyboard_not_pressed(self):
        return self.previous_key_states is None or self.current_key_states is None