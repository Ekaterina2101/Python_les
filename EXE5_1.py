import time


class TrafficLight:
    __color = None

    def running(self):
        TrafficLight.__color = "red"
        print(TrafficLight.__color)
        time.sleep(7)
        TrafficLight.__color = "yellow"
        print(TrafficLight.__color)
        time.sleep(2)
        TrafficLight.__color = "green"
        print(TrafficLight.__color)
        time.sleep(7)
        TrafficLight.__color = "yellow"
        print(TrafficLight.__color)
        time.sleep(2)


a = TrafficLight()
while True:
    a.running()
