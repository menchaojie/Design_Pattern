class Meta(type):
    def __call__(cls, *args, **kwargs):
        print("Meta.__call__ start")
        obj = super().__call__(*args, **kwargs)
        print("Meta.__call__ end")
        return obj

class TargetClass(metaclass=Meta):
    def __new__(cls):
        print("TargetClass.__new__")
        return super().__new__(cls)

    def __init__(self):
        print("TargetClass.__init__")

a = TargetClass()
