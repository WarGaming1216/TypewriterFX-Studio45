import pygame


class SoundManager:
    def __init__(self):
        pygame.mixer.init()

        self.click_sound = pygame.mixer.Sound("sounds/key/key.wav")

    def play_click(self):
        try:
            self.click_sound.play()
        except Exception as e:
            pass
