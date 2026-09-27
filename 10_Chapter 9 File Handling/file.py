"""
if we want to save contents of a program like input data or 
any thing to save permanently in our computer we use file handling there
"""

f = open("file.txt")# This is default function to open a file(file name +the mod in which you want the file to open )
data = f.read()
print(data)
f.close()