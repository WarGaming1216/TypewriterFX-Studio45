from pynput import keyboard

KEY_MAPPING = {
    keyboard.Key.space: "space",
    keyboard.Key.enter: "enter",
    keyboard.Key.backspace: "backspace",
    keyboard.Key.shift: "shift",
    keyboard.Key.shift_r: "shift_r",
    keyboard.Key.ctrl: "control",
    keyboard.Key.ctrl_r: "control_r",
    keyboard.Key.alt: "alt",
    keyboard.Key.alt_gr: "alt_gr",  # Actualmente no funciona, revisar
    keyboard.Key.caps_lock: "caps_lock",
    keyboard.Key.cmd: "cmd",
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
