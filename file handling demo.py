def student_details():
    print('enter the operation to perform')
    y=input('read,write,delete')
    while y=='write':
        name=input('enter the name')
        age=input('enter the age')
        grade=input('enter the grade')
        a=name+age+grade
        f=open(name,"w")
        f.write(a)
        f.close()
        break
    elif y=='read':
        c=input('enter the file name to open')
        f=open(c,"r")
        print(f.read())
    elif y=='delete':
        b=input('enter the file name to delete')
        import os
        os.remove(b)
student_details()












