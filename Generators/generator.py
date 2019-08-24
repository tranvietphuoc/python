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

