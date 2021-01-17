# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 12:03:49 2021

@author: Asus
"""
##classmethods
class member:
    num_of_mem=0 ## class variable
    
    pay_incre=1.1 ##class variable 
    
    reward_amount=0
    
    def __init__(self,name,session):
        self.name=name
        self.session=session
        self.email=self.name+"@gmail.com"
        self.pay=5000
        member.num_of_mem+=1
    
    def display(self):
        print("name:",self.name,"\nsession:",self.session,"\nemail:",self.email,"\npay:",self.pay)
    
    def raise_pay(self):
        self.pay=self.pay*self.pay_incre
    
    def give(self):
            self.pay = self.pay + member.reward_amount

            
    @classmethod
    def giveReward(cls, amount):
        cls.reward_amount = amount
    
    @classmethod
    def release_reward(cls):
        cls.reward_amount=0
    
    ##class methods as constructors
    @classmethod
    def toarg(cls,string):
        name,session=string.split('-')
        return cls(name,session)

mem1=member('subrat',2020)   
mem2=member('ruchita',2020)
mem1.display()    
mem2.display()
 
member.giveReward(1000)
mem1.give()
mem2.give()
member.release_reward()
mem1.display()
mem2.display()

member3="subrata-2020"
mem3=member.toarg(member3)
mem3.display()

