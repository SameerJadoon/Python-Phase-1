with open("This.txt") as f:
    content=f.read()

with open("Copy_This.txt","w") as f:
    f.write(content)