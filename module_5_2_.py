class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
        
    def __str__(self):
        return str(f' Название: "{self.name}". Кол-во этажей: {self.number_of_floors}.')
 
    def __len__(self):
        return int(self.number_of_floors)

    def go_to(self, new_floor):
        new_floor = int(input('Enter your level please: '))
        match new_floor:
            case 1 | 2 | 3 | 4 | 5 :
                print(f'Welcome to {new_floor} level. Have a good time!')   
            case _:
                print('The floor is not exist')
    
pass

house1 = House('ЖК Эльбрус', 30)
house2 = House('ЖК Акация', 10)

print(str(house1))
print(len(house1))

print(str(house2))
print(len(house2))

house1.go_to(0)
