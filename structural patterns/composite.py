from abc import ABC, abstractmethod

class Component(ABC):
    @abstractmethod
    def add_component():
        pass

    @abstractmethod
    def remove_component():
        pass

    @abstractmethod
    def foo():
        pass

class Composite(Component):
    def __init__(self, name: str):
        self.name = name
        self.__children: list[Component] = []

    def add_component(self, component: Component):
        self.__children.append(component)

    def remove_component(self, name: str):
        child_to_remove = None
        for child in self.__children:
            if child.name == name:
                child_to_remove = child
                break

        if child_to_remove:
            self.__children.remove(child_to_remove)

    def foo(self):
        print(f"This is {self.name}!")
        for item in self.__children:
            item.foo()

class Leaf(Component):
    def __init__(self, name: str):
        self.name = name

    def add_component(self, component: Component):
        pass

    def remove_component(self, name: str):
        pass

    def foo(self):
        print(f"This is {self.name}!")

if __name__ == '__main__':
    composite: Composite = Composite('composite')

    leaf: Leaf = Leaf('leaf')
    composite.add_component(leaf)

    root_composite: Composite = Composite('root composite')
    root_composite.add_component(composite)

    root_composite.foo()