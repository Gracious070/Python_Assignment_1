# --- Part i: Dictionary of students and marks ---

students = {
    "Alice": 78,
    "Brian": 85,
    "Carla": 92,
    "David": 67,
    "Ella": 88
}

print("Student marks:")
for name, mark in students.items():
    print(f"{name}: {mark}")

top_student = max(students, key=students.get)
print(f"\nTop student: {top_student} with {students[top_student]} marks")


# --- Part ii: Book class ---

class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display_details(self):
        print(f"\nTitle: {self.title}")
        print(f"Author: {self.author}")
        print(f"Price: ${self.price}")


book1 = Book("Python Crash Course", "Eric Matthews", 35.99)
book2 = Book("Atomic Habits", "James Clear", 18.50)

book1.display_details()
book2.display_details()