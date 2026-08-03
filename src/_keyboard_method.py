import msvcrt


_DEFAULT_KEY_MAP = {
    " ": "SPACE",
    "\r": "ENTER",
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
    "\x0b": "CTRL+K",
    "\x0c": "CTRL+L",
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
    "\x00R": "NUMPAD_INSERT",
    "\xe0R": "INSERT",
    "\x00S": "NUMPAD_DELETE",
    "\xe0S": "DELETE",
    "\x00G": "NUMPAD_HOME",
    "\xe0G": "HOME",
    "\x00O": "NUMPAD_END",
    "\xe0O": "END",
    "\x00I": "PAGE_UP",
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
    "\xe0\x86": "F12",
}


def _get_key_code() -> str:
    key = msvcrt.getwch()

    if key in ("\x00", "\xe0"):
        key += msvcrt.getwch()

    return key


def _get_key(key_map: dict[str, str] = _DEFAULT_KEY_MAP) -> str | None:
    key_code = _get_key_code()
    return key_map.get(key_code) or key_code.isprintable() and key_code


def keyboard_listening(callback):
    while callback(_get_key()):
        pass
