'''
Additional task 49

'''

# class Car:
#     fuel_tipes = ['бензин', 'дизель', 'електрика', 'гібрид']
#     colors = []
#     number_of_cars = 2
#
#     def __init__(self, model, year, fuel_tipe, color):
#         self.model = model
#         self.year = year
#         self.color = color
#         self.fuel_tipe = self.is_valid_fuel_type(fuel_tipe)
#         self.number = Car.number_of_cars
#         Car.number_of_cars += 2
#         if not color in Car.colors:
#             Car.colors.append(color)
#
#     def __str__(self):
#         return f'{self.model} {self.year} {self.fuel_tipe} {self.color}'
#
#     @property
#     def numbers(self):
#         return f'{self.number} from {Car.number_of_cars - 2}'
#
#     @staticmethod
#     def is_valid_fuel_type(fuel_tipe):
#         return fuel_tipe if fuel_tipe in Car.fuel_tipes else Car.fuel_tipes[0]
#     @classmethod
#     def get_used_colors(cls):
#         return f'we used {len(Car.colors)} colors'
#
#     @classmethod
#     def get_number_of_cars(cls):
#         return f'We to produce {Car.number_of_cars - 2} cars'
#
#
# car_1 = Car('Zaz', 1979, 'дизель', 'black')
# car_2 = Car('BMW', 2000, 'бензин', 'red')
# car_3 = Car('VOLVO', 2012, 'електрикаcccc', 'black')
# car_4 = Car('Mersedes', 2012, 'гібрид', 'black')
# print('COLORS:', Car.get_used_colors())
# print('NUMBER_OF_CARS:', Car.get_number_of_cars())
# for item in (car_1, car_2, car_3, car_4):
#     print('item:', item)
#     print('numbers:', item.numbers)