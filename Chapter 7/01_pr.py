# here we will perform the table.
t=int(input("Enter table you want to print: "))
i=1
print("Using while loop print table")
while i<=10:
    print(t,"x",i,"=",t*i)
    i=i+1
print("Using for loop print table")

for i in range (1,11):
    print(t,"x",i,"=",t*i)