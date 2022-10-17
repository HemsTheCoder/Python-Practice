# here we will use if else to check weather student is pass or fail.
print("*******Enter your marks*******")
s1=int(input("Input subject 1 marks:-"))
s2=int(input("Input subject 2 marks:-"))
s3=int(input("Input subject 3 marks:-"))
sp=(s1+s2+s3)/300
per=sp*100
print(per,"%")

if (s1<33 or s2<33 or s3<33):
    print("you are failed in one subject.")    
elif per>40:
     print("You passed the exam.You have",per,"%")
else:
    print("You failed the exam.You have",per,"%")