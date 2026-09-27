with open("This.txt") as f:
    content = f.read()

with open("log.txt") as f:
    content_2=f.read()
if(content==content_2):
    print("Both are same.")
else:
    print("They are not same.")