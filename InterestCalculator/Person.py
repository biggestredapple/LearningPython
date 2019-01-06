class Person:
    instances = 0

    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age
        Person.instances += 1


person1 = Person(1, "Shiva Sai", 34)
person2 = Person(2, "Rajesh", 36)

print("----- Person Details -----")
print('Person.Instances: ', Person.instances)
print('Person 1: ', person1.id, person1.name, person1.age)
print('Person 2: ', person2.id, person2.name, person2.age)