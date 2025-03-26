n=int(input('ENTER THE NUMBER :'))
for x in n:
    if (x==0):
        print(x)
    elif (x<0):
        print('ENTER VALID NUMBER')
    elif (x==1)or(x==2):
        print('1')
    else:
        x(n - 1) + x(n - 2)
print(x(n))


