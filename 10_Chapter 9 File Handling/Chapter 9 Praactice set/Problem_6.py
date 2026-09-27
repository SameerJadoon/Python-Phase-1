with open("log.txt") as f:
    content=f.read()
    content=content.lower()

# if content.__contains__("python"):
#     print("Present")
if "python" in content:
    print("python is present.")
else:
    print("Python is not present.")