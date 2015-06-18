import os
from os.path import join,expanduser
from page import Page
from printer import instance as printer
from math import floor

def points_format(points):
    points = int(points)
    points /= 10
    points = int(floor(points))
    return str(points)

class PointsPage(Page):
    def __init__(self, page_num):
        super(PointsPage, self).__init__(page_num)
        self.title = "House Points"

    def generate_content(self):
        import json
        from operator import itemgetter
        with open(join(expanduser('~'),'.klb/points')) as f:
            data = json.load(f)

        if "Gryffindor" in data: g = points_format(data["Gryffindor"])
        else:                    g = "0"
        if "Hufflepuff" in data: h = points_format(data["Hufflepuff"])
        else:                    h = "0"
        if "Slytherin" in data:  s = points_format(data["Slytherin"])
        else:                    s = "0"
        if "Squib" in data:     sq = points_format(data["Squib"])
        else:                   sq = "0"
        if "Ravenclaw" in data:  r = points_format(data["Ravenclaw"])
        else:                    r = "0"
        if "Durmstrang" in data: d = points_format(data["Durmstrang"])
        else:                    d = "0"

        content = self.colours.colour_print(printer.text_to_ascii("decapoints"))
        content += "\nWhat do points mean?\n"

        content += self.colours.colour_print_join([
                        (printer.text_to_ascii(g,False)+"\nGryffindor",
                            self.colours.Background.RED,
                            self.colours.Foreground.YELLOW+self.colours.Style.BOLD),
                        (printer.text_to_ascii(s,False)+"\nSlytherin",
                            self.colours.Style.BLINK,
                            self.colours.Foreground.GREEN),
                        (printer.text_to_ascii(sq,False)+"\nSquib",
                            self.colours.Background.BLUE,
                            self.colours.Foreground.MAGENTA)
                    ]," "," ")
        content += "\n"
        content += self.colours.colour_print_join([
                        (printer.text_to_ascii(r,False)+"\nRavenclaw",
                            self.colours.Background.BLUE,
                            self.colours.Foreground.WHITE+self.colours.Style.BOLD),
                        (printer.text_to_ascii(h,False)+"\nHufflepuff",
                            self.colours.Style.BLINK,
                            self.colours.Foreground.YELLOW+self.colours.Style.BOLD),
                        (printer.text_to_ascii(d,False)+"\nDurmstrang",
                            self.colours.Background.GREEN,
                            self.colours.Foreground.RED)
                    ]," "," ")
        content += "\n"
        sorted_pts = sorted(data.items(),key=itemgetter(1),reverse=True)

        content += "Full List\n"
        i=0
        for house,points in sorted_pts:
            i+=1
            content += self.colours.Foreground.YELLOW + house + self.colours.Foreground.DEFAULT
            content += " "
            content += self.colours.Foreground.GREEN + str(points) + self.colours.Foreground.DEFAULT
            if i%4==0:  content += "\n"
            else:       content += "  "

        self.content = content

page_number = os.path.splitext(os.path.basename(__file__))[0]
p_page = PointsPage(page_number)

class SecretPage(Page):
    def __init__(self, page_num):
        super(SecretPage, self).__init__(page_num)
        self.title = "Secret Page"
        self.is_enabled = False

    def generate_content(self):

        content = self.colours.colour_print(printer.text_to_ascii("secret page"))
        content += "\n\n"
        content += "You have found the secret page!\n\n"
        content += self.colours.colour_print(printer.text_to_ascii("go puffs!"))

        self.content = content

s_page = SecretPage("042")
