class Animals:
    def __init__(self, name, animal_type, color, age, quantity):
        self.name = name
        self.animal_type = animal_type.title()
        self.color = color.lower()
        self.age = int(age)
        self.quantity = int(quantity)

    def animal_quantity_zero(self):
        print(f'So, I was {self.name} with {self.color} color, '
              f'my age was {self.age} years old, but now i`m gone')

    def animal_quantity_one(self):
        print(f'I`m {self.name} with {self.color} color, '
              f'my age {self.age} years old, '
              f'and I`m alone')

    def animal_quantity_many(self):
        print(f'So, we are {self.name}`s with {self.color} color, '
              f'our age {self.age - 2}-{self.age + 2} years each, '
              f'and our quantity is {self.quantity} individuals')


class Animal_info(Animals):
    def type_of_animal(self):
        print(f'\nAnimal type "{self.animal_type}" is incorrect, we can`t give you any info.')


class Fish(Animal_info):
    def type_of_animal(self):
        print(f'\nAnimal type: {self.animal_type}\n')
        if self.quantity > 1:
            Animal_info.animal_quantity_many(self)
        elif self.quantity == 1:
            Animal_info.animal_quantity_one(self)
        elif self.quantity == 0:
            Animal_info.animal_quantity_zero(self)


class Snake(Animal_info):
    def type_of_animal(self):
        print(f'\nAnimal type: {self.animal_type}\n')
        if self.quantity > 1:
            Animal_info.animal_quantity_many(self)
        elif self.quantity == 1:
            Animal_info.animal_quantity_one(self)
        elif self.quantity == 0:
            Animal_info.animal_quantity_zero(self)


class Bird(Animal_info):
    def type_of_animal(self):
        print(f'\nAnimal type: {self.animal_type}\n')
        if self.quantity > 1:
            Animal_info.animal_quantity_many(self)
        elif self.quantity == 1:
            Animal_info.animal_quantity_one(self)
        elif self.quantity == 0:
            Animal_info.animal_quantity_zero(self)


class Animal(Animal_info):
    def type_of_animal(self):
        print(f'\nAnimal type: {self.animal_type}\n')
        if self.quantity > 1:
            Animal_info.animal_quantity_many(self)
        elif self.quantity == 1:
            Animal_info.animal_quantity_one(self)
        elif self.quantity == 0:
            Animal_info.animal_quantity_zero(self)


class Insect(Animal_info):
    def type_of_animal(self):
        print(f'\nAnimal type: {self.animal_type}\n')
        if self.quantity > 1:
            Animal_info.animal_quantity_many(self)
        elif self.quantity == 1:
            Animal_info.animal_quantity_one(self)
        elif self.quantity == 0:
            Animal_info.animal_quantity_zero(self)


types = {'animal': Animal, 'fish': Fish, 'snake': Snake, 'bird': Bird, 'insect': Insect}

name = input('What is the name of animal? ')
animal_type = input("What type of animal (animal/fish/snake/bird/insect) ? ")
color = input("What color of animal? ")
age = input("What if age? ")
quantity = input("How much they are? ")

AnimalClass = types.get(animal_type.lower(), Animal_info)
animal_instance = AnimalClass(name, animal_type, color, age, quantity)

if __name__ == '__main__':
    animal_instance.type_of_animal()