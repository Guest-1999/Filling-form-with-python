# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 13:51:39 2022

@author: rahma
"""

from docxtpl import DocxTemplate


def fillDoc(info, file = "anketa.docx"):
    form = DocxTemplate("anketa.docx")
    form.render(info)
    filename = f"{info['familiya']}_anketa.docx"
    form.save("filename")
    return filename

