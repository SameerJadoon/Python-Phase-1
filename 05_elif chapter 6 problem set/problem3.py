p1="Makes alot of Money."
p2="Buy know."
p3="subscribe this."
p4="click this."
comment=input("Enter your comment here.")

if(p1 in comment or p2 in comment or p3 in comment or p4 in comment):
    print("This comment is a spam.")
else:
    print("Your comment is not a spam.")