########
# there are some special methods of class
# which are formed: __a_name()__ --> methods, which are surrounded by double __
# let's start
import person
import datetime

class Employee(person.Person):
    def __init__(self,first,last,birthday,salary):
        super().__init__(first,last,birthday)
        self.salary=salary
    
    #now we start learn about special method
    # __repr__(), __str__() are special methods
    #representation of instances
    def __repr__(self):
        return "Employee('{}','{}',{})".format(self.first,self.last,self.salary)
    #string for end user
    def __str__(self):
        return '{}, {}'.format(self.fullname(),self.email)
    # add salary
    # overloading operator +
    def __add__(self,other):
        return self.salary+other.salary



if __name__=='__main__':
    emp1=Employee('Tran','Phuoc',datetime.datetime(1993,10,10),2000)
    emp2=Employee('Van','Linh',datetime.datetime(1993,5,15),3000)
    print(emp1)
    print(repr(emp1))
    ## overloading + operator
    print("sum of salary: {}".format(emp1+emp2))