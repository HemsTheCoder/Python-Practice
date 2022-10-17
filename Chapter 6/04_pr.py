# here we will check does username is less than 10 char or not. 
user=input("Enter user name:\n")
l=len(user)
if l>10:
    print("invalid!! user name please enter less than 10 character.")
else:
    print("congratulation user name is valid.")
