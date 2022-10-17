# here we will aloot the grade to the student.
a=int(input("Enter the student marks between 100:\n"))

if a>=90 and a<100:
    print("Congratulation!! Your grade is excellent.")
elif a>=80 and a<90:
    print("Congratulation!! Your grade is A.")
elif a>=70 and a<80:
    print("Congratulation!! Your grade is B.")
elif a>=60 and a<70:
    print("Congratulation!! Your grade is C.")
elif a>=50 and a<60:
    print("Congratulation!! Your grade is D.")
elif a<50:
    print("Sorry you are fail in subject.")