subject1=int(input("Enter first subject's marks"))
subject2=int(input("Enter second subject's marks"))
subject3=int(input("Enter third subject's marks"))
total_marks=int(input("Enter total marks:"))


if((subject1/total_marks)*100>=33 and (subject2/total_marks)*100>=33 and (subject3/total_marks)*100>=33 and ((subject1+subject2+subject3)/(total_marks*3))*100>=40):
    print("You have passed the exam!")

else:
    print("You have failed the exam")
    print("Better Luck Next time.")
             