# here we will check the name is present in list or not. 
name=["hems","ambu","goku"]
a=input("Enter a name to check in list:\n")
if(a in name ):
    print(a,"is present inside the list.")
else:
    print(a,"is not present inside the list.")

print("here is the list:",name)