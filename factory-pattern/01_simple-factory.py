"""
 * @file            factory-pattern/simple-factory.py
 * @description     test the simple factory pattern
 * @author          menchaojie <menchaojie@163.com>
 * @createTime      2026-01-27 10:41:49
 * @lastModified    2026-01-27 13:07:51
 * Copyright ©YourCompanyName All rights reserved
"""

from abc import ABC, abstractmethod

# 产品接口
class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

# 具体产品
class Dog(Animal):
    def speak(self):
        return "汪汪！"

class Cat(Animal):
    def speak(self):
        return "喵喵！"

# 简单工厂
# 这个是简单工厂模式的实现，它根据传入的动物类型参数，返回对应的动物对象。
# 如果传入的动物类型参数未知，则抛出 ValueError 异常。
# 这样将相似类创建对象的过程集中到一个工厂类中, 客户端只需要知道工厂类的名称, 就可以创建出需要的对象

class AnimalFactory:
    @staticmethod
    def create_animal(animal_type):
        if animal_type == "dog":
            return Dog()
        elif animal_type == "cat":
            return Cat()
        else:
            raise ValueError(f"未知的动物类型: {animal_type}")

# 使用示例
def test_simple_factory(animal_type):
    factory = AnimalFactory()
    animal = factory.create_animal(animal_type)
    print(animal.speak())  

if __name__ == "__main__":
    test_simple_factory("cat")