# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 14:18:38 2022

@author: rahma
"""
from pywebio.output import put_file, put_html
from pywebio.session import hold
from frontend import getInfo 
from backend import fillDoc 
title = '<h1 style="text-align:center">Form for Uzbekistan citizen</h1>'
put_html(title)

userInfo = getInfo() 
filename = fillDoc(userInfo)
text = "<h3> Form is ready to download.</h3>"
put_html(text)

with open(filename, "rb") as file:
    form = file.read()
    put_file(filename, content=form)
    hold()


     
    
    
    