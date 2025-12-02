# 2. Person Class with Age Calculation
# Write a Python program to create a person class. 
# Include attributes like name, country and date of birth. 
# Implement a method to determine the person's age.
from datetime import date

class Person:
    def __init__(self, name, country, DoB):
        self.name = name
        self.country = country
        self.DoB = DoB
    def getName():
        return self.name
    def getCountry():
        return self.country
    def getDoB():
        return self.DoB
    def getAge():
        x = date.today()
        age = x - self.DoB.year
        if today < date(today.year, self.DoB.month, self.DoB.day):
            age -= 1
        return age
    

        