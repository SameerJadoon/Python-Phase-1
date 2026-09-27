marks={
    "Sameer":99,
    "Ali": 0,
    "Gull":50,              #Left one is key and the corresponding right one is the value
    "Sudais":99,
    "list":[1,2,3,4]
}
# print(marks.items()) # Returns a list of key value pairs
# print(marks.keys()) #Returns keys of the dictionary
# print(marks.values()) # prints the values of the dictionary
# marks.update({"list":100}) #updates the orignal dictionary(add + update) because dictionary is mutable
# print(marks)
print(marks.get("Sameer")) #Gives none if marks are not present
print(marks["Sameer"])  # Gives error if the requested value is not present