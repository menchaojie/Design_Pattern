## 简单工厂模式

### 开闭原则
开闭原则 (Open-Closed Principle, OCP) 是面向对象设计的五大原则之一（SOLID原则中的"O"）。

定义 ：软件实体（类、模块、函数等）应该对扩展开放，对修改关闭。

具体含义 ：

- 对扩展开放 ：当需求变化时，可以通过添加新的代码来扩展功能
- 对修改关闭 ：已有的代码不应该被修改，保持稳定性


在简单工厂模式中违反了开闭原则 ：

```python
class AnimalFactory:
    @staticmethod
    def create_animal(animal_type):
        if animal_type == "dog":
            return Dog()
        elif animal_type == "cat":
            return Cat()
        # 如果要添加新动物，必须修改这里的代码
        else:
            raise ValueError(f"未知的动物类型: {animal_type}")
```
问题 ：每次添加新动物（如"bird"），都需要修改 AnimalFactory 类的代码，这违反了开闭原则。

## 工厂方法模式

工厂方法模式有抽象工厂和具体工厂之分，将对象的创建逻辑集中在具体工厂中，而抽象工厂只负责定义对象创建的接口。

```python
# 抽象工厂 + 多个具体工厂
class AnimalKeeper(ABC):          # 抽象工厂
    @abstractmethod
    def create_animal(self): pass
    
    def care_for_animal(self):
        animal = self.create_animal()  # 工厂方法调用
        return animal.speak()

class DogKeeper(AnimalKeeper):    # 具体工厂1
    def create_animal(self): return Dog()

class CatKeeper(AnimalKeeper):    # 具体工厂2  
    def create_animal(self): return Cat()

```

此方法中虽然也有 if-elif 分支，但只是出现在`test_factory_method`这个测试函数中，具体的类，只是做了相似结构的描述，不同对象具有不同行为是隐藏在结构中的，不是靠if-else来实现的。 在`demonstrate_ocp_advantage`中，我们可以看到，当我们添加新的动物类型时，不需要修改原来的代码，只需要添加新的具体工厂类即可。

从中可以看出，简单工厂模式将对象创建的逻辑集中在了工厂类中，而工厂方法模式使用继承和多态的机制，抽象类描述对象的使用，将对象的创建延迟到了子类中，从而达到创建和使用的分离。

二者的区别可以见下表：

| 方面 | 简单工厂模式 | 工厂方法模式 |
|------|-------------|-------------|
| **工厂数量** | 1个工厂类 | 1个抽象工厂 + N个具体工厂 |
| **开闭原则** | 违反 | 符合 |
| **扩展方式** | 修改工厂类 | 添加新具体工厂类 |
| **复杂度** | 简单 | 较高 |
| **适用场景** | 产品稳定、变化少 | 产品多变、需要灵活扩展 |

## 抽象工厂模式

工厂方法模式架构

```sh
AnimalKeeper(抽象)
    ├── DogKeeper → Dog
    ├── CatKeeper → Cat
    └── BirdKeeper → Bird
```

抽象工厂模式架构

```sh
PetFactory(抽象)
    ├── DogPetFactory → Dog + DogFood + DogToy
    ├── CatPetFactory → Cat + CatFood + CatToy
    └── BirdPetFactory → Bird + BirdFood + BirdToy
```

工厂方法模式 的核心是"一个工厂创建一个产品"，

抽象工厂模式 的核心是"一个工厂创建一个产品族"。

抽象工厂模式可以看作是工厂方法模式的组合和扩展，用于处理更复杂的对象创建场景