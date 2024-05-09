#Write an python program to print the number one to five using recursion
def onetofive(x):#Own
    if x<6:
        print(x)
        x+=1
        onetofive(x)
    else:
        print("Execution completed")

#onetofive(1)

def printx(x):
    if x==0:#Clg given
        return
    printx(x-1)
    print(x)

#printx(5)

#Write an python program to sum the number from 1 to 5 using recursion
def sumof(s):#Clg given
    if s==0:
        return 0
    return s+sumof(s-1)

#print(sumof(5))

def s(x):#Own

    if x==5:
        return 5
    return x+s(x+1)

#print(s(0))

#Write an python program to find the factorial of a given number using recursion
def recursion(s):
    if s==0:
        return 1
    return s*recursion(s-1)

print(recursion(5))

#