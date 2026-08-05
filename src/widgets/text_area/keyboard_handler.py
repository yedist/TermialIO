from keyboard.keyboard_method_abc import KeyboardMethod
from .new import view_update


class KeyboardHandler(KeyboardMethod):
    def __init__(self, text_object):
        self._text = text_object
    
    def __call__(self, key: str):
        spacial = ["SPACE", "TAB", "BACKSPACE", "ENTER", "ARROW_UP", "ARROW_DOWN", "ARROW_RIGHT", "ARROW_LEFT"]

        if string := (key in spacial or len(key) == 1) and key:
            match string:
                case "SPACE":
                    self._text.write(" ")
                case "TAB":
                    self._text.write(" " * 4)
                case "ENTER":
                    self._text.new_line()
                case "BACKSPACE":
                    self._text.del_char()
                case "ARROW_UP":
                    self._text.cursor_up()
                case "ARROW_DOWN":
                    self._text.cursor_down()
                case "ARROW_LEFT":
                    self._text.cursor_left()
                case "ARROW_RIGHT":
                    self._text.cursor_right()
                case _:
                    self._text.write(string)

            view_update(self._text._lines, location={"x": self._text.cursor_x, "y": self._text.cursor_y})

        return True
