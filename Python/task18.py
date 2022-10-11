class Human:

    leg_count = 4
    can_walk = True

    def __init__(self, name):
        self.name  = name

count = Human(4)
walk = Human(True)

print(count.name)
print(walk.name)
