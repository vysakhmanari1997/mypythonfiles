a=int(input('ENTER a NUMBER:'))
b=int(input('ENTER A NUMBER:'))
print('ENTER THE OPERATION TO PERFORM')
y=input('+,-,*,/:')
if y=='+':
    c= a+b
elif y=='-':
    c= a-b
elif y=='*':
    c= a*b
elif y=='/':
    c= a/b
else:
    print("UNRECOGNIZED SYMBOL")
print(a,y,b,":",c)
