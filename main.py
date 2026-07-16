from src.sound_manager import SoundManager
from src.keyboard_listener import KeyboardListener

sound_manager = SoundManager()

listener = KeyboardListener(sound_manager)

print("TypewriterFX iniciado.")
print("Presiona Ctrl+C para salir.")

listener.start()
