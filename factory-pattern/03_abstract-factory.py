"""
 * @file            factory-pattern/abstract-factory.py
 * @description     test the abstract factory pattern
 * @author          menchaojie <menchaojie@163.com>
 * @createTime      2026-01-27 15:16:25
 * @lastModified    2026-01-27 15:16:25
 * Copyright ©YourCompanyName All rights reserved
"""


from abc import ABC, abstractmethod

# 抽象产品 A - 动物
class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

# 抽象产品 B - 食物
class Food(ABC):
    @abstractmethod
    def get_description(self):
        pass

# 具体产品 A1 - 狗
class Dog(Animal):
    def speak(self):
        return "汪汪！"

# 具体产品 A2 - 猫
class Cat(Animal):
    def speak(self):
        return "喵喵！"

# 具体产品 B1 - 狗粮
class DogFood(Food):
    def get_description(self):
        return "优质狗粮"

# 具体产品 B2 - 猫粮
class CatFood(Food):
    def get_description(self):
        return "优质猫粮"

# 抽象工厂 - 宠物用品工厂
class PetFactory(ABC):
    @abstractmethod
    def create_animal(self) -> Animal:
        pass
    
    @abstractmethod
    def create_food(self) -> Food:
        pass

# 具体工厂 1 - 狗用品工厂
class DogPetFactory(PetFactory):
    def create_animal(self) -> Animal:
        return Dog()
    
    def create_food(self) -> Food:
        return DogFood()

# 具体工厂 2 - 猫用品工厂
class CatPetFactory(PetFactory):
    def create_animal(self) -> Animal:
        return Cat()
    
    def create_food(self) -> Food:
        return CatFood()

# 客户端代码 - 宠物店
class PetShop:
    def __init__(self, factory: PetFactory):
        self.factory = factory
        self.animal = None
        self.food = None
    
    def setup_pet(self):
        self.animal = self.factory.create_animal()
        self.food = self.factory.create_food()
    
    def display_pet_info(self):
        result = []
        if self.animal:
            result.append(f"动物叫声: {self.animal.speak()}")
        if self.food:
            result.append(f"食物描述: {self.food.get_description()}")
        return "\n".join(result)

# 使用示例
def test_abstract_factory():
    # 根据宠物类型选择工厂
    pet_type = "dog"  # 可以从配置读取
    
    if pet_type == "dog":
        factory = DogPetFactory()
    else:
        factory = CatPetFactory()
    
    shop = PetShop(factory)
    shop.setup_pet()
    print(shop.display_pet_info())

# 演示产品族的优势
def demonstrate_product_family():
    """
    演示抽象工厂模式创建产品族的优势
    确保同一工厂创建的产品是兼容的
    """
    print("\n=== 演示产品族兼容性 ===")
    
    # 狗用品工厂创建的产品是兼容的
    dog_factory = DogPetFactory()
    dog_shop = PetShop(dog_factory)
    dog_shop.setup_pet()
    print("狗用品套装:")
    print(dog_shop.display_pet_info())
    
    print("\n猫用品套装:")
    cat_factory = CatPetFactory()
    cat_shop = PetShop(cat_factory)
    cat_shop.setup_pet()
    print(cat_shop.display_pet_info())

if __name__ == "__main__":
    test_abstract_factory()
    demonstrate_product_family()