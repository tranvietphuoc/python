import person
import datetime

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
    
    # static method
    @staticmethod
    def set_seniority():   # just act like a normal function, does not have cls argument
        pass



if __name__=='__main__':
    teacher1=Teacher('Vo','Son',datetime.datetime(1983,1,1),'Ph.D')
    teacher2=Teacher('Cuong','Tran',datetime.datetime(1974,2,3),'Engineer')
    Teacher.num_of_periods=30
    print(teacher1.num_of_periods) # change the class variable directly
    print(teacher2.num_of_periods)
    # print(teacher1.num_of_periods)   
    # print(teacher2.get_title()) 
    # print(teacher1.set_periods(50)) # change class variable
    # print(teacher1.num_of_periods)
    # print(teacher2.num_of_periods)
    print(teacher1.set_title)
    print(teacher2.set_title)
    print(teacher1.set_periods) #bound method of class
    print(teacher2.set_periods) #bound method of class
    print(teacher1.set_seniority) #function
    print(teacher2.set_seniority) #function
    print(Teacher.__dict__)