# all examples about decorator
# a decorator is a function wraps another function and change the behavior of that function
# let's start
# ===> Part 1: the base of theory
# a function can be assigned to a variable
def talk(): 
    return "aaa".upper()+"!"

scream=talk
print(scream == talk) #print True
print(scream()) #print "AAA"
# a function can become a parameter of another function
def whisper(func):
    return func.lower()+"..."

print(whisper(talk())) #will print aaa!...
# ---> functions in Python is first-class objects: can be assigned, passed as argument, defined inside another functions,...
# nested functions
def shout():
    def laugh():
        return "hahaha".upper()+"!"
    return laugh

print(shout()()) #will print HAHAHA!

# ====> Part 2: now we explore the decorator
# define a function like this, we'll decorate another function manualy
def p_decor(func):
    def wrapper(name):
        return "<p>{}</p>".format(func(name))
    return wrapper
# there is function which we want to decorate
def get_text(name):
    return "lorem ipsum dolor sit amet...{}".format(name)

get_text=p_decor(get_text) #get_text function is decorated
print(get_text("phuoc")) #this will print "<p>lorem ipsum dolor sit amet...phuoc</p>"

# => ok, let begin with decorator syntax in Python
def p_decor(func):
    def wrapper(name):
        return "<p>{}</p>".format(func(name))
    return wrapper

@p_decor
def get_text(name): #note: get_text's argument will pass to wrapper function
    return "lorem ipsum dolor sit amet...{}".format(name)

# this equivalent to get_text=p_decor(get_text)
print(get_text("phuoc")) # this will print "<p>lorem ipsum dolor sit amet...phuoc</p>"

# => decorator can be associated with lambda like this
def p_decor(func):
    return lambda name: "<p>{}</p>".format(func(name))

@p_decor
def get_text(name):
    return "lorem ipsum dolo sit amet...{}".format(name)

print(get_text("phuoc")) #will print <p>lorem ipsum dolor sit amet...phuoc</p>

# => because decorator is a function, so it can be decorated by another decorator, example

def p_decor(func):
    return lambda name: "<p>{}</p>".format(func(name))

def strong_decor(func):
    return lambda name: "<strong>{}</strong>".format(func(name))

def div_decor(func):
    return lambda name: "<div>{}</div>".format(func(name))
@div_decor
@strong_decor
@p_decor
def get_text(name):
    return "lorem ipsum dolor sit amet...{}".format(name)

print(get_text("phuoc")) #will print <div><strong><p>lorem ipsum dolor sit amet...phuoc</p></strong></div>

# => methods of classes can be decorated
def p_decor(func):
    def wrapper(self): #wrapper's argument is self
        return "<p>{}</p>".format(func(self))
    return wrapper
    #or use lambda like this
    # return lambda self: "<p>{}</p>".format(func(self))

class Person:
    def __init__(self,first,last):
        self.first=first
        self.last=last
    
    @p_decor
    def get_fullname(self):
        return self.first+" "+self.last
    
per1=Person("tran","phuoc")
print(per1.get_fullname()) #will print <p>tran phuoc</p>

# ===> Part 3: decorator advanced
# A much better approach would be to make our decorator useful for functions and methods alike.
# By putting args and *kargs as parameter of wrapper

def p_decor(func):
    # def wrapper(*args,**kargs):
    #     return "<p>{}</p>".format(func(*args,**kargs))
    # return wrapper
    return lambda *args,**kargs: "<p>{}</p>".format(func(*args,**kargs)) #wrapper - lambda version

@p_decor
def get_name(first,last):
    return "My name: {} {}".format(first,last)

print(get_name("phuoc","tran")) #will print <p>My name: phuoc tran</p>

#how about class?
class Person:
    def __init__(self,first,last):
        self.first=first
        self.last=last
    
    @p_decor
    def get_fullname(self):
        return "My name: {} {}".format(self.first,self.last)

per1=Person("phuoc","tran")
print(per1.get_fullname())  #will print <p>My name: phuoc tran</p>

#=> we can passing argument to decorators too

def tags(tagname):
    def tags_decor(func):
        return lambda *args,**kargs: "<{0}>{1}</{0}>".format(tagname,func(*args,**kargs)) #notice here
    return tags_decor

@tags("p")
def get_text(name):
    return "lorem ipsum dolor sit amet...{}".format(name)

print(get_text("phuoc")) #will print <p>lorem ipsum dolor sit amet...phuoc</p>

@tags("strong")
def get_text(name):
    return "lorem ipsum dolor sit amet...{}".format(name)

print(get_text("phuoc")) #will print <strong>lorem ipsum dolor sit amet...phuoc</strong>

@tags("div")
def get_text(name):
    return "lorem ipsum dolor sit amet...{}".format(name)

print(get_text("phuoc")) #will print <div>lorem ipsum dolor sit amet...phuoc</div>

print(get_text.__name__) #will print lambda, what's wrong? we expected __name__ is get_text.
# because the attributes of get_text (__name__,__doc__,__module__) is overidden by wrapper function

# **** Python has functools module (from Python 2.5) to handle above problem
# example:
import functools

def tags(tagname):
    def tags_decor(func):
        @functools.wraps(func) #we will insert @functools.wraps(..) here
        def wrapper(*args,**kargs):
            return "<{0}>{1}</{0}>".format(tagname,func(*args,**kargs)) #notice here
        return wrapper
    return tags_decor

@tags("p")
def get_text(name):
    return "lorem ipsum dolor sit amet...{}".format(name)

print(get_text.__name__) #will print get_text here
print(get_text.__doc__) #will print None here
print(get_text.__module__) #will print __main__ here