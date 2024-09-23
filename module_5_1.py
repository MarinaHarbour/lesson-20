class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        i = int
        if new_floor > self.number_of_floors or new_floor < 1:
            print(f'Такого этажа не существует')
        else:
            for i in range(new_floor):
                print(i + 1)


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)


print(h1.name, h1.number_of_floors)
h1.go_to(5)
print(h2.name, h2.number_of_floors)
h2.go_to(10)
