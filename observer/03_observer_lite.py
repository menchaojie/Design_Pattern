# 01_observer_lite.py 中的例子有点复杂，实现一个简单的，以气象站为例的观察者模式
from abc import ABC, abstractmethod

# interface of the observer
class Observer(ABC):
    @abstractmethod
    def update(self, temperature, humidity, pressure):
        pass

# omit the interface of the subject
# directly implement the subject
class WeatherStation:
    def __init__(self):
        self._observers = []
        self._temperature = 0
        self._humidity = 0
        self._pressure = 0

    def add_observer(self, observer: Observer):
        self._observers.append(observer)
    
    def remove_observer(self, observer: Observer):
        self._observers.remove(observer)
    
    def set_state(self, temperature, humidity, pressure):
        self._temperature = temperature
        self._humidity = humidity
        self._pressure = pressure
        self.notify_observers()
    
    def notify_observers(self):
        for observer in self._observers:
            observer.update(self._temperature, self._humidity, self._pressure)

# imply the first observer
class DisplayDevice:
    def update(self, temperature, humidity, pressure):
        self.display()
        print(f"temperature: {temperature}, humidity: {humidity}, pressure: {pressure}")
    
    def display(self):
        print("display the weather on device")

# imply the second observer
class DisplayApp:
    def update(self, temperature, humidity, pressure):
        self.display()
        print(f"temperature: {temperature}, humidity: {humidity}, pressure: {pressure}")
    
    def display(self):
        print("display the weather on app")
    
def main():
    weather_station = WeatherStation()

    display_device = DisplayDevice()
    weather_station.add_observer(display_device)

    display_app = DisplayApp()
    weather_station.add_observer(display_app)

    print("======= the init state ===========")
    weather_station.set_state(20, 60, 1000)
    print("=======  state change from wetherstation ===========")
    weather_station.set_state(30, 70, 2000)

if __name__ == "__main__":
    main()