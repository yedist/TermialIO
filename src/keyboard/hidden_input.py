from keyboard_method_abc import KeyboardMethod


class ClassicInput:
    def __init__(self):
        self.value = ""

    def __call__(self, key: str):
        spacial = ["SPACE", "TAB", "BACKSPACE", "ENTER"]

        if string := (key in spacial or len(key) == 1) and key:
            match string:
                case "SPACE":
                    self.value += " "
                case "TAB":
                    self.value += " " * 4
                case "BACKSPACE":
                    self.value = self.value[:-1]
                case "ENTER":
                    print()
                    return False
                case _:
                    self.value += string
        
        return True
