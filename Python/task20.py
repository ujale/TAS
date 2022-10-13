#Lesson 20 Task

# Create a class called Human
# Add an attribute leg_count with the value of 4
# Add a method called get_gender() that returns "Unknown" in the Human class
# Create another class called Man that extends Human

# Optionally you can instantiate the classes Man and Woman then print out the values of the get_gender() method in each object instance

class Human:

    leg_count = 4

    def get_gender(self, ugender):
        return ugender


class man(Human):
    pass

class woman(Human):
    pass


man1 = man()
print(man1.get_gender("unknown"))

woman1 = man()
print(woman1.get_gender("unknown"))