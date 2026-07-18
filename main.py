from src.sound_manager import SoundManager
from src.theme_manager import ThemeManager
from src.keyboard_listener import KeyboardListener

theme = ThemeManager("themes/studio45")

print(f"Tema seleccionado: {theme.display_name}")

sound_manager = SoundManager(theme.path)

listener = KeyboardListener(sound_manager)

print("TypewriterFX iniciado.")
print("Presiona Ctrl+C para salir.")

listener.start()
