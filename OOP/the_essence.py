# this part will explain how instance method, class method and static method work
import teacher
import person
import datetime
## to see the essence of the instance method, class method and static method

if __name__=='__main__':
    #create 2 instances of Teacher class
    teach1=teacher.Teacher('Vo','Son',datetime.datetime(1983,1,1),'Ph.D')
    teach2=teacher.Teacher('Cuong','Luu',datetime.datetime(1976,3,4),'Engineer')
    # print __dict__ of Teacher class
    print(teacher.Teacher.__dict__)
    # OK, let's start the survey
    # methods are functions which are bound to object
    print(teach1.get_title) ## call an instance method of class Teacher
    # the command above is equivalent with this
    print(teacher.Teacher.__dict__['get_title'].__get__(teach1,teacher.Teacher)) # take 2 parameter, instance and class
    '''
    Because Python can refer to all methods by using __dict__, it has a special object, which is advantage to "bind"
    objects call "descriptor",include:
    __get__
    __set__
    __delete__
    in this case, Python use __get__ method to demonstrate instance methods, class methods, static methods
    '''
    # then call class method
    print(teach2.set_periods)
    # equivalent to
    print(teacher.Teacher.__dict__['set_periods'].__get__(None,teacher.Teacher))
    # then static method
    print(teach1.is_seniority)
    # equivalent to 
    print(teacher.Teacher.__dict__['is_seniority'].__get__(teach1,None))

    


