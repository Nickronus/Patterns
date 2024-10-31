from abc import ABC, abstractmethod

class AbstractComponent(ABC):
    @abstractmethod
    def foo(self):
        pass

class Component(AbstractComponent):
    def foo(self):
        print('Component')

class AbstractDecorator(AbstractComponent, ABC):
    def __init__(self, component: AbstractComponent):
        self.component = component

class DecoratorA(AbstractDecorator):
    def __init__(self, component: AbstractComponent):
        AbstractDecorator.__init__(self, component)

    def moo(self):
        print(' + Decorator A')

    def foo(self):
        self.component.foo()
        self.moo()

class DecoratorB(AbstractDecorator):
    def __init__(self, component: AbstractComponent):
        AbstractDecorator.__init__(self, component)

    def boo(self):
        print(' + Decorator B')

    def foo(self):
        self.component.foo()
        self.boo()

if __name__ == '__main__':
    component: AbstractComponent = Component()
    component.foo()

    decorated_component_A: AbstractComponent = DecoratorA(component)
    decorated_component_A.foo()

    decorated_component_B: AbstractComponent = DecoratorB(decorated_component_A)
    decorated_component_B.foo()