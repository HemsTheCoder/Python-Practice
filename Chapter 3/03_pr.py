# here we will replace double space with the single space. 
a="\n\nHello  my  name  is  Hemant  and  i  am  replacing  double  space  with  single  space.\n\n"
b=" "
a=a.replace("  ",b)
print(a)