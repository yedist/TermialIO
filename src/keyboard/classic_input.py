from keyboard_method_abc import KeyboardMethod


class ClassicInput(KeyboardMethod):
    def __init__(self):
        self.value = ""

    def __call__(self, key: str):
        spacial = ["SPACE", "TAB", "BACKSPACE", "ENTER"]

        if string := (key in spacial or len(key) == 1) and key:
            match string:
                case "SPACE":
                    self.value += " "
                    string = " "
                case "TAB":
                    self.value += " " * 4
                    string = "\t"
                case "BACKSPACE":
                    self.value = self.value[:-1]
                    string = "\b \b"
                case "ENTER":
                    print()
                    return False
                case _:
                    self.value += string

            print(string, end="", flush=True)
        
        return True
