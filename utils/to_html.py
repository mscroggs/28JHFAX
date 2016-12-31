#!/usr/bin/env python
import sys
sys.path.insert(0,'..')

# width:79
# height: 30

from os import listdir
from os.path import isfile
import os
from page import PageManger, Page
from colours import terminal_to_html
from name import NAME

def is_page_file(f):
    if "_" in f:
        return False
    if "pyc" in f:
        return False
    return True


pages_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), "../pages")
only_page_files = [f for f in listdir(pages_dir)
                   if isfile(os.path.join(pages_dir, f)) and is_page_file(f)]

page_manager = PageManager()

for page_file in only_page_files:
    page_file_no_ext = str(os.path.splitext(page_file)[0])
    module = getattr(__import__("pages", fromlist=[page_file_no_ext]),
                     page_file_no_ext)
    reload(module)
    for object in dir(module):
        obj = getattr(module, object)
        if isinstance(obj, Page):
            try:
                page_manager.add(obj)
            except:
                pass

html_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), "../html")

items = page_manager.pages.items()
items.sort()
taglines = "taglines = {"
pages_on = "pages_on = Array("
t_next = ""
p_next = ""
for page_num, page in items:
    try:
        page.generate_content()
        cont = page.content.encode('ascii', 'xmlcharrefreplace')
        cont = "&nbsp;".join(cont.split(" "))
        cont = "<br />".join(cont.split("\n"))
        for term,html in terminal_to_html.items():
            cont = html.join(cont.split(term))
        cont = cont.split("\033[0m")
        while len(cont)>1:
            spans = len(cont[0].split("<span"))-len(cont[0].split("</span>"))
            cont = [cont[0]+"</span>"*spans+cont[1]] + cont[2:]
        cont = cont[0]
        with open(os.path.join(html_dir,page_num+".html"),"w") as f:
            f.write(cont)
        if page.is_enabled:
            pages_on += p_next + '"'+page_num+'"'
            p_next = ","
        if page.tagline != NAME + ": The World at Your Fingertips":
            taglines += t_next +'"'+page_num+'":"'+page.tagline+'"'
            t_next = ","
        print page_num
    except BaseException as e:
        print page_num,e

taglines += "}"
pages_on += ")"

print os.path.join(html_dir,"info.js")
with open(os.path.join(html_dir,"info.js"),"w") as f:
    f.write(taglines+"\n"+pages_on)
