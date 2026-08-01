import msvcrt


KEY_NAMES = {
    "\r": "ENTER",
    "\n": "LINE_FEED",
    "\b": "BACKSPACE",
    "\t": "TAB",
    "\x1b": "ESC",

    "\x01": "CTRL+A",
    "\x02": "CTRL+B",
    "\x03": "CTRL+C",
    "\x04": "CTRL+D",
    "\x05": "CTRL+E",
    "\x06": "CTRL+F",
    "\x07": "CTRL+G",

    # CTRL+H = \x08, אבל \x08 הוא BACKSPACE
    # CTRL+I = \x09, אבל \x09 הוא TAB
    # CTRL+J = \x0a, אבל \x0a הוא LINE_FEED

    "\x0b": "CTRL+K",
    "\x0c": "CTRL+L",

    # CTRL+M = \x0d, אבל \x0d הוא ENTER

    "\x0e": "CTRL+N",
    "\x0f": "CTRL+O",
    "\x10": "CTRL+P",
    "\x11": "CTRL+Q",
    "\x12": "CTRL+R",
    "\x13": "CTRL+S",
    "\x14": "CTRL+T",
    "\x15": "CTRL+U",
    "\x16": "CTRL+V",
    "\x17": "CTRL+W",
    "\x18": "CTRL+X",
    "\x19": "CTRL+Y",
    "\x1a": "CTRL+Z",

    "\xe0H": "ARROW_UP",
    "\xe0P": "ARROW_DOWN",
    "\xe0K": "ARROW_LEFT",
    "\xe0M": "ARROW_RIGHT",
    "\x00H": "NUMPAD_UP",
    "\x00P": "NUMPAD_DOWN",
    "\x00K": "NUMPAD_LEFT",
    "\x00M": "NUMPAD_RIGHT",

    "\xe0R": "INSERT",
    "\x00R": "INSERT",
    "\xe0S": "DELETE",
    "\x00S": "DELETE",
    "\xe0G": "HOME",
    "\x00G": "HOME",
    "\xe0O": "END",
    "\x00O": "END",
    "\xe0I": "PAGE_UP",
    "\x00I": "PAGE_UP",
    "\xe0Q": "PAGE_DOWN",
    "\x00Q": "PAGE_DOWN",

    "\x00;": "F1",
    "\x00<": "F2",
    "\x00=": "F3",
    "\x00>": "F4",
    "\x00?": "F5",
    "\x00@": "F6",
    "\x00A": "F7",
    "\x00B": "F8",
    "\x00C": "F9",
    "\x00D": "F10",
    "\x00\x85": "F11",
    "\x00\x86": "F12",
}

def get_char():
    char = msvcrt.getwch()

    if char in ("\x00", "\xe0"):
        char += msvcrt.getwch()
        return KEY_NAMES.get(char, char)

    return KEY_NAMES.get(char, char)

def keyboard_loop():
    while True:
        print(repr(get_char()))


def smart_input(message=""):
    ...

keyboard_loop()
