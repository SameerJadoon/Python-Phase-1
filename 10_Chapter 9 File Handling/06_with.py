f=open("file.txt")
print(f.read())
f.close()
#The same above can be done using with statement 
with open("file.txt") as f:
    print(f.read())
#By using with statement you don't have to close the file explicitly