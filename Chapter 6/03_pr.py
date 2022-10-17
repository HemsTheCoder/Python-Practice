# here we will detect the spam comment.
comm=input("Enter the comment:\n")

if("make lot of money" in comm):
  print("it is spam comment")
elif("click this" in comm):
    print("it is spam comment")
elif("subscribe this" in comm):
    print("it is spam comment")
elif("buy now" in comm):
    print("it is spam comment")
else:
    print("it is not a spam")