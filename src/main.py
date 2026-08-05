from keyboard.keyboard_listening import keyboard_listening
from widgets.text_area.keyboard_handler import KeyboardHandler
from widgets.text_area.virtual_text import VirtualText


if __name__ == "__main__":
    text = VirtualText()
    keyboard_listening(KeyboardHandler(text))
