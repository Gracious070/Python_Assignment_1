age = None

while age is None:
    user_input = input("Enter your age: ")
    try:
        age = int(user_input)
    except ValueError:
        print("That's not a valid whole number. Please try again.")

print(f"Your age is {age}")