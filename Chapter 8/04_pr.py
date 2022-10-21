# here we will print the pattern using the function. 
num=int(input("Enter a number:"))

def patt(n):
    while n>=0:
        print("*"*n)
        n=n-1
patt(num)