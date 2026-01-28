class X: pass
class Y: pass
class Z: pass

# class A(X, Y): pass
class A(X,Y): pass
# class B(Y, Z): pass
class B(X,Y): pass
# class C(A, B): pass  # 多重继承
class C(Z): pass  # 多重继承
class D(A,B,C): pass  # 多重继承，与 C 不同的解析顺序K

class Basic:
    pass

class MyClass(Basic):
    # 第一级缩进：类级别（共享）
    class_var1 = "Class_Var_1"      # ← 所有实例共享
    class_var2 = "Class_Var_2"      # ← 所有实例共享
    
    def method1(self):           # ← 方法定义共享
        return "共享方法1"
    
    def method2(self):           # ← 方法定义共享  
        return "共享方法2"
    
    def __init__(self, name):
        # 第二级缩进：实例级别（不共享）
        self.name = name          # ← 每个实例独立
        self.age = 20             # ← 每个实例独立
        # self.dynamic_var = None
    
    def dynamic_method(self):
        # 第二级缩进：运行时实例级别
        self.dynamic_var = self.name  # ← 每个实例独立

if __name__ == "__main__":
    obj1 = MyClass("Alice")
    obj1.dynamic_method()
    obj1.test_name = "Alice_Test"
    
    obj2 = MyClass("Bob")

    print(f"obj1.__dict__: {obj1.__dict__}")
    print(f"obj2.__dict__: {obj2.__dict__}")
    print(f"obj1.test_name: {obj1.test_name}")
    # print(f"obj2.test_name: {obj2.test_name}") # error: 'MyClass' object has no attribute 'test_name'
    print("=== instance attribute is private ======")
    print(f"obj1.name: {obj1.name},but, obj2.name: {obj2.name}")
    print(f"obj1.dynamic_var: {obj1.dynamic_var}")
    # print(f"obj1.dynamic_var: {obj1.dynamic_var},but, obj2.dynamic_var: {obj2.dynamic_var}") # error: 'MyClass' object has no attribute 'dynamic_var'
    print("=== class attribute is shared ======")
    print(f"obj1.class_var1: '{obj1.class_var1}', and obj2.class_var1: '{obj2.class_var1}'")
    print("===MRO 是 Method Resolution Order 的缩写，意思是 方法解析顺序 ====")
    print(f"obj1.__mro__: {type(obj1).__mro__}")
    print(f"obj2.__mro__: {type(obj2).__mro__}")
    
    print(D.__mro__)
    # C → A → X → B → Y → Z → object