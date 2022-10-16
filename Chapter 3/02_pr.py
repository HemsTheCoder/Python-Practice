# here we will use replace method of strinr to replace the value in letter.
letter="***************************************************\n Dear <|NAME|>. \n \tYou are selected.\n Thank you \n |DATE|\n***************************************************"
name=input("Enter your name:\n")
date=input("Enter date:\n")
letter=letter.replace("<|NAME|>",name)
letter=letter.replace("|DATE|",date)
print(letter)