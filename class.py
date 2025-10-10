import random
# Always start class name with capital letter - convention
class Human:
    def __init__(self):
        pass

    def speak(self):
        print("Hello, I am a human.")

class Employee(Human): # Inheritance - Employee class inherits from Human class
    # Class variable - shared by all instances of the class
    # When you create a class, the first thing you should do is to create a docstring for the class. This will help others to understand what the class is about.
    """A class to represent an employee.
    1. This class demonstrates the use of __new__ and __init__ methods.
    2. It also shows how to create objects and access their attributes and methods.
    3. __new__ is called to create a new instance of the class, while __init__ initializes the instance.
    4. The class has attributes like name, age, and salary, and a method to display employee information.
    5. This example is created by Alok Sharma.
    """
    
    # __new__ is a special method used to create objects, is also known as a factory method. It is called before __init__.
    def __new__(cls, *args, **kwargs):
        print("Creating __new__ instance")
        return super(Employee, cls).__new__(cls) #calls the parent class's __new__ method to create the instance

    # __init__ is a special method used to initialize objects, is also known as a constructor.
    def __init__(self, name, age, salary) -> None: # type hinting, shows the return type of the function
        print("Initializing __init__ instance")
        self.name = name
        self.age = age
        self.salary = salary
        super().__init__() #calls the parent class's __init__ method to initialize the instance

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}")


    # Class method needs class as the first parameter, conventionally named cls
    # Class method can access class variables and modify class state that applies across all instances of the
    @classmethod
    def update_salary(cls, new_salary=None):
        if new_salary is None:
            new_salary = random.randint(30000, 100000)
        # cls.default_salary = new_salary
        cls.salary = new_salary
        print(f"Updated company-wide salary benchmark to {new_salary}")
    
    # Static method does not take self or cls as the first parameter
    # Static method cannot access or modify class state
    @staticmethod
    def company_policy():
        print("Company policy: All employees must adhere to the code of conduct.")


Employee.update_salary() # Class method can be called without creating an object of the class

#Creating objects of the class
emp1 = Employee("Alice", 30, 70000)
emp2 = Employee("Bob", 25, 50000)
print(emp1.name)  # Accessing attributes
emp2.display_info()  # Calling method

print('Returns the doc string', Employee.__doc__)  # Accessing class docstring
print('Returns attributes in dict type', Employee.__dict__) # Accessing class attributes and methods dictionary
print('Return name of the file of Employee class:', Employee.__module__) # Accessing module name where the class is defined
print('Returns base class if any:', Employee.__bases__)  # Accessing base classes of the class
print('Returns Name of the class:', Employee.__name__)   # Accessing class name
