class Singleton:
    """在new方法中实现单例模式"""
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.counter = 0  # 用于测试的计数器
            print("单例实例已创建")
        return cls._instance
    
    def increment(self):
        """增加计数器"""
        self.counter += 1
        return self.counter


# 测试单例模式
if __name__ == "__main__":
    print("=== 单例模式测试 ===")
    
    # 创建第一个实例
    s1 = Singleton()
    print(f"s1的计数器: {s1.counter}")
    
    # 增加计数器
    s1.increment()
    print(f"s1增加后计数器: {s1.counter}")
    
    # 创建第二个实例（应该是同一个对象）
    s2 = Singleton()
    print(f"s2的计数器: {s2.counter}")
    
    # 验证是否是同一个对象
    print(f"s1和s2是同一个对象: {s1 is s2}")
    print(f"s1的内存地址: {id(s1)}")
    print(f"s2的内存地址: {id(s2)}")
    
    # 通过s2修改状态
    s2.increment()
    print(f"通过s2增加后，s1的计数器: {s1.counter}")
    print(f"通过s2增加后，s2的计数器: {s2.counter}")
    
    # 创建第三个实例
    s3 = Singleton()
    print(f"s3的计数器: {s3.counter}")
    
    print("\n=== 单例模式验证完成 ===")
    print("所有实例都是同一个对象，状态共享!")