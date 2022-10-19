# Lesson 25 Task

# Create a class called Utilities
# Create a static method called print_name which accepts a parameter, and prints out the parameter.
# Invoke the static method print_name()
# You can use any of the two methods to create your static methods.

class Utilities:

    def print_name(firstname):
        return firstname

Utilities.print_name = staticmethod(Utilities.print_name)
print("The first name is :", Utilities.print_name("Johnson"))

# Method 2

class Utilities:

    @staticmethod
    def print_name(firstname):
        return firstname

print("The first name is :", Utilities.print_name("Johnson"))