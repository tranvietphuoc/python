#this part mention about instance method, class method and static method

import person
import datetime
import json

# demonstrate about instance method, class method and static method 
class Teacher(person.Person):
    # class variable
    num_of_periods=40 #periods per week
    seniority=20      #years
    def __init__(self,first,last,birthday,title):
        super().__init__(first,last,birthday) #inheritance
        self.title=title

    # instance method
    def set_title(self,title):  # just effect to instances, first argument is self --> instances
        self.title=title


    def get_title(self): 
        return 'title: {}'.format(self.title)


    # classmethod
    @classmethod
    def set_periods(cls,num_of_pds):  # the first argument is cls ---> effect to all class, not instances
        cls.num_of_periods=num_of_pds 
    
    #class method
    #build a new instance from string
    # day with string format yyyy/mm/dd
    @classmethod
    def from_string(cls,str1):
        first,last,birthday,title=str1.split('-')
        y,m,d=list(map(int,birthday.split('/')))
        return cls(first,last,datetime.datetime(y,m,d),title)
    
    # static method
    @staticmethod
    def is_seniority(seniority):   # just act like a normal function, does not have cls or self argument
        return True if seniority>=10 else False
    
    #get instances's information
    def get_inf(self):
        return json.dumps({
            'Name': self.first+self.last,
            'Birthday': str(self.birthday),
            'Email': self.email,
            'Title': self.title
        })


if __name__=='__main__':
    teacher1=Teacher('Vo','Son',datetime.datetime(1983,1,1),'Ph.D')
    teacher2=Teacher('Cuong','Tran',datetime.datetime(1974,2,3),'Engineer')
    Teacher.num_of_periods=30
    # print(teacher1.num_of_periods) # change the class variable directly
    # print(teacher2.num_of_periods)
    # # print(teacher1.num_of_periods)   
    # # print(teacher2.get_title()) 
    # # print(teacher1.set_periods(50)) # change class variable
    # # print(teacher1.num_of_periods)
    # # print(teacher2.num_of_periods)
    # print(teacher1.set_title)
    # print(teacher2.set_title)
    # print(teacher1.set_periods) #bound method of class
    # print(teacher2.set_periods) #bound method of class
    # print(teacher1.set_seniority) #function
    # print(teacher2.set_seniority) #function
    # print(Teacher.__dict__)
    # take info from string
    str1='Ninh-Tran-1974/2/9-Professor'
    new_teacher=Teacher.from_string(str1)
    print(new_teacher)
    print(new_teacher.get_inf())
    ## static method example
    print(Teacher.is_seniority(5))
    print(Teacher.is_seniority(10))