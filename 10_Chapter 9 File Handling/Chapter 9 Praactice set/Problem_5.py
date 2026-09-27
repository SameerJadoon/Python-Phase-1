words=["donkey", "shouting", "tired"]
with open("Censor.txt") as f:
    content=f.read()
for word in words:
    content=content.replace(word,"#"*len(word))

with open("Censor.txt","w") as f:
    f.write(content)