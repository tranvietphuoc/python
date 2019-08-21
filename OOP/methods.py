import Person
import datetime

#demonstrate about classmdethod and staticmethod of class
class Teacher(Person.Person):
    #class variable
    num_of_periods=40
    def __init__(self,first,last,birthday,title):
        super().__init__(first,last,birthday)
        self.title=title
    
    def get_title(self):
        return 'title: {}'.format(self.title)
    ## about classmethod
    @classmethod
    def set_periods(cls,num_of_pds):
        cls.num_of_periods=num_of_pds 




if __name__=='__main__':
    teacher1=Teacher('Vo','Son',datetime.datetime(1983,1,1),'Ph.D')
    print(teacher1.num_of_periods)   
    print(teacher1.get_title()) 
    print(teacher1.set_periods)