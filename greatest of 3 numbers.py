a=int(input('enter n1 :' ))
b=int(input('enter n2 :'))
c=int(input('enter n3 :'))
if a>b and a>c:
    y=a
elif b>a and b>c:
    y=b
else :
    y=c
print('greatest number is',y)