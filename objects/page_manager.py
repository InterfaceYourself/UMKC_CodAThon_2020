class PageManager:
    def __init__(self, parent):
        self.parent = parent
        self.pages = []
        self.index = 0

    def add_pages(self, pages):
        self.pages.extend(pages)

    def start(self):
        self.pages[self.index].place(relx=.16, rely=.2)

    def flip_page(self):
        self.pages[self.index].place_forget()

        self.index += 1

        self.pages[self.index].place(relx=.16, rely=.2)
