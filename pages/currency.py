#!/usr/bin/env python
# -*- coding: utf-8 -*-
from ceefax.page import Page
from ceefax import config

class CurrencyPage(Page):
    def __init__(self, page_num, c1, c2):
        global pagelist
        super(CurrencyPage, self).__init__(page_num)
        url = "http://"+c1[0].lower()+".fxexchangerate.com/"+c2[0].lower()+".xml"
        self.importance = 1
        self.top_title = c1[0]+" vs "+c2[0]
        self.title = c1[3]+" vs "+c2[3]
        pagelist[page_num] = (c1,c2)
        self.url = url
        self.in_index = False
        self.tagline = "From fxexchangerate.com"
        self.c1 = c1
        self.c2 = c2

    def background(self):
        if self.c1[0] != self.c2[0]:
            import feedparser
            rss_url = self.url
            feed = feedparser.parse(rss_url)
            s = feed["entries"][0]["summary"]
            self.a = s.split("<br")[0].split("=")[1]
            while self.a[0] == " ":
                self.a = self.a[1:]
            self.a = self.a.split(" ")[0]
            self.b = s.split("<br")[1].split("=")[1]
            while self.b[0] == " ":
                self.b = self.b[1:]
            self.b = self.b.split(" ")[0]

            import fix_yahoo_finance as yf
            from dateutil.relativedelta import relativedelta
            this_time_last_year = (config.now() - relativedelta(years=1,days=1)).strftime("%Y-%m-%d")
            yesterday = (config.now() - relativedelta(days=1)).strftime("%Y-%m-%d")
            data = yf.download(self.c1[0].upper() + self.c2[0].upper() + "=X", start=this_time_last_year, end=yesterday,progress=False)
            data_as_list = data.to_records()
            self.xs = []
            self.ys = []
            for d in data_as_list:
                self.xs.append(d[0])
                self.ys.append(d[1])
            #from IPython import embed
            #embed()

        else:
            from dateutil.relativedelta import relativedelta
            this_time_last_year = (config.now() - relativedelta(years=1,days=1)).strftime("%Y-%m-%d")
            yesterday = (config.now() - relativedelta(days=1)).strftime("%Y-%m-%d")
            self.a = "1"
            self.b = "1"
            self.xs = [this_time_last_year,yesterday]
            self.ys = [1,1]

    def generate_content(self):
        self.add_title(self.top_title,bg="BLACK",fg="RED",font='size4')
        self.add_title(self.c1[1]+"1"+self.c1[2]+" = "+self.c2[1]+self.a+self.c2[2],font='size4',fg="BLACK",bg="YELLOW")
        self.add_title(self.c2[1]+"1"+self.c2[2]+" = "+self.c1[1]+self.b+self.c1[2],font='size4',fg="BLACK",bg="LIGHTBLUE")
        self.plot(range(len(self.ys)),self.ys,14,0,width=80,height=13,ytitle=self.c2[0],xtitle="Date",xlabels=[(i,self.xs[i].strftime('%-d-%b-%y')) for i in range(0,len(self.ys),53)],point=None,line="y")


class IndexPage(Page):
    def __init__(self, page_num, pagelist):
        super(IndexPage, self).__init__(page_num)
        self.pagelist = pagelist
        self.importance = 1
        self.title = "Money"

    def generate_content(self):
        self.add_title("Currencies",bg="BLACK",fg="LIGHTRED",font='size4bold')
        c1 = None
        x = 0
        y = 7
        self.add_text("341",fg="RED")
        self.add_text(" Bitcoin")
        self.add_newline()
        self.add_text("342",fg="RED")
        self.add_text(" Bitcoin vs USD")
        self.add_newline()
        self.add_text("343",fg="RED")
        self.add_text(" Bitcoin vs GBP")
        self.add_newline()
        self.add_text("344",fg="RED")
        self.add_text(" Bitcoin vs EUR")
        for i,page in enumerate(sorted(self.pagelist.items())):
            #from IPython import embed
            #embed()
            d = self.pagelist[page[0]]

            if c1 != d[0][3]:
                c1 = d[0][3]
                y += 1
                if y>25:
                    y = 4
                    x += 28
                self.move_cursor(x=x,y=y)
                self.add_text(c1,fg="YELLOW")
            y += 1
            if y>26:
                y = 4
                x += 28
            self.move_cursor(x=x,y=y)
            self.add_text(str(page[0]),fg="RED")
            self.add_text(" vs "+d[1][3])

currencies = [
        ("GBP",u"£","","British Pound"),
        ("EUR",u"€","","Euro"),
        ("USD",u"$","","US Dollar"),
        ("NZD",u"NZ$","","New Zealand Dollar"),
        ("AUD",u"AU$","","Australian Dollar"),
        ("JPY",u"¥","","Japanese Yen"),
        ("NOK",u"",u"kr","Norwegian Krone"),
        ("VND",u"₫","","Vietnam Dong"),
        ("RUB",u"",u"₽","Russian Rouble"),
        ("CHF",u"Fr","","Swiss Franc"),
        ("GBP",u"SCOT£","","Scottish Pound")
    ]

pagelist = {}
pages = []
pn = 345
for i,a in enumerate(currencies):
    for b in currencies[i+1:]:
        pages.append(CurrencyPage(pn,a,b))
        pn += 1

index = IndexPage(340, pagelist)
index.index_num = "340-399"
