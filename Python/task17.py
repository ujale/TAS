class Human:

    name = "Bob"
    age = 13
    sex = "Male"

    def get_name_sex(self):
        return self.name + ":" + self.sex

bob = Human()
print(bob.name, bob.age, bob.get_name_sex())


