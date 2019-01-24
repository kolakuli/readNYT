# -*- coding: utf-8 -*-
"""
Created on Wed May  9 16:07:17 2018

@author: HBui
@ Reading NYT Articles
"""
import re 
import requests


def readNews(link):
    f = requests.get(link)
    myfile = f.text
    mylist = re.split('>|< |\*|\n',myfile)
    
    foobar = []
    for i in mylist:
            foobar.append(i)
    
    foofoo = []
    for i in foobar:
        if '</p' in i and len(i)>20:
            foofoo.append(i)
            
    foo = []
    for i in foofoo:
        temp = re.split(r'<',i)
        for j in temp:
            if len(j) > 10:
                foo.append(j)
    return foo

link = "https://www.nytimes.com"
print(readNews(link))