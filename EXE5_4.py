
class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Машина поехала')

    def stop(self):
        print('Машина остановилась')

    def turn(self):
        print('Машина повернула')

    def show_sped(self):
        print('Текущая скорость автомобиля')


class TownCar(Car):
    def show_speed(self):
        message = 'Скорость автомобиля' + ' ' +  str(self.speed)
        if float(self.speed) > 60:
            message = 'Скорость превышена'
        return message


class SportCar(Car):
    def show_speed(self):
        return 'Скорость автомобиля' + ' ' +  str(self.speed)


class WorkCar(Car):
    def show_speed(self):
        message = 'Скорость автомобиля' + ' ' + str(self.speed)
        if float(self.speed) > 40:
            message = 'Скорость превышена'
        return message


class PoliceCar(Car):
    def show_speed(self):

        return 'Скорость автомобиля' + ' ' + str(self.speed)


car_1 = PoliceCar(80, 'white', 'Lada', True)
print(car_1.name)
print(car_1.color)
print(car_1.speed)
print(car_1.show_speed())
car_2 = WorkCar(90, 'green', 'Renault', False)
print(car_2.name)
print(car_2.color)
print(car_2.speed)
print(car_2.show_speed())
