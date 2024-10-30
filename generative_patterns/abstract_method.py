from abc import ABC, abstractmethod

class AbstractProduct(ABC):
    @abstractmethod
    def foo(self):
        pass

class ProductA(AbstractProduct):
    def foo(self):
        print('ProductA')

class ProductB(AbstractProduct):
    def foo(self):
        print('ProductB')

class AbstractFactory(ABC):
    @abstractmethod
    def factory_method(self) -> AbstractProduct:
        pass

class FactoryA():
    def factory_method(self) -> AbstractProduct:
        return ProductA()

class FactoryB(AbstractFactory):
    def factory_method(self) -> AbstractProduct:
        return ProductB()

if __name__ == '__main__':
    factory: AbstractFactory = FactoryA()
    product: AbstractProduct = factory.factory_method()
    product.foo()