from abc import ABC, abstractmethod

class IClassA(ABC):
    @abstractmethod
    def foo(self):
        pass

class ClassA(IClassA):
    def foo(self):
        print('Class A!')

class ClassB():
    def moo(self):
        print('Class B!')

class AdapterClassBToClassA(IClassA):
    def __init__(self, class_B: ClassB):
            self.class_B = class_B

    def foo(self):
        self.class_B.moo()

if __name__ == '__main__':
    a: IClassA = ClassA()
    a.foo()

    b: ClassB = ClassB()

    adapter: IClassA = AdapterClassBToClassA(b)
    adapter.foo()