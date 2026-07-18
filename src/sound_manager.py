from pathlib import Path
import pygame
import random


class SoundManager:

    def __init__(self, theme_path):
        pygame.mixer.init()

        self.theme_path = Path(theme_path)

        self.sounds = {}

        for folder in self.theme_path.iterdir():
            if folder.is_dir():
                self.sounds[folder.name] = self._load_folder(folder)

    def _load_folder(self, folder):
        sounds = [pygame.mixer.Sound(str(file)) for file in folder.glob("*.wav")]

        print(f"{folder.name}: {len(sounds)} sonidos cargados")

        return sounds

    def play(self, sound_type):
        sounds = self.sounds.get(sound_type)

        if not sounds:
            print(f"\tNo hay sonidos para '{sound_type}'")
            return

        random.choice(sounds).play()
