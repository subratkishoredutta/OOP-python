# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 17:44:25 2021

@author: Asus
"""

##magic function

#Call function:
class test:
    def add(self,inputs):
        return (2+inputs)
    def __call__(self,inputs):##__call__ function
        h=self.add(inputs)
        return h

one=test()(1)##called the __call__ function

class member:
    def __repr__(self):##used for debugging
        return ("member({},{})".format(self.first,self.last))
    
    def __str__(self):##used for representation
        return("object of member class ")
    
    def __add__(self,other):##used by default to add the given object's specific attributes
        return (self.pay + other.pay)
    
    def __len__(self):
        return (len(self.fullname))
    
    def __init__(self,first,last):
        self.first=first
        self.last=last
        self.pay=5000
    
   
    
    @property
    def email(self):
        return (self.first+self.last+"@gmail.com")
    @property
    def fullname(self):
        return (self.first+" "+self.last)
    @fullname.setter
    def fullname(self,inputs):
        self.first,self.last=inputs.split(' ')
    
mem1=member('subrat','dutta')
mem2=member('ruchita','somani')
print(mem1.__repr__())
print(mem1.__str__())
print(mem1+mem2)