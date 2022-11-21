# Using the OOP feature Inheritance, create a class Animal with the method sound()
# and then create a Cat and Dog class that inherits from the Animal class.
# The Cat and Dog class should override the sound class and print a different sound

class Animal:

    def print_animal_sound(self, sound):
        return sound


animal = Animal()
print(animal.print_animal_sound("unknown"))


class Cat(Animal):
    sound = "Meow"


class Dog(Animal):
    sound = "Bark"


cat = Animal()
print(cat.print_animal_sound("Meow"))
dog = Animal()
print(dog.print_animal_sound("Bark"))
