# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 14:06:14 2022

@author: rahma
"""

from pywebio.input import input, input_group 
def getInfo():
    info = input_group("Info about citizen of UZB", [
        input("Name", name = "ism"),
        input("Lastname", name = "familiya",),
        input("Middlename", name = "otasi",),
        input("Birth-year", name = "tyil",),
        input("Birth-month", name = "toy",),
        input("Birth-day", name = "tkun",),
        input("Mobile number", name = "telefon",),
        input("Passport number", name = "pass_raqam",),
        input("Issued date", name = "pass_sana",),
        ],)
    return info

