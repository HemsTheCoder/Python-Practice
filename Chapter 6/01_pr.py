# here we will find the greatest of four number entered by the user.
a=int(input("Please enter 1st number: "))
b=int(input("Please enter 2nd number: "))
c=int(input("Please enter 3rd number: "))
d=int(input("Please enter 4th number: "))

if a>b:
    f1=a
else:
    f1=b
if c>d:
    f2=c
else:
    f2=d
if f1>f2:
    print(f1,"is greater than ",f2)
else:
    print(f2,"is greater than ",f1)
        

