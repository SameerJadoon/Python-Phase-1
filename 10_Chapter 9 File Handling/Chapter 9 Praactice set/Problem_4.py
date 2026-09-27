with open("Donkey.txt") as f:
    c=f.read()
    c=c.lower()
if("donkey" in c):
    c=c.replace("donkey", "#####")
    with open("Donkey.txt",'w') as f:
        f.write(c)
    