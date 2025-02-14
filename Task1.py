class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    
    def display_info(self):
        print(f"Car Brand: {self.brand}")
        print(f"Car Model: {self.model}")
        print(f"Year: {self.year}")

# Creating two car objects
car1 = Car("BMW", "M2 Coupe", 2025)
car2 = Car("Audi", "RS Q8 SUV", 2025)

# Displaying their details
car1.display_info()
print()  # Adding a blank line between the car details
car2.display_info()
