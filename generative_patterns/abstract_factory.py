from abc import ABC, abstractmethod

class AbstractProductA(ABC):
    @abstractmethod
    def foo(self):
        pass

class AbstractProductB(ABC):
    @abstractmethod
    def moo(self):
        pass

class AbstractFactory(ABC):
    @abstractmethod
    def create_product_A(self) -> AbstractProductA:
        pass

    @abstractmethod
    def create_product_B(self) -> AbstractProductB:
        pass

class ProductA1(AbstractProductA):
    def foo(self):
        print('ProductA1')

class ProductA2(AbstractProductA):
    def foo(self):
        print('ProductA2')

class ProductB1(AbstractProductB):
    def moo(self):
        print('ProductB1')

class ProductB2(AbstractProductB):
    def moo(self):
        print('ProductB2')

class Factory1(AbstractFactory):
    def create_product_A(self) -> AbstractProductA:
        return ProductA1()

    def create_product_B(self) -> AbstractProductB:
        return ProductB1

class Factory2(AbstractFactory):
    def create_product_A(self) -> AbstractProductA:
        return ProductA2

    def create_product_B(self) -> AbstractProductB:
        return ProductB2

class Client():
    def __init__(self, abstract_factory: AbstractFactory):
        self.product_A = abstract_factory.create_product_A()
        self.product_B = abstract_factory.create_product_B()

if __name__ == '__main__':
    factory_1 = Factory1()
    client = Client(factory_1)
    client.product_A.foo()