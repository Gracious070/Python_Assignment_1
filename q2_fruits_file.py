fruits = ["Mango", "Banana", "Pineapple", "Grapes", "Orange"]

# Write the fruits to the file, one per line
with open("fruits.txt", "w") as file:
    for fruit in fruits:
        file.write(fruit + "\n")

# Read the fruits back and display them
with open("fruits.txt", "r") as file:
    contents = file.readlines()

print("Fruits in the file:")
for line in contents:
    print(line.strip())