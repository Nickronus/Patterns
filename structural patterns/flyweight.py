from abc import ABC, abstractmethod

class Flyweight(ABC):
    @abstractmethod
    def operation(self, extrinsic_state: int):
        pass

class ConcreteFlyweightA(Flyweight):
    __intrinsic_state = 'Flyweight A!'

    def operation(self, extrinsic_state: int):
        
        print('Intrisic state: ', self.__intrinsic_state, 'Extrisic state: ', extrinsic_state)

class ConcreteFlyweightB(Flyweight):
    __intrinsic_state = 'Flyweight B!'

    def operation(self, extrinsic_state: int):
        print('Intrisic state: ', self.__intrinsic_state, 'Extrisic state: ', extrinsic_state)

class UnsharedConcreteFlyweight(Flyweight):
#А вот у этой штуки по сути нет внутреннего стстояния (оно зависит от переданного извне значения), поэтому это неразделяеый класс.
#Но, в фабрику таки можно и запихать.
    def operation(self, extrinsic_state: int):
        print('Intrisic state: ', f"NEIN!", 'Extrisic state: ', extrinsic_state)

class FlyweightFactory():
    def __init__(self):
        self.__flyweight: dict[int: Flyweight] = {}

        self.__flyweight.update({'A': ConcreteFlyweightA()})
        self.__flyweight.update({'B': ConcreteFlyweightB()})

    def get_flyweight(self, key: str) -> Flyweight | None:
    # Реализация может быть разной - от возвращения None, если ключа нет в хэше, до...
        if not key in self.__flyweight:
            self.__flyweight.update({key: UnsharedConcreteFlyweight()})

        return self.__flyweight[key]

if __name__ == '__main__':
    flyweight_factory = FlyweightFactory()
    flyweight_factory.get_flyweight('A').operation('Extrisic state for A!')
    flyweight_factory.get_flyweight('N').operation('Extrisic state for N!')
    flyweight_factory.get_flyweight('B').operation('Extrisic state for B!')