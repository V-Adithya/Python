import random

#The above code as a parameterized code
def user_input():
    x=int(input("Enter x:"))
    y=int(input("Enter y:"))
    return x,y

#A function to create a list of size n
def list():
    list=[]
    x=int(input("Enter list size:"))
    for i in range(x):
        list.append(int(input("Enter a value:")))
    return list

#A function to add two numbers
def add(a,b):
    return a+b

#A function to find the minimum numbers in a list
def minimum(list):
    minimum=list[0]
    for element in list:
        if minimum>element:
            minimum=element
    return minimum

#A function to find the maximum numbers in a list
def maximum(list):
    maximum=list[0]
    for element in list:
        if maximum<element:
            maximum=element
    return maximum

#A function to find the second maximum element in a list
def second_maximum(list):
    mainmaximum=maximum(list)
    second_maximum=list[0]
    for element in list:
        if second_maximum<element and element<mainmaximum:
            second_maximum=element
    return second_maximum

#A function to find the second minimum element in a list
def second_minimum(list):
    mainminimum=minimum(list)
    length=len(list)
    second_minimum=random.choice(list)
    for element in list:
        if second_minimum>element and element>mainminimum:
            second_minimum=element
    return second_minimum

#x,y=user_input() #Takes the user input(2 values)
#print("The sum of ",x,"and",y,"is:",add(x,y))#Prints the sum of the above variables
list=list()#Creates a list and adds elements to the list
#print("Minimum element in the list is:",minimum(list))#Finds the maximum element in the list
#print("Maximum element in the list is:",maximum(list))#Find the minimum element in the list
#print("Second maximum element in the list is:",second_maximum(list))#Find the second maximum element in the list
#print("Second minimum element in the list is:",second_minimum(list))#Find the second minimum element in the list