## 观察者模式

设计核心：主题(subject)持有观察者(observer)对象引用， 当主题状态改变时， 会通知所有观察者对象。

### property 装饰器

property 装饰器可以将方法转换为属性， 可以像属性一样访问和赋值。

```python
class Person:
    def __init__(self, age: int = 0):
        self.__age = age

    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("年龄不能为负数")
        self.__age = value
```

可以参考 `02_attribute_operation.py` 中的代码。

### 内存泄漏问题

问题场景 ：

1. 投资者对象被创建并注册到股票市场
2. 投资者对象在其他地方不再被使用
3. 但由于股票市场持有对投资者的 强引用 ，垃圾回收器无法回收这个投资者对象
4. 导致内存泄漏

使用若引用：

```python
    class StockMarket(Subject):
        def __init__(self):
            self._observers: List[Observer] = []  # 强引用

    import weakref
    class SafeSubject(Subject):
        def __init__(self):
            self._observers = weakref.WeakSet()  # 弱引用集合
```

### 异步通知

```python
import asyncio

class AsyncObserver(ABC):
    @abstractmethod
    async def update_async(self, message: str):
        pass

class AsyncSubject:
    async def notify_observers_async(self):
        tasks = [observer.update_async(self._message) 
                for observer in self._observers]
        await asyncio.gather(*tasks)
```

### 错误处理

```python
def safe_notify(self):
    for observer in self._observers.copy():  # 使用副本避免修改问题
        try:
            observer.update(self._message)
        except Exception as e:
            print(f"观察者 {observer} 更新失败: {e}")
```