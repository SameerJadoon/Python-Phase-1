def rem(l,word):
    n=[]
    for items in l:
        n.append(items.strip(word))
        return n

l=["Sameer","Jadoon","Samiullah","Jadoon"]
print(rem(l,"oon"))
