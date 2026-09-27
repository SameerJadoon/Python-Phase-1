import os

# Specify the directory
directory = "/5th Semester Data"

# Get the contents of the directory
contents = os.listdir(directory)

# Print each item
for item in contents:
    print(item)
