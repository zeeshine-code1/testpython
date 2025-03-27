# # # # # def check_odd_or_even():
# # # # #     try:
# # # # #         # Taking input from the user
# # # # #         number = int(input("Enter an integer: "))
        
# # # # #         # Checking if the number is even or odd
# # # # #         if number % 2 == 0:
# # # # #             print(f"The number {number} is even.")
# # # # #         else:
# # # # #             print(f"The number {number} is odd.")
# # # # #     except ValueError:
# # # # #         print("Please enter a valid integer.")

# # # # # # Let's test the function
# # # # # check_odd_or_even()

# # # # # class Students:
# # # # #     def __init__(self, name, marks):
# # # # #         self.name = name
# # # # #         self.marks = marks
# # # # #         print("adding students in the database..")

# # # # # s1= Students("Zeeshan", 9)
# # # # # print(s1.name)

# # # # # s2 = Students("Yasir")
# # # # # print(s2.name)

# # # # class Students:
# # # #     college_name = "Apna College"
# # # #     def __init__(self, name, marks=0):  # Added default value of 0 for marks
# # # #         self.name = name
# # # #         self.marks = marks
# # # #         print("adding students in the database..")

# # # # s1 = Students("Zeeshan", 9)
# # # # print(s1.name) 
# # # # print(s1.marks) 
# # # # print(s1.college_name) 

# # # # s2 = Students("Yasir", 9) 
# # # # print(s2.name) 
# # # # print(s2.marks) 

# # # class Car:
# # #     @staticmethod
# # #     def start():
# # #         print("car started")

# # # @staticmethod
# # # def stop():
# # #     print("car stopped")

# # # class ToyotaCar(Car):
# # #     def __init__(self, name):
# # #        self.name = name

# # # car1 = ToyotaCar("a")
# # # car2 = ToyotaCar("b")

# # # print(car1.start)

# # class Car:
# #     @staticmethod
# #     def start():
# #         print("car started")

# #     @staticmethod
# #     def stop():  # Now inside the Car class
# #         print("car stopped")

# # class ToyotaCar(Car):
# #     def __init__(self, name):
# #        self.name = name

# # car1 = ToyotaCar("a")
# # car2 = ToyotaCar("b")

# # print(car1.start)
# # car1.stop()  # Call stop on an instance of the class

# class Person:
#     def __init__(self, fname, lname):
#         self.firstname = fname
#         self.lastname = lname
#     def printname(self):
#         print(self.firstname, self.lastname)

# x = Person("John", "Doe")
# x.printname()

my_list = [1, 2, 3, 4]

# Create an iterator from the list
my_iterator = iter(my_list)

# Get the next element
print(next(my_iterator))  # Output: 1
print(next(my_iterator))  # Output: 2

# Keep getting elements until StopIteration is raised
