# -*- coding: utf-8 -*-
from ceefax.page import Page
from ceefax import config


class LambPage(Page):
    def __init__(self, page_num):
        super().__init__(page_num)
        self.title = "Jackson Lamb novel"
        self.index_num = page_num
        self.tagline = ("Another tale from the inimitable chronicles "
                        "of Jackson Lamb")

    def generate_content(self):
        # Pick randomly
        import random
        titles = [
            'Slow Horses',
            'Dead Lions',
            'Real Tigers',
            'Stoned Pigeons',
            'Spooky Street',
            'London Rules',
            'Joe Country',
            'Quantum Lamb',
            'Mining Lamb',
            'Regle du Jeu',
            'Tidal Lamb',
            'Et tu, Lamb',
            'Bravo, Lamb',
            'Curse of Lamb',
            'Don\'t fail me Lamb',
            'Son of a Lamb',
            'Mackerel Lamb',
            'Anatomy Lamb',
            'Lamb in Time',
            'Outback Lamb',
            'Sacred Texts',
            'That\'s it. Finished',
            'Return of Lamb',
            'Lamb\'s Ressurection',
            'Baa-baa braLamb',
            'Grand\'s Lamb',
            'Lamb & Pineapple',
            'Look of Lamb',
            'Casino RoyLamb',
            'Money Penny Goes for Lamb',
            'Le Chiffre\'s Torture of the Lamb',
            'Home James, Don\'t Spare the Lamb',
            'Sir James\' Trip to Find Lamb',
            'Look of Lamb (Instrumental)',
            'Hi There Miss GoodLamb',
            'Little French Lamb',
            'Flying Lamb',
            'The Venerable Sir Jackson Lamb',
            'Dream on Lamb, You\'re Lamb',
            'The Big Cowboys and Lamb Fight at Casino RoyLamb',
            'Casino RoyLamb (Reprise)',
            'Lamb Korma',
            'Lamb Passanda',
            'Lamb Tikka Masala',
            'Lamb Dhansak',
            'Lamb Jalfrezi',
            'Lamb Madras',
            'Lamb Vindaloo',
            'Lamb Phall',
            'Fireman Lamb',
            'Green Eggs and Lamb',
            'Lambda',
            'Lady Di Another Day',
            'Lambourine',
            'Lambalaya',
            'Lambagotchi',
            'Lamb.de',
            'Lambp post',
            'Finlamd',
            'Irelamb',
            'Jurrassic Lamb (sic)',
            'Teaches of Lamb',
            'JC2: Loop of Jade',
            'Tied Up In Nottz',
            'Golf Bravo Zero Lamb',
            'Sparkling Lamb',
            'Mango Lamb',
            'The Great Lamb',
            'Bric-a-brac Lamb',
            'Battery Lamb',
            'Fat Lamb',
            'Vegan Lamb',
            'Joe County',
            'Joe 90',
            'Silence of Lamb',
            'Lamb\'s Bum',
            'Astral Lamb',
            'Slough Sandwiches',
            'The Tuna Melt',
            'Jackson Five',
            'Rogue Passander',
            'Surely Ewe Jest?',
            'Uncle Wilburforce',
            'Jo, My Slippers?',
            'Catch the Pigeon',
            'Another Lamb',
            'God Lamb It',
            'Lamb? No I\'m full',
            'Merge Conflicts',
            'Maggot Lamb',
            'Lamb\'s Wife',
            'Lamb Shank',
            'Back to Bedlamb',
            'Fulhamb Broadway',
            'Shepherd\'s Pie',
            'Shepherd\'s Delight',
            'Shepherd\'s Warning',
            'Mackerel Man',
            'Cheeky Lambdo\'s',
            'Lamb Tagine',
            'Lambateur Radio',
            'Lambazon Prime',
            'Hodgkins Lamb',
            'Mallard Lamb',
            'Cod Lamb It',
            'Corona Lamb',
            'Jonti Lamb',
            'The Roman Baths',
            'Clockwork Lamb',
            'Tyre Iron',
            'Lockdown Lamb',
            'Hustings Lamb',
            'Lambd sanitiser',
            'Super Mario Cartwright',
            'All\'s Lamb that ends Lamb',
            'Laaaaaaaaaamb',
            'Newborn Lamb',
            'Disneylambd',
            'Lambd and Deliver',
            'Ostrich Lamb',
            'Untitled Lamb',
            'Lady Di\'s Holiday',
            'Philambderer',
            'Lamb goes to Prison',
            'Prison goes to Lamb',
            'Lady (Di) and the Lambp',
            'Lamb on Toast',
            'Toast on Lamb',
            'Toad Pie',
            'Who took Lamb?',
            'Who shook Lamb?',
            'Who cooked Lamb?',
            'Who pfooked Lamb?',
            'A Time for Lamb',
            'Lamb IV',
            'L. A. M. B.',
            'Jack\'s On Lamb',
            'David Lamberon',
            'The Return of David Lamberon',
            'Even More David Lamberon',
            'I\'ve Had Enough of David Lamberon',
            'What\'s for Dinner? Not Lamb.']
        chosen_book = random.choice(titles)

        self.add_title("Book of the week", font="size4",
                       fg="ORANGE", bg="BRIGHTWHITE")

        book_width = 41
        book_height = 42
        top_margin = 5
        left_margin = (config.WIDTH - book_width) // 2

        book = "x" * book_width + "\n"
        book += ("x" + "-" * (book_width - 2) + "x" + "\n") * (book_height - 2)
        book += "x" * book_width + "\n"
        book = book.replace(" ", "-").replace("x", "W")
        color = random.choice(['g', 'r', 'o', 'c', 'b', 'm', 'R', 'y', 'G',
                               'C', 'B', 'p'])
        self.print_image(book.replace('g', color), top_margin, left_margin)

        spy = ("-----xxxxxxx-----\n"
               "----xxxxxxxxx----\n"
               "----xxxxxxxxx----\n"
               "xxxxxxxxxxxxxxxxx\n"
               "-----------------\n"
               "----ggggggggg----\n"
               "----gggg-gggg----\n"
               "----gggg-gggg----\n"
               "-----------------\n"
               "-xx-----------xx-\n"
               "-xxxx-------xxxx-\n"
               "-xxxxxx---xxxxxx-\n"
               "-xxxxxx---xxxxxx-\n"
               "xxxxxxxxxxxxxxxxx\n"
               "xxxxxxxxxxxxxxxxx\n"
               "xxxxxxxxxxxxxxxxx").replace(" ", "-").replace("x", "W")
        mackerel = ("------------------\n"
                    "------------------\n"
                    "--------xxxxxx----\n"
                    "--------xxxxxx----\n"
                    "------xxxxxxxxxx--\n"
                    "xx----------------\n"
                    "x-x-----xxxxxx----\n"
                    "x--x---xxxxxxxxx--\n"
                    "-x--x-xxxxxxxggggg\n"
                    "-x---xxxxxxxxggxgg\n"
                    "-x--x-xxxxxxxxxxx-\n"
                    "x--x---xxxxxxxxx--\n"
                    "x-x------xxxxx----\n"
                    "xx----------------").replace(" ", "-").replace("x", "W")
        if chosen_book in ["Mackerel Lamb", "Mackerel Man", "Cod Lamb It"]:
            self.print_image(mackerel.replace('g', color),
                             top_margin + 2, left_margin + 12)
        else:
            self.print_image(spy.replace('g', color), top_margin + 2,
                             left_margin + 12)

        author = "M I C K   H E R R O N"
        self.move_cursor(x=left_margin + book_width // 2 - len(author) // 2,
                         y=top_margin + book_height // 2 - 10)
        self.add_text(author)
        self.move_cursor(x=left_margin + 2,
                         y=top_margin + book_height // 2 - 9)
        self.add_title_wrapped(chosen_book.upper(), font="size4", fg="BLACK",
                               bg="BRIGHTWHITE", pre=left_margin + 2,
                               fill=False, max_width=book_width - 4,
                               center=True)


lamb01 = LambPage("181")
lamb01.importance = 4
