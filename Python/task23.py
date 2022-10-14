# Lesson 23 Task

# Create a class called User
# Create a private attribute called __password with the value "password" in the User class
# Create a method get_password() that returns self.__password in the User class
# Create another class called ActiveUser that inherits from the User class
# Create a method get_password() that returns "********" in the ActiveUser class
# Instantiate an object of the ActiveUser class
# Print the value of get_password() from the object instance

class User:
    __password = "password"

    def get_password(self):
        return self.__password

user = User()
print(user.get_password())

class ActiveUser(User):

    def get_password(self):
        return "**********"

active = ActiveUser()
print(active.get_password())
