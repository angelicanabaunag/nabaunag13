class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course
    
    def introduce(self):
        print(f"Hello, my name is {self.name}. I am {self.age} years old and I'm studying {self.course}.")

# Creating three student objects
student1 = Student("Asher", 19, "Computer Science")
student2 = Student("Hugo", 20, "Engineering")
student3 = Student("Jordan", 20, "Architecture")

# Calling the introduce method for each student
student1.introduce()
student2.introduce()
student3.introduce()
