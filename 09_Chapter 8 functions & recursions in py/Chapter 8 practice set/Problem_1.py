def greatest_of_three(num1,num2,num3):
    if(num1>num2 and num1>num3):
        print(f"{num1} is the greatest of all.")
    elif(num2>num1 and num2>num3):
        print(f"{num2} is the greatest of all.")
    elif(num3>num2 and num3>num1):
        print(f"{num3}is the greatest of all.")

num1=int(input("Enter a Number: "))
num2=int(input("Enter a Number: "))
num3=int(input("Enter a Number: "))
greatest_of_three(num1,num2,num3)