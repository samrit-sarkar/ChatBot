class Student:
    def __init__(self, name, roll_no, marks):
        self._name = name
        self._roll_no = roll_no
        self._marks = marks

    def set_name(self, name):
        if name == "":
            print("Name cannot be empty.")
        else:
            self._name = name

    def set_roll_no(self, roll_no):
        if(roll_no < 1 and roll_no > 100):
            print("Roll number must be between 1 and 100.")
        else:
            self._roll_no = roll_no

    def set_marks(self, marks):
        if(marks < 0):
            print("Marks cannot be less than zero.")
        else:
            self._marks = marks

    def display(self):
        print(f"Name: {self._name}")
        print(f"Roll No: {self._roll_no}")
        print(f"Marks: {self._marks}")

student1 = Student("Samrit", 23, 80)

student1.display()

print("\nUpdating Details...")

student1.set_name("")
student1.set_roll_no(101)
student1.set_marks(-1)

print()
student1.display()