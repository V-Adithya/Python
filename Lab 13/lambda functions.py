#Simple lambda function
'''a=lambda s:s*2
print(a(20))'''

#User defined python function to add two numbers using a lambda function
def add(s):
    return lambda a:a+s
v=add(20)
print(v(50))