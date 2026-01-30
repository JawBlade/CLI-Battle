from pynput import keyboard

class KeyLogger:
    def __init__(self, character):
        self.character = character

    def on_press(self, key):
        if key == keyboard.KeyCode.from_char('1'):
            return key
        if key == keyboard.KeyCode.from_char('2'):
            return key
        if key == keyboard.KeyCode.from_char('3'):
            return key