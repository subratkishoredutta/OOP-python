# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 23:41:33 2021

@author: Asus
"""
##OOP python class variable: variables that area shared among the instances of a class
class member:
    num_of_member=0
    pay_increment=1.1
    
    def __init__(self,name,session):
        self.name=name
        self.session=session
        self.email= self.name+"@gmail.com"
        self.pay=5000
        member.num_of_member+=1
    
    def display(self):
        print("name:",self.name,"\nsession:",self.session,"\nemail",self.email,"\npay",self.pay)
    
    def pay_raise(self):
        self.pay = self.pay*self.pay_increment
        
mem=member('subrat',2020)
mem.display()
mem.pay_raise()
mem.display()

print("number of members: ",member.num_of_member)