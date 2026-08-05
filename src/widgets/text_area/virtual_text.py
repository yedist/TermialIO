class VirtualText:
    def __init__(self):
        self.cursor_x = 0
        self.cursor_y = 0
        self.preferred_x = 0
        self._lines = [[]]

    @property
    def currect_line(self):
        return self._lines[self.cursor_y]

    def set_cursor(self, x=None, y=None):
        if x == -1:
            self.cursor_x = len(self.currect_line)
        elif x is not None:
            self.cursor_x = x

        if y == -1:
            self.cursor_y = len(self._lines) - 1
        elif y is not None:
            self.cursor_y = y

    def change_cursor(self, x=None, y=None):
        if x is not None:
            self.cursor_x += x

        if y is not None:
            self.cursor_y += y

    def cursor_up(self):
        if self.cursor_y:
            self.change_cursor(y=-1)
            self.set_cursor(x=min(self.preferred_x, len(self.currect_line)))
        else:
            self.set_cursor(x=0)
            self.preferred_x = self.cursor_x

    def cursor_down(self):
        if self.cursor_y < (len(self._lines) - 1):
            self.change_cursor(y=1)
            self.set_cursor(x=min(self.preferred_x, len(self.currect_line)))
        else:
            self.set_cursor(x=-1)
            self.preferred_x = self.cursor_x

    def cursor_left(self):
        if self.cursor_x:
            self.change_cursor(x=-1)
        elif self.cursor_y:
            self.change_cursor(y=-1)
            self.set_cursor(x=-1)

        self.preferred_x = self.cursor_x

    def cursor_right(self):
        if self.cursor_x < len(self.currect_line):
            self.change_cursor(x=1)
        elif self.cursor_y < (len(self._lines) - 1):
            self.change_cursor(y=1)
            self.set_cursor(x=0)
        
        self.preferred_x = self.cursor_x

    def write(self, string):
        for index, line in enumerate(string.split("\n")):
            if index:
                self.new_line()

            self.currect_line[self.cursor_x:self.cursor_x] = line
            self.change_cursor(x=len(line))

        self.preferred_x = self.cursor_x

    def new_line(self):
        save = self.currect_line[self.cursor_x:]
        del self.currect_line[self.cursor_x:]
        self._lines.insert(self.cursor_y + 1, save)
        self.change_cursor(y=1)
        self.set_cursor(x=0)

    def del_line(self):
        if self.cursor_y:
            line = self.currect_line
            del self._lines[self.cursor_y]
            self.change_cursor(y=-1)
            self.set_cursor(x=-1)
            self._lines[self.cursor_y].extend(line)

    def del_char(self):
        if self.cursor_x:
            self.currect_line.pop(self.cursor_x - 1)
            self.change_cursor(x=-1)
        else:
            self.del_line()
