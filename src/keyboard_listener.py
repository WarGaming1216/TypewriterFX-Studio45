from pynput import keyboard

KEY_MAPPING = {
    keyboard.Key.space: "space",
    keyboard.Key.enter: "enter",
    keyboard.Key.backspace: "backspace",
    keyboard.Key.shift: "shift",
    keyboard.Key.shift_l: "shift",
    keyboard.Key.shift_r: "shift",
}


class KeyboardListener:

    def __init__(self, sound_manager):
        self.sound_manager = sound_manager

    def on_press(self, key):

        sound_type = KEY_MAPPING.get(key, "key")

        self.sound_manager.play(sound_type)

    def start(self):
        listener = keyboard.Listener(on_press=self.on_press)
        listener.start()
        listener.join()
