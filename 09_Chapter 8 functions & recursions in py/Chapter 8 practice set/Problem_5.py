def pattern(n):
    # for i in range(0,n):
    #     print("*"*(n-i))
    if(n==0):
        return
    print("*"*n)
    pattern(n-1)

pattern(6)