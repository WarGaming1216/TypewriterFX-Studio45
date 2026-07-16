from pynput import keyboard


class KeyboardListener:

    def __init__(self, sound_manager):
        self.sound_manager = sound_manager

    def on_press(self, key):
        try:
            self.sound_manager.play_click()
        except Exception as e:
            print(f"Error al reproducir el sonido: {e}")

    def start(self):
        listener = keyboard.Listener(on_press=self.on_press)
        listener.start()
        listener.join()
