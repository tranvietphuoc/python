# All examples about generators in Python
# in Python, Generator functions allow you to declare a function\
# that behaves like # an iterator, i.e it can be used in a for loop
# -----------------------------------------
# Iterable objects is one that can create Iterators that can traverses or\
# loop through each element in Collections or Sequences\
# that supports either Iteration Protocol and Sequence Protocol
# So, what is Iterators?
'''
Iterators provide a way to access the elements of a Collection or Sequence
sequentially without exposing its underlying representation, in other words, 
it just returns each element of a collection sequentially, 
if the object has a __next__() method attached to it, it is an iterator
'''
# let's explore these examples
# for element in [1, 2, 3]:
#     print(element)
# for element in (1, 2, 3):
#     print(element)
# for key in {'one':1, 'two':2}:
#     print(key)
# for char in "123":
#     print(char)
# for line in open("myfile.txt"):
#     print(line, end='')

# Behind the scenes, for statement call iter() on container object
# the function return an iterator object that defines method __next__()
# which are accesses elements in the container one at a time. 
# when there are no more elements, __next__() raises a StopIteration exception
# which tells the for loop to terminate. 
# You can call __next__() by use built-in function next(). This's called iterator protocol ---> example:
s='abc'
it=iter(s) 
print(it) #will print  <str_iterator object at 0x105fd0850>
print(next(it)) #will print a
print(next(it)) #will print b
print(next(it)) #will print c
print(next(it)) #will raise StopIteration exception

########################
'''
Let's start to explore this example
>>>import dis
>>>list = [1,2,3,4,5]
>>>for each in list:
>>>    print(each)

>>>print(dis.dis('for each in list: print(each)')
1           0 SETUP_LOOP              20 (to 22)
              2 LOAD_NAME                0 (list)
              4 GET_ITER
        >>    6 FOR_ITER                12 (to 20)
              8 STORE_NAME               1 (each)
             10 LOAD_NAME                2 (print)
             12 LOAD_NAME                1 (each)
             14 CALL_FUNCTION            1
             16 POP_TOP
             18 JUMP_ABSOLUTE            6
        >>   20 POP_BLOCK
        >>   22 LOAD_CONST               0 (None)
             24 RETURN_VALUE
None

As can be seen in the disassembly of the Python code 
print(dis.dis('for each in list: print(each)'), the for statement 
makes a call GET_ITER method iter(each) thus creating an iterator
than can now be invoked FOR_ITER equivalent to next() and will return the results.
'''
#in Python, we can create an Iterable object by call two protocols, the fist
#is the Iteration (__iter__() method)), and the second is the Sequence
#(__getitem__())

#example about a iterator
class yrange:
     def __inti__(self,n):
          self.n=n
          self.i=0
     
     def __iter__(self):
          return self
     
     def __next__(self):
          if self.i<self.n:
               i=self.i
               self.i+=1
               return i
          else:
               raise StopIteration()


y=yrange(2)
y.__next__() #0
y.__next__() #1
y.__next__() #StopIteration error

# Iterator can traverse only once

# Generator is functions that use one or more 'yield' statement to return something
# whenever generator is called, it returns the generator object
# when __next__ method is called, generator will run still it meet a 'yield' statement
# example:
def integers:
     '''Infinite sequence of integers'''
     i=1
     while True:
          yield i
          i+=1

def squares():
     for i in integers():
          yield i*i

def take(n,seq):
     '''Return first n values from the given sequence'''
     seq=iter(seq)
     result=[]
     try:
          for i in range(n):
               result.append(seq.__next__())
     except StopIteration:
          pass
     return result
print(take(5,squares())) # will print [1,4,9,16,25]

## Generator expression
# generator expression just look like a list comprehension
# example:
a=(x**2 for i in range(3)) #will return a generator object
sum(a) #will print out the sum of 0,1,4
# example to find out Pythagoras use generator expression

pyt=((x,y,z) for z in integers() for y in range(1,z) for x in range(1,y) if x*x+y*y==z*z)
take(10,pyt)
## So why use generator?
# to make code is simple
#example: make a function to return n positive intergers
#using function - list
def firstn(n):
     num=0
     nums=[]
     while num<n:
          nums.append(num)
          num+=1
     return nums

# this function above will run generally, except it has a problem, it'll save all list in memory
# now we use an iterator
class firstn:
     def __init__(self,n):
          self.n=n
          self.num,self.nums=0,[]

     def __iter__(self):
          return self
     
     def __next__(self):
          if self.num<self.n:
               cur,self.num=self.num,self.num+1
               return cur
          else:
               raise StopIteration()
     
# it's too complex and gassy
# now we use generator
def firstn(n):
     num=0
     while num<n:
          yield num
          num+=1
#=====>ok done
#unless, generator can be used to optimize the performance
## Python produce a module name itertools to work with iterators




          
