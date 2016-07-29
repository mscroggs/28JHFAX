﻿import os
from page import Page
import colours
from printer import instance as printer

r1 = Page("581")
r1.title = "Bad Tempered Cake"
r1.in_index = False
r1.content = (colours.colour_print(
    printer.text_to_ascii("bad tempered cake"),
    colours.Background.RED,
    colours.Foreground.BLUE) +
u"""
    ½ lb    Rich tea and/or digestive biscuits
    4 oz    Margarine
    1 dsp   Sugar
    3 dsp   Cocoa
    3 dsp   Drinking chocolate
   1½ tbsp  Golden syrup
    2 oz    Sultanas
    2 bars  Milk chocolate

1. Break the biscuits.
2. Melt the margarine, sugar, cocoa, drinking chocolate and syrup over a medium
   heat.
3. Mix with biscuits and sultanas and press down in baking tray.
4. Cover with melted milk chocolate.
5. Leave in the fridge to set""")

r2 = Page("582")
r2.title = "Huda Friendship Cake"
r2.in_index = False
r2.content = (colours.colour_print(
    printer.text_to_ascii("Huda Friendship Cake"),
    colours.Background.RED,
    colours.Foreground.BLUE) +
"""
"""+colours.Foreground.GREEN+"""Day 1:    """+colours.Foreground.DEFAULT+"""Put me in a large mixing bowl and cover loosely with a tea towel.
"""+colours.Foreground.GREEN+"""Days 2-3: """+colours.Foreground.DEFAULT+"""Stir well.
"""+colours.Foreground.GREEN+"""Day 4:    """+colours.Foreground.DEFAULT+"""HUDA HUNGRY. Add 1 cup each of plain flour, sugar and milk.
          Stir well.
"""+colours.Foreground.GREEN+"""Days 5-8: """+colours.Foreground.DEFAULT+"""Stir well.
"""+colours.Foreground.GREEN+"""Day 9:    """+colours.Foreground.DEFAULT+"""Add the same as day 4 and stir well. Divide into 4 equal portions and
          give away to friends with a copy of these instructions. Keep the
          fourth portion.
"""+colours.Foreground.GREEN+"""Day 10:   """+colours.Foreground.DEFAULT+"""Now you are ready to make the cake. Stir well and add the following:
"""+colours.Style.BOLD+colours.Foreground.YELLOW+"""    1 cup of sugar (8oz or 225g)     2 cups plain flour (10oz or 300g)
    half tsp. salt                   2/3 cup of cooking oil (5.3oz or 160ml)
    2 eggs                           2 tsp. vanilla essence
    2 cooking apples cut into chunks 1 cup raisins (7oz or 200g)
    2 heaped tsp. cinnamon           2 heaped tsp. baking powder
"""+colours.Style.DEFAULT+colours.Foreground.YELLOW+"""    Optional: 1/4 cup brown sugar    Optional: 1/4 cup melted butter"""+colours.Foreground.DEFAULT+"""
    Mix everything together and put into a large greased baking tin. Sprinkle
    with a quarter of a cup of brown sugar and a quarter of a cup of melted
    butter. Bake for 45 minutes at 170-180C.
    Test the middle with a clean knife; you may need to cover in tin foil and
    bake for a further 20 minutes to make sure Huda is cooked properly
    in the middle.
    When baked, Huda can be frozen.
""")

r3 = Page("583")
r3.title = "Cherry Clafoutis"
r3.in_index = False
r3.content = (colours.colour_print(
    printer.text_to_ascii("cherry clafoutis"),
    colours.Background.RED,
    colours.Foreground.BLUE) +
"""
    4       Eggs
    1 jar   Cherries
    ? ???   Flour


1. To be continued...""")

r4 = Page("584")
r4.title = "Cheese Twists"
r4.in_index = False
r4.content = (colours.colour_print(
    printer.text_to_ascii("cheese twists"),
    colours.Background.RED,
    colours.Foreground.BLUE) +
"""
    1 sheet Puff pastry (all butter)
    100g    Soft cheese
    100g    Pesto (see page 585)
    1       Egg (yolk only)

1. Cut pastry sheet in half.
2. Spread soft cheese on one half.
3. Spread pesto on the cheese.
4. Cover with the other half of pastry (like a sandwich).
5. Cut into 1cm wide, 6cm long strips. Twist and place on a baking tray.
6. Bake in the oven for 20 minutes at 180"""+u"\u00b0"+"C")

r5 = Page("585")
r5.title = "Pesto"
r5.in_index = False
r5.content = (colours.colour_print(
    printer.text_to_ascii("hey pesto!"),
    colours.Background.RED,
    colours.Foreground.BLUE) +
"""
    100g    Pine nuts
    100g    Parmesan cheese
    50g     Olive oil
    4 cloves of Garlic
    One large basil plant (or two small basil plants)

1. Put in blender.
2. Turn on blender.
3. Wait.
4. Turn off blender.
5. Hey Pesto!

    Note: You can make other kinds of pesto if you replace the basil with
    another ingredient, such as rocket, mint or sundried tomatoes. In fact,
    if you put straw rather than basil leaves, you end up with HEY PESTO!""")


r_index = Page("580")
r_index.title = "Recipes Index"
r_index.content = (colours.colour_print(
    printer.text_to_ascii("recipes", padding={"left": 8}),
    colours.Background.RED,
    colours.Foreground.BLUE) + "\n\n")

for r in [r1,r2,r3,r4,r5]:
    r_index.content += colours.Background.BLUE+r.number+colours.Background.DEFAULT+" "+r.title+"\n"
