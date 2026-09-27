lineno =0

with open("log.txt") as f:
    lines=f.readlines()
    for line in lines:
        lineno+=1
        if "python" in line:
            print(f"Python is present at {lineno}")
            break;
    else:
        print("Python is not present") 