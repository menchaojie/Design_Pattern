class PersonTraditional:
    def __init__(self, age: int = 0):
        self._age = age
        
    def get_age(self):
        return self._age
    
    def set_age(self, value):
        if value < 0:
            raise ValueError("年龄不能为负数")
        self._age = value


class PersonModern:
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


if __name__ == "__main__":
    # 使用传统方式
    p = PersonTraditional(2)
    print(p.get_age()) # 获取年龄
    p.set_age(5)      # 设置年龄
    print(p.get_age()) # 获取年龄

    # 使用现代方式
    p = PersonModern(20)
    print(p.age)       # 获取年龄
    p.age = 50       # 像属性一样赋值
    print(p.age)       # 像属性一样读取 
