from pynput import keyboard


class KeyboardListener:

    def __init__(self, sound_manager):
        self.sound_manager = sound_manager

    def on_press(self, key):
        try:
            self.sound_manager.play_key()
        except Exception as e:
            pass

    def start(self):
        listener = keyboard.Listener(on_press=self.on_press)
        listener.start()
        listener.join()
