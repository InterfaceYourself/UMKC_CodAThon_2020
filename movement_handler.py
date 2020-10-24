class MovementHandler:
    def __init__(self, root):
        self.root = root
        self.previous_mouse_x = None
        self.previous_mouse_y = None

    def bind_callbacks(self):
        self.root.bind('<Button-1>', self._set_mouse_location)
        self.root.bind('<B1-Motion>', self._move)

    def _move(self, event):
        change_in_x = event.x - self.previous_mouse_x
        change_in_y = event.y - self.previous_mouse_y

        self.root.geometry(
            f'+{self.root.winfo_x() + change_in_x}'
            f'+{self.root.winfo_y() + change_in_y}'
        )

    def _set_mouse_location(self, event):
        self.previous_mouse_x = event.x
        self.previous_mouse_y = event.y


class MovementHandlerWithInvertedBounds:
    def __init__(self, root, top_left, bottom_right):
        self.root = root
        self.top_left = top_left
        self.bottom_right = bottom_right

        self._parent = MovementHandler(root)

        self.click_in_bounds = False

    def bind_callbacks(self):
        self.root.bind('<Button-1>', self._set_mouse_location)
        self.root.bind('<B1-Motion>', self._move)

    def _check_click_in_bounds(self, event):
        in_x = self.top_left[0] <= event.x <= self.bottom_right[0]
        in_y = self.top_left[1] <= event.y <= self.bottom_right[1]

        return not (in_x and in_y)

    def _set_mouse_location(self, event):
        self.click_in_bounds = self._check_click_in_bounds(event)

        if not self.click_in_bounds:
            return

        self._parent._set_mouse_location(event)

    def _move(self, event):
        if not self.click_in_bounds:
            return

        self._parent._move(event)