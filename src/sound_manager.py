from pathlib import Path
import pygame
import random


class SoundManager:

    def __init__(self):
        pygame.mixer.init()

        self.key_sounds = self._load_folder("sounds/key")
        self.space_sounds = self._load_folder("sounds/space")
        self.enter_sounds = self._load_folder("sounds/enter")
        self.backspace_sounds = self._load_folder("sounds/backspace")
        self.shift_sounds = self._load_folder("sounds/shift")

    def _load_folder(self, folder):
        try:
            return [
                pygame.mixer.Sound(str(file)) for file in Path(folder).glob("*.wav")
            ]
        except Exception as e:
            print("Ocurrió un error:", e)

    def play_click(self):
        try:
            random.choice(self.key_sounds).play()
        except Exception as e:
            print(e)

    def play_space(self):
        try:
            random.choice(self.space_sounds).play()
        except Exception as e:
            print(e)

    def play_enter(self):
        try:
            random.choice(self.enter_sounds).play()
        except Exception as e:
            print(e)

    def play_backspace(self):
        try:
            random.choice(self.backspace_sounds).play()
        except Exception as e:
            print(e)

    def play_shift(self):
        try:
            random.choice(self.shift_sounds).play()
        except Exception as e:
            print(e)
