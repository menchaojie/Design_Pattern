class SingletonMeta(type):
    """单例元类"""
    _instances = {}
    
    def __call__(cls, *args, **kwargs):
        # 如果类还没有实例，就创建新实例
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class MyClass(metaclass=SingletonMeta):
    def __init__(self, name="默认"):
        self.name = name
        print(f"初始化 MyClass，名称: {name}")

# 测试
print("=== 简单单例测试 ===")

# 第一次创建
obj1 = MyClass("第一个")

# 第二次创建（应该返回同一个实例）
obj2 = MyClass("第二个")

# 验证
print(f"obj1 名称: {obj1.name}")
print(f"obj2 名称: {obj2.name}")
print(f"是同一个对象吗？ {obj1 is obj2}")

# 修改一个对象会影响另一个
obj1.name = "修改后的名称"
print(f"修改后 obj2 名称: {obj2.name}")