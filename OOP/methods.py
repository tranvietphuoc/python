import Person
import datetime

#demonstrate about classmdethod and staticmethod of class
class Teacher(Person.Person):
    #class variable
    num_of_periods=40
    def __init__(self,first,last,birthday,title):
        super().__init__(first,last,birthday)
        self.title=title
    
    ## about classmethod
    @classmethod
    def get_tilte(self):
        pass




if __name__=='__main__':
    teacher1=Teacher('vo','son',datetime.datetime(1983,1,1),'Ph.D')
    print(teacher1.num_of_periods)   
    print(teacher1.get_tilte) 