letter ='''Dear <|Name|>,
...........You are selected!
...........<|Date|>'''
a=input("Enter your name: ")
b=input("Enter today's date: ")
print(letter.replace("<|Name|>", a).replace("<|Date|>", b))