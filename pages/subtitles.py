from ceefax.page import Page


class SubtitlesPage(Page):
    def __init__(self):
        super().__init__("888")
        self.importance = 2
        self.title = "Subtitles"

    def generate_content(self):
        self.move_cursor(y=22)
        self.add_title("    subtitles", fg="BLACK",
                       bg="BRIGHTWHITE", font="size4")


p = SubtitlesPage()
