'''
Необхідно написати класс Car який має атрибути fuel(паливо, задається за допомогою random.randrange(0, 9)),
trip_distance(Відстань яку проїхав автомобіль), model (модель авто) та color(колір)ю
реалізувати в класі метод move який приймає distance як аргумент.

Створити 3 екземпляра цього классу

В циклі while race_dist < desired_dist: необхідно для кожного екземпляру класу викликати метод move
та передати йому значення random.randrange(0, 9). Метод move повинен додавати до trip_distance значення,
яке було повернуто методом randomrange та зменшити кількість палива на це ж значення

Як тільки один із автомобілів проїхав відстань більшу або яка дорівнює desired_dist -
вивести повідомлення про те що автомобіль переміг, вказавши марку та дистанцію яку проїхав цей автомобіль.
Цикл необхідно у такому випадку перервати

Після циклу необхідно вивести повідомлення про те скільки і який автомобіль проїхав, та який у нього запас палива
'''


import random
class Car:
    def __init__(self, model, color):
        self.fuel = random.randrange(0, 9)
        self.trip_distance = 0
        self.model = model
        self.color = color

    def move(self, distance):
        if self.fuel == 0:
            return False
        if self.fuel < distance:
            distance = self.fuel
        self.trip_distance += distance
        self.fuel -= distance
        return True

car1 = Car('Honda NSX', 'Red')
car2 = Car('Toyota Supra', 'Orange')
car3 = Car('Nissan GTR', 'Gray')

cars = [car1, car2, car3]
cars_without_fuel = []
desired_dist = 8
flag = None

while cars:
    for car in cars[:]:
        if not car.move(random.randrange(0, 9)):
            cars.remove(car)
            cars_without_fuel.append(car)
            if not cars:
                longest_dist = max(cars_without_fuel, key=lambda _: _.trip_distance)
                print(f'All cars ran out of fuel.')
                print(f'{longest_dist.color} {longest_dist.model} has longest distance {longest_dist.trip_distance}!')
                break
            continue
        if car.trip_distance >= desired_dist:
            flag = car
            break
    if flag:
        break

if flag:
    print(f'{flag.color} {flag.model} WINS, distance - {flag.trip_distance} km!')

print('=== OVERALL RESULTS ===')
for car in cars + cars_without_fuel:
    status = 'out of fuel' if car.fuel == 0 else f'fuel left: {car.fuel}'
    print(f'{car.color} {car.model} drove by {car.trip_distance} km ({status})')


