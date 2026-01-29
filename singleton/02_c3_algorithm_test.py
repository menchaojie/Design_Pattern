#!/usr/bin/env python3
"""
C3算法测试用例
algorithm test case
"""

class C: 
    def __init__(self) -> None:
        super().__init__()
        print("C")

class B(C): 
    def __init__(self) -> None:
        super().__init__()
        print("B")

class A(B): 
    def __init__(self) -> None:
        super().__init__()
        print("A")

class Z: 
    def __init__(self) -> None:
        print("Z")
class Y(Z): 
    def __init__(self) -> None:
        super().__init__()
        print("Y")
class X(B,Y): 
    def __init__(self) -> None:
        super().__init__()  
        print("X")


class D(A,X): pass

# print(f"list1 : {A.__mro__}")
# print(f"list2 : {X.__mro__}")
print("="*40)
print(f"merge [list1, list2] : {D.__mro__}")
print("="*40)
D()
print("="*40)
C()