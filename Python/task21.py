#Lesson 21 Task

# Create a class called Human
# Add an attribute leg_count with the value of 4
# Add a method called get_gender() that returns "Unknown" in the Human class
# Create another class called Man that extends Human
# Create another class called Woman that extends Human
# In the class, Man create the method get_gender() which should return "man"
# In the class, Woman create the method get_gender() which should return "woman"
# Instantiate the Man and Woman classes
# Print out the value of get_gender() from the Man and Woman object instances

class Human:

    leg_count = 4

    def get_gender(self, unkno):
        return unkno

human = Human()
print(human.get_gender("Unknown"))

class Man(Human):

    def get_gender(self, unkno):
        return unkno
man = Human()
print(man.get_gender("Man"))

class Woman(Human):

    def get_gender(self, unkno):
        return unkno


woman = Human()
print(woman.get_gender("Woman"))