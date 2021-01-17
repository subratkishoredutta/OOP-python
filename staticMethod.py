# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 14:20:10 2021

@author: Asus
"""

##static methods: it donot take in any instances or the class itself as a argument

class member:
    @staticmethod
    def isWorkday(day):
        if (day.weekday()==5 or day.weekday()==6):
            return False
        return True

import datetime

day=datetime.date(2021,5,1)

print(member.isWorkday(day))