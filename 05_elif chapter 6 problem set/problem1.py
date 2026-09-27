a=int(input("Enter a number:"))
b=int(input("Enter another number: "))
c=int(input("Enter another number: "))
d=int(input("Enter another number: "))
if(a>b and a>c and a>d ):
    print(f"{a} is the greatest of all.")

if(b>a and b>c and b>d ):
    print(f"{b} is the greatest of all.")
if(c>b and c>a and c>d ):
    print(f"{c} is the greatest of all.")

if(d>b and d>c and d>a ):
    print(f"{d} is the greatest of all.")
