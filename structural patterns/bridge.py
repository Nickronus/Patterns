from abc import ABC, abstractmethod

class IImplementor(ABC):
    @abstractmethod
    def foo(self):
        pass

class Abstraction(ABC):
    def __init__(self, implementor: IImplementor):
        self._implementor = implementor

    def set_implementor(self, implementor: IImplementor):
        self._implementor = implementor

    @abstractmethod
    def moo(self):
        pass

class ImplementorA(IImplementor):
    def foo(self):
        print('This is implementor A!')

class ImplementorB(IImplementor):
    def foo(self):
        print('This is implementor B!')

class RefinedAbstraction(Abstraction):
    def __init__(self, implementor):
        Abstraction.__init__(self, implementor)

    def moo(self):
        self._implementor.foo()
        print('This is Refined Abstraction!')

if __name__ == '__main__':
    implementor_A: IImplementor = ImplementorA()
    refined_abstraction: Abstraction = RefinedAbstraction(implementor_A)
    refined_abstraction.moo()

    implementor_B: IImplementor = ImplementorB()
    refined_abstraction.set_implementor(implementor_B)
    refined_abstraction.moo()