class Borg:
    """Borg模式基类 - 所有实例共享状态"""
    _shared_state = {}  # 类变量，所有实例共享

    def __init__(self):
        # 关键：让实例的属性字典指向共享字典
        self.__dict__ = self._shared_state


class YourBorg(Borg):
    """Borg模式的具体实现"""
    
    def __init__(self, state=None):
        super().__init__()  # 调用父类初始化，设置共享字典
        
        if state:
            self.state = state  # 设置状态（实际修改共享字典）
        else:
            # 如果是第一个实例，初始化默认状态
            if not hasattr(self, "state"):
                self.state = "Init"

    def __str__(self):
        return self.state


# 简单演示
if __name__ == "__main__":
    print("=== Borg模式演示 ===")
    
    # 创建第一个实例
    borg1 = YourBorg()
    print(f"borg1创建时的状态: {borg1}")
    
    # 创建第二个实例
    borg2 = YourBorg()
    print(f"borg2创建时的状态: {borg2}")
    print(f"两个实例状态相同: {borg1.state == borg2.state}")
    
    # 修改第二个实例的状态
    print("\n--- 修改borg2的状态为'Running' ---")
    borg2.state = "Running"
    print(f"borg1的状态: {borg1}")
    print(f"borg2的状态: {borg2}")
    print(f"状态自动同步!")
    
    # 验证实例是不同的对象
    print(f"\n实例是不同的对象: {borg1 is not borg2}")
    print(f"但共享同一个字典: {borg1.__dict__ is borg2.__dict__}")
    
    # 创建第三个实例
    print("\n--- 创建borg3实例 ---")
    borg3 = YourBorg()
    print(f"borg3的状态: {borg3}")
    print(f"自动获得当前共享状态!")
    
    # 创建时指定状态
    print("\n--- 创建borg4并指定状态'Zombie' ---")
    borg4 = YourBorg("Zombie")
    print(f"borg4的状态: {borg4}")
    print(f"borg1的状态: {borg1}")
    print(f"所有实例状态同步更新!")