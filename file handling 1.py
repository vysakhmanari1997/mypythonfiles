def student_details():
    print('enter the operation to perform')
    y = input('read,write,delete :')
    if y == 'write':
        name = input('ENTER THE NAME :')
        age = input('ENTER THE AGE :')
        grade = input('ENTER THE GRADE :')
        a = name + age + grade
        f = open(name, "w")
        f.write(a)
        f.close()
    elif y=='read':
        import os
        c = input("ENTER THE FILE TO OPEN :")
        if  os.path.exists(c):
            f = open(c, "r")
            print(f.read())
        else:
            print('THE FILE DOES NOT EXIST')
    elif y=='delete':
        b = input("ENTER THE FILE NAME TO DELETE :")
        import os
        if os.path.exists(b):
            os.remove(b)
        else:
            print("THE FILE DOES NOT EXIST")
student_details()






