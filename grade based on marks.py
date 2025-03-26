a=int(input('ENTER THE MARK OF SUB 1 :'))
b=int(input('ENTER THE MARK OF SUB 2 :'))
c=int(input('ENTER THE MARK OF SUB 3 :'))
avg=(a+b+c)/3
if (avg>=90):
    print('THE GRADE IS A')
elif (avg>=80 and avg<90):
    print('THE GRADE IS B')
elif (avg>=70 and avg<80):
    print('THE GRADE IS C')
elif (avg>=60 and avg<70):
    print('THE GRADE IS D')
else:
    print('FAIL')

