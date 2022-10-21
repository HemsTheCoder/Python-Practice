# here we will print the sum of natural number using the recursion.
num=int(input("Enter a number:"))

def sum(n): 
     if n <= 1:
       return n
     else:
       return n + sum(n-1)
d=sum(num)
print(f"sum of number {num} is {d}")
    