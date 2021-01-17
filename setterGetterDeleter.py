# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 23:08:31 2021

@author: Asus
"""
##getter,setter,deleter

class member:
    def __init__(self,first,second):
        self.first=first
        self.second=second
    @property
    def email(self):##sets the email without flaw when first and second name are altered
        return(self.first+self.second+"@gmail.com")
        
    @property
    def fullname(self):
        print(self.first+" "+self.second)
        
    @fullname.setter
    def fullname(self,full):
        self.name,self.second=full.split(' ')
        
    @property
    def delete(self):
        pass
    
    @delete.deleter
    def delete(self):
        print('DELETING INFO!!')
        self.first=self.second=None
        
    def display(self):
        print("name:",self.first+" "+self.second,"\nemail:",self.email)
        
mem1=member('si','k')
mem1.display()

mem1.first="subrat"
mem1.display()

mem1.fullname

mem1.fullname="subrat kishore"
mem1.display()

del mem1.delete


