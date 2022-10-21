# here we will create a function for printing a table for given number.
def tab(n):
    for i in range(1,11):
        print(f"{n}x{i}={n*i}")
        i=i+1

num=int(input("Enter a number:"))
tab(num)