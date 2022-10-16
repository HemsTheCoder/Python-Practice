# here we are creating a hindi dictionary.
hindi={"pyar":"Love",
    "parivar":"Family",
    "jeevan":"Life"}
print(hindi.keys())
a=input("Type your selected option:\n")

print("Meaning of your selected word is: ",hindi.get(a))
