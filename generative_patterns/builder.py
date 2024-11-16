from abc import ABC, abstractmethod

class Product():
    def __init__(self):
        self.__parts: list[str] = []

    def add_part(self, part: str):
        self.__parts.append(part)

    def print_parts(self):
        print(self.__parts)

class AbstractBuilder():
    def __init__(self):
        self._product = Product()

    @abstractmethod
    def build_part_A(self):
        pass

    @abstractmethod
    def build_part_B(self):
        pass

    @abstractmethod
    def build_part_C(self):
        pass

    @abstractmethod
    def get_product(self) -> Product:
        return self._product

class Director():
    def get_product(self, builder: AbstractBuilder):
        builder.build_part_A()
        builder.build_part_B()
        builder.build_part_C()
        return builder.get_product()

class BuilderAC(AbstractBuilder):
    def __init__(self):
        super().__init__()

    def build_part_A(self):
        self._product.add_part('Part A')

    def build_part_B(self):
        pass

    def build_part_C(self):
        self._product.add_part('Part C')

class BuilderAB(AbstractBuilder):
    def __init__(self):
        super().__init__()

    def build_part_A(self):
        self._product.add_part('Part A')

    def build_part_B(self):
        self._product.add_part('Part B')

    def build_part_C(self):
        pass

if __name__ == '__main__':
    builder_AC: AbstractBuilder = BuilderAC()
    director: Director = Director()

    product_AC: Product = director.get_product(builder_AC)
    product_AC.print_parts()

    builder_AB: AbstractBuilder = BuilderAB()
    product_AB: Product = director.get_product(builder_AB)
    product_AB.print_parts()
    