# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 18:25:16 2021

@author: Asus
"""

## class inheritance

class member:
    num_of_member=0
    
    raise_amt=1.1
    
    reward_amount=0
    
    def __init__(self,name,session):
        self.name=name
        self.session=session
        self.email=self.name+"@gmail.com"
        self.pay=5000
        member.num_of_member+=1
        
    def display(self):
        print("name:",self.name,"\nsession:",self.session,"\nemail:",self.email,"\npay:",self.pay)
    
    def pay_raise(self):
        self.pay=self.pay * self.raise_amt
    
    def giveR(self):
        self.pay+=member.reward_amount
        
    @classmethod
    def giveReward(cls,amount):
        cls.reward_amount = amount
    
    @classmethod
    def resetReward(cls):
        cls.reward_amount = 0

##subclass deriving member class
        
class developer(member):
    raise_amt=1.2
    def __init__(self,prog_lang,project,**kwargs):
        self.prog_lang = prog_lang
        self.project=project
        super(developer,self).__init__(**kwargs)

class AIlead(member):
    def __init__(self,project,mems=None,**kwargs):
        self.project=project
        if mems is None:
            self.mems=[]
        else:
            self.mems=mems
        super(AIlead,self).__init__(**kwargs)

    def addDev(self,mem):
        for m in mem:
            if m not in self.mems:
                if m.project == self.project:
                    self.mems.append(m)
    
    def remDev(self,mem):
        for m in mem:
            if m in self.mems:
                self.mems.remove(m)
    def displayDevs(self):
        for m in self.mems:
            print(m.name)


##developers

dev1=developer('python','NLP',name='subrat',session=2020)
dev2=developer('python','NLP',name="ruchita",session=2020)
dev3=developer('java','Ai-GUI',name="chillu",session=2020)
dev4=developer('java','Ai-GUI',name="zafer",session=2020)

##managers

manager1=AIlead("NLP",name="eric",session=2020)
manager2=AIlead("Ai-GUI",name="hanson",session=2020)

##adding developers to managers

manager1.addDev([dev1,dev2,dev3,dev4])
manager2.addDev([dev1,dev2,dev3,dev4])
manager1.displayDevs()
manager2.displayDevs()

##removing developers from managers
manager1.remDev([dev1])
manager2.remDev([dev3])
manager1.displayDevs()
manager2.displayDevs()

##checking if an object is an instance of a class

print(isinstance(manager1,AIlead))
print(isinstance(manager1,member))
print(isinstance(manager1,developer))

##checking if a class is a subclass of a class 

print(issubclass(AIlead,AIlead))
print(issubclass(AIlead,member))
print(issubclass(AIlead,developer))





