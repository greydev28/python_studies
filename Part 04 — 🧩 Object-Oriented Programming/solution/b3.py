class Animal:
    def __init__(self,name):
        self.name = name


class Dog(Animal):
    def __init__(self,name):
          super().__init__(name)

    def bark(self):
         print(f'{self.name} barks')

dog1 = Dog("j.spark")
dog1.bark()

class vehicle:
     def __ini__(self,brand):
          self.brand = brand

class Car(vehicle):
     def __init__(self,brand):
          super().__init__(brand)
     def honk(self):
          print(f'{self.brand}-honk powpow')

toyota1 = Car("avalon")

toyota1.honk()