# -*- coding: utf-8 -*-
from ceefax.page import Page
from ceefax import config


class ShowerGelPage(Page):
    def __init__(self, page_num):
        super(ShowerGelPage, self).__init__(page_num)
        self.title = "Shower gel"
        self.in_index = True
        self.tagline = "FREE Shower puff when you spend OVER £10"

    def generate_content(self):
        # Pick randomly
        import random
        outer = [
            ['the', 'kiss'],
            ['my', 'island'],
            ['marsh', 'hearts'],
            ['her', 'thoughts'],
            ['one', 'morning'],
            ['', 'love'],
            ['that', 'moment'],
            ['sweet', 'zing'],
            ['fresh', 'tingle'],
            ['the', 'secret'],
            ['gentle', 'love'],
            ['water', 'splash'],
            ['fizzy', 'party'],
            ['wild', 'magic'],
            ['slow', 'horses'],
            ['neutral', 'hotel'],
            ['crazy', 'horses'],
            ['deus', 'machina'],
            ['last', 'christmas'],
            ['torchy', 'boy'],
            ['university', 'london'],
            ['see it', 'sorted'],
            ['music', 'podcasts']]
        inner = [
            'raspberry',
            'coconut',
            'mallow',
            'mango',
            'ginger',
            'brazilian',
            'vanilla',
            'lime',
            'mint',
            'honeycomb',
            'powder',
            'melon',
            'prosecco',
            'cherry',
            'milk',
            'ex',
            'battery',
            'college',
            'radio',
            'cherry',
            'banana',
            'duckling',
            'apple',
            'easy peeler']

        chosen_outer = random.choice(outer)
        chosen_inner = random.choice(inner)

        if random.randint(0, 99) in [0, 1]:
            chosen_outer = ['pink', 'everywhere']
            chosen_inner = 'shit'
        elif random.randint(0, 99) in [2]:
            chosen_outer = ['nivea', 'men']
            chosen_inner = 'for'

        self.add_title("Shower gel", font="size4", fg="ORANGE",
                       bg="BRIGHTWHITE")

        book_width = 41
        book_height = 29
        top_margin = 11
        left_margin = (config.WIDTH - book_width) // 2

        book = "x" * book_width + "\n"
        book += ("x" + "-" * (book_width - 2) + "x" + "\n") * (book_height - 2)
        book += "x" * book_width + "\n"
        book = book.replace(" ", "-").replace("x", "W")
        color = random.choice(['g', 'r', 'o', 'c', 'b', 'm', 'R', 'y', 'G',
                               'C', 'B', 'p'])
        self.print_image(book.replace('g', color), top_margin, left_margin)

        top = ("---------------ggggggggggg---------------\n"
               "--------------ggggggggggggg--------------\n"
               "--------------ggggggggggggg--------------\n"
               "--------------ggggggggggggg--------------\n"
               "--------------ggggggggggggg--------------\n"
               "--------------ggggggggggggg--------------\n"
               "--------------ggggggggggggg--------------\n"
               "--------------ggggggggggggg--------------\n"
               "-----------------------------------------\n"
               "--xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx--\n"
               "-x-------------------------------------x-\n"
               "x---------------------------------------x")
        top = top.replace(" ", "-").replace("x", "W")
        self.print_image(top.replace('g', color), top_margin - 5, left_margin)

        self.move_cursor(x=left_margin + 2,
                         y=top_margin + book_height // 2 - 13)
        self.add_title_wrapped(chosen_outer[0], font="size4", fg="BLACK",
                               bg="BRIGHTWHITE", pre=left_margin + 2,
                               fill=False, max_width=book_width - 4,
                               center=True)
        self.move_cursor(x=left_margin + 2,
                         y=top_margin + book_height // 2 - 9)
        self.add_title_wrapped(chosen_inner, font="size4", fg="BLACK",
                               bg=color, pre=left_margin + 2, fill=False,
                               max_width=book_width - 4, center=True)
        self.move_cursor(x=left_margin + 2,
                         y=top_margin + book_height // 2 - 5)
        self.add_title_wrapped(chosen_outer[1], font="size4", fg="BLACK",
                               bg="BRIGHTWHITE", pre=left_margin + 2,
                               fill=False, max_width=book_width - 4,
                               center=True)


lamb01 = ShowerGelPage("179")
lamb01.importance = 4
