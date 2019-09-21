# this part will explain how instance method, class method and static method work

import datetime
## to see the essence of the instance method, class method and static method


class Person:
    # constructor
    def __init__(self, first, last, birthday):
        self.first = first
        self.last = last
        self.birthday = birthday  # with datetime format
        self.email = first+'.'+last+'@email.com'
    # get full name

    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    ## make a function to calculate the age

    def age(self):
        # use the comparison mechanism between 2 tuples
        today = datetime.date.today()  # today
        return today.year-self.birthday.year-((today.month, today.day) < (self.birthday.month, self.birthday.day))


class Teacher(Person):
    # class variable - class attribute
    num_of_periods = 40  # periods per week
    seniority = 20      # years

    def __init__(self, first, last, birthday, title):
        super().__init__(first, last, birthday)  # inheritance
        self.title = title

    # instance method
    def set_title(self, title):  # just effect to instances, first argument is self --> instances
        self.title = title

    def get_title(self):
        return 'title: {}'.format(self.title)

    # classmethod
    @classmethod
    # the first argument is cls ---> effect to all class, not instances
    def set_periods(cls, num_of_pds):
        cls.num_of_periods = num_of_pds

    #class method
    #build a new instance from string
    # day with string format yyyy/mm/dd
    @classmethod
    def from_string(cls, str1):
        first, last, birthday, title = str1.split('-')
        y, m, d = list(map(int, birthday.split('/')))
        return cls(first, last, datetime.datetime(y, m, d), title)

    # static method
    @staticmethod
    # just act like a normal function, does not have cls or self argument
    def is_seniority(seniority):
        return True if seniority >= 10 else False

    #get instances's information
    def get_inf(self):
        return json.dumps({
            'Name': self.first+self.last,
            'Birthday': str(self.birthday),
            'Email': self.email,
            'Title': self.title
        })


if __name__=='__main__':
    #create 2 instances of Teacher class
    teach1=Teacher('Vo','Son',datetime.datetime(1983,1,1),'Ph.D')
    teach2=Teacher('Cuong','Luu',datetime.datetime(1976,3,4),'Engineer')
    # print __dict__ of Teacher class
    print(Teacher.__dict__)
    # OK, let's start the survey
    # methods are functions which are bound to object
    print(teach1.get_title) ## call an instance method of class Teacher
    # the command above is equivalent with this
    print(Teacher.__dict__['get_title'].__get__(teach1,Teacher)) # take 2 parameter, instance and class
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
    print(Teacher.__dict__['set_periods'].__get__(None,Teacher))
    # then static method
    print(teach1.is_seniority)
    # equivalent to 
    print(Teacher.__dict__['is_seniority'].__get__(teach1,None))

    


