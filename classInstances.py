# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 22:20:53 2021

@author: subrat
"""
##OOP python class and instances
class member:
    def __init__(self, first,second,session):
        self.first=first
        self.second=second
        self.session=session
        self.email=first + second + "@gmail.com"

    def display(self):
        print ("name:",self.first+" "+self.second,"\nsession:",self.session)
    
    
one=member('subrat','kishore',2020)
second=member('ruchita','somani',2020)

one.display()
second.display()














