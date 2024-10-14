class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        i = 1
        if new_floor > self.number_of_floors or new_floor < 1:
            return print('Такого этажа не существует')
        else:
            while i <= new_floor:
                print(i)
                i += 1


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h3 = House('ЖК Апельсин', 20)
h1.go_to(5)
h2.go_to(10)
h3.go_to(18)
h3.go_to(25)
