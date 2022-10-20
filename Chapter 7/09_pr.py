# here we will print the table in a reverse order.
num=int(input("Enter a number:"))
for i in range(10,0,-1):
  
    if i<=10:
       print(num,"x",i,"=",num*i)