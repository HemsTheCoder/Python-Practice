# here we will find the given number is prime or not using for loop. 
num=int(input("Enter a number:\n"))
for i in range(2,(num+1)):
    if(num%i==0):
       prime=True
    else:
       prime=False
if prime:
    print("prime")
else:
    print("not prime")