# here we will print the greatest number between 3 using function. 
def great(n1,n2,n3):
    if n1>n2:
        if n1>n3:
            print(n1,"is greatest.")
        else:
            print(n3,"is greatest")
    else:
        if n2>n3:
             print(n2,"is greatest.")
        else:
            print(n3,"is greatest")

num=int(input("Enter the number 1:"))
num1=int(input("Enter the number 2:"))
num2=int(input("Enter the number 3:"))

great(num,num1,num2)
