def generatetable(i):   
    table=""
    for t in range(1,11):
        
        print(f"{i}x{t}={t*i}")
        table+=f"{i}x{t}={t*i}\n"
    with open(f"Tables/Table_{i}","w") as f:
        f.write(table)




for s  in range(2,21):
    generatetable(s)