from ceefax.page import Page
from textwrap import fill


class TubePage(Page):
    def __init__(self, page_num):
        super().__init__(page_num)
        self.title = "Tube Line Status"
        self.importance = 5

    def background(self):
        import tubestatus
        # Create a new status object for retrieving data
        self.current_status = tubestatus.Status()

    def generate_content(self):
        self.add_title("Tube Lines")
        # Get a list of tube lines
        # Loop through the lines and print the status of each one
        lines_tube = ['Bakerloo', 'Central', 'Circle', 'District',
                      'Hammersmith and City', 'Jubilee', 'Metropolitan',
                      'Northern', 'Piccadilly', 'Victoria',
                      'Waterloo and City']
        lines_other = ['DLR', 'Overground', 'TfL Rail', 'Trams']

        colours_tube = ["ORANGE", "RED", "YELLOW", "GREEN", "PINK", "GREY",
                        "MAGENTA", "DEFAULT", "BLUE", "LIGHTBLUE", "LIGHTCYAN"]
        colours_tube_text = ["WHITE", "WHITE", "BLACK", "BLACK", "BLACK",
                             "WHITE", "WHITE", "WHITE", "WHITE", "WHITE",
                             "BLACK"]

        colours_other = ["CYAN", "ORANGE", "BLUE", "LIGHTGREEN"]
        colours_other_text = ["BLACK", "BLACK", "WHITE", "BLACK"]

        mapping = [
            ('London Overground', 'LO'),
            ('London Buses', 'Buses'),
            ('London Underground', 'LU'),
            ('King\'s Cross St. Pancras', 'KX'),
            ('Kings Cross St. Pancras', 'KX'),
            ('Tottenham Court Road', 'TCR'),
            ('Highbury & Islington', 'H&I'),
            ('Harrow & Wealdstone', 'H&W'),
            ('Kensington (Olympia)', 'Olympia'),
            ('Cross', 'X'),
            ('Road', 'Rd'),
            ('Square', 'Sq'),
            ('Street', 'St'),
            ('Junction', 'Jn'),
            ('Airport', 'Apt'),
            ('Town', 'Tn'),
            ('Park', 'Pk'),
            ('Lane', 'Ln'),
            ('Hill', 'Hl'),
            ('Central', 'Ctl'),
            ('North ', 'N '),
            ('South ', 'S '),
            ('East ', 'E '),
            ('West ', 'W ')]

        good = []
        for line, fg, bg in zip(lines_tube + lines_other,
                                colours_tube_text + colours_other_text,
                                colours_tube + colours_other):
            desc = self.current_status.get_status(line).description
            if desc == "Good Service":
                good.append((line, fg, bg))
            else:
                self.start_fg_color(fg)
                self.start_bg_color(bg)
                self.add_text(" " + str(line).replace(
                    "and", "&") + " " * (
                        20 - len(str(line).replace("and", "&"))))
                self.end_bg_color()
                self.end_fg_color()
                if desc == "Minor Delays":
                    self.start_fg_color("YELLOW")
                elif desc == "Part Closure":
                    self.start_fg_color("ORANGE")
                elif desc == "Special Service":
                    self.start_fg_color("LIGHTCYAN")
                else:
                    self.start_fg_color("LIGHTRED")

                full_description = ""
                full_description += self.current_status.get_status(
                    line).description
                description = self.current_status.get_status(
                    line).status_details
                for k, v in mapping:
                    description = description.replace(k, v)
                if len(description) > 1:
                    full_description += ": " + description
                self.move_cursor(x=22)
                self.add_wrapped_text(fill(full_description, 57).replace(
                    '\n', '\n' + " " * 22), pre=22)
                self.end_fg_color()
                self.add_newline()

        self.add_newline()

        for line, fg, bg in good:
            desc = self.current_status.get_status(line).description
            self.start_fg_color(fg)
            self.start_bg_color(bg)
            self.add_text(" " + str(line).replace(
                "and", "&") + " " * (20 - len(str(line).replace("and", "&"))))
            self.end_bg_color()
            self.start_fg_color("GREEN")

            self.add_wrapped_text(" Good service", pre=24)
            self.end_fg_color()
            self.add_newline()


page = TubePage("849")
