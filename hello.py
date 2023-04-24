#Given a nested turple,write a python program to print the value of

def tuple_values():
    tuple = ("fruits",[100,234,565])
    print(tuple[1][1])

#Write a python program to unpack the following tuple into four variables and 
#display each variable
def tuples():
    tuple1 = (400,67,657,643)
    #assign values
    r,y,p,b = tuple1
    print(r)
    print(y)
    print(p)
    print(b)
#Write a program to copy elements 64 and 56 from the following turple into a new 
#turple
tuple1 =(39,575,64,78,795,56)
def copy_elements(*elements):
    new_tuple = (elements)
    print(new_tuple)
    copy_elements(64,56)

#Write a program to modify the first item (22) of a list inside a 
# following tuple to 222

def num_modify():
   tuple1 = (45, 45, 45, 45)
   result=  tuple1 == tuple1
   print(result)
        