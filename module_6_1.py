class Animal:
    alive = True  # живой
    fed = False  # голодный

    def __init__(self, name):
        self.name = name


class Plant:
    edible = False  # несъедобное

    def __init__(self, name):
        self.name = name


class Mammal(Animal):
    def eat(self, food):
        if food.edible == False:
            print(f'{self.name} не стал есть {food.name}')
            self.fed = False
            self.alive = True
        else:
            print(f'{self.name} съел {food.name}')
            self.fed = True
            self.alive = True

    pass


class Predator(Animal):
    def eat(self, food):
        if food.edible == False:
            print(f'{self.name} не стал есть {food.name}')
            self.alive = False
        else:
            print(f'{self.name} съел {food.name}')
            self.fed = True


class Flower(Plant):
    pass


class Fruit(Plant):
    edible = True
    pass


a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')
print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)
