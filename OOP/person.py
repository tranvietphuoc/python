import datetime
import json

## class definition, inheritance and instantiate
## make a class Person

class Person:
    # constructor
    def __init__(self,first,last,birthday):
        self.first=first
        self.last=last
        self.birthday=birthday # with datetime format
        self.email=first+'.'+last+'@email.com'
    # get full name
    def fullname(self):
        return '{} {}'.format(self.first,self.last)
    ## make a function to calculate the age
    def age(self):
        # use the comparison mechanism between 2 tuples
        today=datetime.date.today() #today
        return today.year-self.birthday.year-((today.month,today.day)<(self.birthday.month,self.birthday.day))
        

## make a class Student inherit from class Person
class Student(Person):
    # constructor
    def __init__(self,first,last,birthday,university,gpa):
        super().__init__(first,last,birthday) #inherit from Person's constructor
        # can use this syntax:
        # Person.__init__(self,first,last,birthday)
        self.university=university
        self.gpa=gpa
    # get the information of a student in json format
    def get_info(self):
        return json.dumps({
            'name': self.fullname(),
            'birthday': str(self.birthday), #convert datetime format to string
            'age': self.age(),
            'email': self.email,
            'University': self.university,
            'GPA': self.gpa
        })

if __name__=='__main__':
    ## create an instantiation
    stu1=Student('Tran','Phuoc',datetime.datetime(1993,10,10),'HCMC University of Technology',3.6)
    print(stu1.get_info())
    #get age 
    print(stu1.age())
