from abc import ABC, abstractmethod

class Handler(ABC):
    def __init__(self, handler):
        self._successor: Handler = handler

    @abstractmethod
    def foo(self, text: str):
        pass

class ConcreteHandlerA(Handler):
    def __init__(self, handler):
        Handler.__init__(self, handler)

    def foo(self, text: str):
        print(f"This is handler {text}!")
        self._successor.foo('B')

class ConcreteHandlerB(Handler):
    def __init__(self, handler):
        Handler.__init__(self, handler)

    def foo(self, text: str):
        print(f"This is handler {text}!")

if __name__ == '__main__':
    concrete_handler_B: Handler = ConcreteHandlerB(None)
    concrete_handler_A: Handler = ConcreteHandlerA(concrete_handler_B)
    concrete_handler_A.foo('A')