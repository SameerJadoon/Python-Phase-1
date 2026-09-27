
f=open("poem.txt")
c=str(f.read())
c = c.lower()
if("twinkle" in c):
    print("Twinkle is present ")
else:
    print("Twinkle is not present in the content")