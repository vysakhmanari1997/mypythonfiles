def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def division(x,y):
    if y!=0:
        return x/y
    else:
        return 'not defined'
c=input('ENTER THE OPERATION TO PERFORM :')
a=int(input('ENTER FIRST NUMBER :'))
b=int(input('ENTER THE SECOND NUMBER :'))
if c=='add':
    print(f" {a} + {b} = {add(a,b)}")
elif c=='subtract':
    print(f" {a} - {b} = {subtract(a, b)}")
elif c=='multiply':
    print(f" {a} * {b} = {multiply(a, b)}")
elif c=='division':
    print(f" {a} / {b} = {division(a, b)}")
else:
    print('INVALID NUMBER')






