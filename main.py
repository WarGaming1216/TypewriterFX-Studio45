from pynput import keyboard
import pygame

pygame.mixer.init()
click = pygame.mixer.Sound("sounds/key/key.wav")

def on_press(key):
    try:
        click.play()
    except Exception as e:
        pass

listener = keyboard.Listener(on_press=on_press)
listener.start()

print("TypewriterFX iniciado.")
print("Presiona Ctrl+C para salir.")

listener.join()