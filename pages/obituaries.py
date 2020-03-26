from ceefax.page import Page
from ceefax import config

class ObitPage(Page):
    def __init__(self, n, which_number, main=None):
        super(ObitPage, self).__init__(n)
        self.title = "Obituaries"
        if n == "260":
            self.in_index = True
            self.importance = 3
            self.index_num = "260-269"
        else:
            self.in_index = False
            self.importance = 2
        self.which_number = which_number
        self.main = main

    def background(self):
        if self.main is None:
            import requests
            from bs4 import BeautifulSoup
            html = requests.get('https://en.wikipedia.org/wiki/Wikipedia%3ADatabase_reports%2FRecent_deaths')
            b = BeautifulSoup(html.text, 'lxml')
            all_people = b.find_all(name = 'tr')
            person_data = [0 for i in range(11)]
            name = [0 for i in range(11)]
            birth = [0 for i in range(11)]
            death = [0 for i in range(11)]
            description = [0 for i in range(11)]
            for i,person in enumerate(all_people[1:12]):
                person_data[i] = person.find_all(name='td')
                name[i] = person_data[i][1].text.replace("\n","")
                birth[i] = person_data[i][2].text[0:4]
                death[i] = person_data[i][3].text[0:4]
                description[i] = person_data[i][4].text.replace("\n","")
            self.name = name
            self.birth = birth
            self.death = death
            self.description = description

    def generate_content(self):
        import random
        self.print_image(
            "-yyyyyyyy--------yyyyyy--------yyyyyyyyy-------yyyyyyyyy----yyyyyyyyy----------\n"
            "-yyyyyyyy--------yyyyyy--------yyyyyyyyy-------yyyyyyyyy----yyyyyyyyy----------\n"
            "-ybbbbbby----------ybby----------ybbybby---------ybbbbyy------ybbbbby----------\n"
            "-ybbyybby-yyyyyyyy-ybby-yyyyyyyy-ybbybby-yyyyyyy-ybbybby-yyyy-ybbyyyy-yyyyyyyy-\n"
            "-ybbyybby-yyyyyyyy-ybby-yyyyyyyy-ybbybby-yyyyyyy-ybbbbyy-yyyy-ybbbbyy-yyyyyyyy-\n"
            "-ybbyybby-ybbbbbyy-ybby-ybbbbbby-ybbybby-yybbbyy-ybbybby-ybby-ybbyyyy-ybbbbbyy-\n"
            "-ybbbbbby-ybbyybby-ybby-yyybbyyy-ybbbbby-ybbybby-ybbybby-ybby-ybbbbby-ybbyyyyy-\n"
            "-yyyyyyyy-ybbbbbyy-yyyy-yyybbyyy-yyyyyyy-ybbbbby-yyyyyyy-ybby-yyyyyyy-ybbbbbyy-\n"
            "-yyyyyyyy-ybbyybby-yyyy-yyybbyyy-yyyyyyy-ybbybby-yyyyyyy-ybby-yyyyyyy-yyyybbyy-\n"
            "----------ybbbbbyy------yyybbyyy---------ybbybby---------ybby---------ybbbbbyy-\n"
            "--------yyyyyyyyyy----yyyyyyyyyy-------yyyyyyyyy-------yyyyyy-------yyyyyyyyyy-\n"
            "--------yyyyyyyyyy----yyyyyyyyyy-------yyyyyyyyy-------yyyyyy-------yyyyyyyyyy-",1)


        i = int(self.which_number)
        if i == 0:
            self.print_image(
                "-wwwwwww-wwwwwwwwwwwwwwwwwwwww-wwwwww-wwwwwww\n"
                "ww-----www-----ww-----ww-----www----www--w--w\n"
                "w--www--ww--wwwww--wwwww--wwwww--ww--ww--w--w\n"
                "w--wwwwwww----www----www----www------www---ww\n"
                "w--www--ww--wwwww--wwwww--www-w--ww--ww--w--w\n"
                "ww-----www-----ww-----ww--w---w--ww--ww--w--w\n"
                "-wwwwwww-wwwwwwwwwwwwwwwwww---wwwwwwwwwwwwwww\n"
                "---------------------------------------------",9,16)
            self.print_image(
                "--www-wwww-wwwwwwwww-----------wwwwwwwwwwww-wwwwwwwww-\n"
                "-ww-www---ww-----w-w-----------w----ww----www-ww----ww\n"
                "-w--ww--w--wwww--w-www--wwwwww-w-ww--w-ww--w--ww-ww--w\n"
                "-ww-www----www--ww-w-ww-w----w-www--ww-w-w-ww-wwww--ww\n"
                "-ww-wwww--www--www----w-wwwwww-ww--www--ww-ww-www--www\n"
                "-w---ww--www--ww-www-ww--------w-----ww----w---w-----w\n"
                "-wwwwwwwwwwwwww----www---------wwwwwwwwwwwwwwwwwwwwwww\n"
                "------------------------------------------------------",14,11)
            self.add_newline()
        else:
            self.move_cursor(y=10,x=2)
            if self.main is None:
                self.add_title(self.name[i],bg="BRIGHTWHITE",fg="BLACK",font="size4")
            else:
                self.add_title(self.main.name[i],bg="BRIGHTWHITE",fg="BLACK",font="size4")
            self.move_cursor(y=15,x=1)
            if self.main is None:
                self.add_text(self.description[i])
            else:
                self.add_text(self.main.description[i])
            self.move_cursor(y=16,x=20)
            if self.main is None:
                self.add_title("          "+self.birth[i]+" - "+self.death[i],bg="YELLOW",fg="BLACK",font="size4")
            else:
                self.add_title("          "+self.main.birth[i]+" - "+self.main.death[i],bg="YELLOW",fg="BLACK",font="size4")
            mouth_color = random.choice(['r','c','g','y','o','p'])
            self.print_image(
                "-wwwwwww-\n"
                "ww-----ww\n"
                "w--w-w--w\n"
                "w-------w\n"
                "w---" + mouth_color + "---w\n"
                "w-------w\n"
                "ww-w-w-ww\n"
                "w-w-w-w-w",17,1)


i_p1 = ObitPage("261",1)
i_p0 = ObitPage("260",0,i_p1)
i_p2 = ObitPage("262",2,i_p1)
i_p3 = ObitPage("263",3,i_p1)
i_p4 = ObitPage("264",4,i_p1)
i_p5 = ObitPage("265",5,i_p1)
i_p6 = ObitPage("266",6,i_p1)
i_p7 = ObitPage("267",7,i_p1)
i_p8 = ObitPage("268",8,i_p1)
i_p9 = ObitPage("269",9,i_p1)
i_pA = ObitPage("270",10,i_p1)
