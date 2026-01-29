"""
 * @file            factory-pattern/factory-method.py
 * @description     test the factory method pattern
 * @author          menchaojie <menchaojie@163.com>
 * @createTime      2026-01-27 14:09:28
 * @lastModified    2026-01-27 14:09:28
 * Copyright ©YourCompanyName All rights reserved
"""

from abc import ABC, abstractmethod

# 产品接口 - 动物
class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass
    
    @abstractmethod
    def eat(self):
        pass

# 具体产品 - 狗
class Dog(Animal):
    def speak(self):
        return "汪汪！"
    
    def eat(self):
        return "狗在吃狗粮"

# 具体产品 - 猫
class Cat(Animal):
    def speak(self):
        return "喵喵！"
    
    def eat(self):
        return "猫在吃猫粮"

# 创建者抽象类 - 动物饲养员
class AnimalKeeper(ABC):
    @abstractmethod
    def create_animal(self) -> Animal:
        pass
    
    def care_for_animal(self):
        # 调用工厂方法创建动物
        animal = self.create_animal()
        speak_result = animal.speak()
        eat_result = animal.eat()
        return f"{speak_result} {eat_result}"

# 具体创建者 - 狗饲养员
class DogKeeper(AnimalKeeper):
    def create_animal(self) -> Animal:
        return Dog()

# 具体创建者 - 猫饲养员
class CatKeeper(AnimalKeeper):
    def create_animal(self) -> Animal:
        return Cat()

# 使用示例
def test_factory_method():
    # 根据配置选择具体的工厂
    config = "dog"  # 可以从配置文件读取
    
    if config == "dog":
        keeper = DogKeeper()
    else:
        keeper = CatKeeper()
    
    result = keeper.care_for_animal()
    print(result)

# 演示开闭原则的优势
def demonstrate_ocp_advantage():
    """
    演示如何扩展而不修改现有代码
    添加新动物类型时，只需要添加新的具体产品和创建者
    """
    print("\n=== 演示开闭原则优势 ===")
    
    # 添加新动物：鸟
    class Bird(Animal):
        def speak(self):
            return "叽叽！"
        
        def eat(self):
            return "鸟在吃谷物"
    
    # 添加新的创建者：鸟饲养员
    class BirdKeeper(AnimalKeeper):
        def create_animal(self) -> Animal:
            return Bird()
    
    # 使用新的动物类型，无需修改现有代码
    bird_keeper = BirdKeeper()
    result = bird_keeper.care_for_animal()
    print(f"新动物类型: {result}")

if __name__ == "__main__":
    test_factory_method()
    demonstrate_ocp_advantage()