# here we will remove the name from the string using function. 

name=input("Enter a name you want to remove:")
st=("hemant hems sugam vishal")
def remName(l,n):
   newl=l.replace(n,"")
   return newl.strip()

s=remName(st,name)
print(s)