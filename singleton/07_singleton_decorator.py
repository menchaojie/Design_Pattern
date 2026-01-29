def singleton(cls):
    """
    decorator can decorate not only one class, 
    so the the instance is a dict
    """
    instances = {}
   
    def get_instance(*args, **kwargs):
        # 如果该类还没有实例，则创建新实例
        if cls not in instances:
            # 这一句是装饰器单例的核心逻辑
            # 第一个 cls 是 字典键 （类对象，被装饰的类对象），
            # 第二个 cls 是 构造函数 （创建实例的方法）
            instances[cls] = cls(*args, **kwargs)
            print("实例被创建")
        else:
            print("实例被调用")

        return instances[cls]
   
    return get_instance

@singleton
class ConfigurationManager:
    def __init__(self):
        self.name = "MachineLearning"
        self.rate = 0.01

# 测试代码
print("\n=== 测试装饰器单例 ===")
config1 = ConfigurationManager()
config2 = ConfigurationManager()
# config2 = ConfigurationManager().name
print(f"config1 is {config1}")
print(f"config2 is {config2}")
print(f"config1 rate : {config1.rate}")
print(f"config2 rate : {config2.rate}")
config1.level = 1
print(f"config1 level : {config1.level}")
print(f"config2 level : {config2.level}")
