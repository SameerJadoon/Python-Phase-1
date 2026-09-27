s={1,3,4,2,34,"Sameer"}
print(s,type(s))
s.add(5) #adds a value in the set
print(s,type(s  ))
print(len(s)) 
s.remove(5)# Removes element from the set
print(s,type(s))
# s.clear() Empties the whole set
print({1,3}.issubset(s))
print({1,9,3,4,2,34,"Sameer"}.issuperset(s))