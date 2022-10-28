# here i will check does txt file consist the given world or not.
f=open('sample.txt','r')
text=f.read()
print(text)
a=input("Enter the word you want to search in a text file:")
if a in text:
    print(f"'{a}' word is present")
else:
    print(f"'{a}' word is  not present")
f.close()