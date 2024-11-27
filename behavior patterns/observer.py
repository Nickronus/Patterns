from abc import ABC, abstractmethod

class IObserver(ABC):
    @abstractmethod
    def update():
        pass 

class IObservable(ABC):
    @abstractmethod
    def add_observer(observer: IObserver, observer_name: str):
        pass

    @abstractmethod
    def notify_observers():
        pass

    @abstractmethod
    def remove_observer(observer_name: str):
        pass

class Observer(IObserver):
    def __init__(self, observer_name: str):
        self.name = observer_name

    def update(self):
        print(f"Observer {self.name} updated!")

class Observable(IObservable):
    def __init__(self):
        self.__observers: list[IObserver] = []

    def add_observer(self, observer: IObserver):
        self.__observers.append(observer)
        print(f"Observer {observer.name} added!")

    def notify_observers(self):
        for observer in self.__observers:
            observer.update()

    def remove_observer(self, observer_name: str):
        observer_for_delete = None
        for observer in self.__observers:
            if observer.name == observer_name:
                observer_for_delete = observer

        if observer_for_delete:
            self.__observers.remove(observer)
            print(f"Observer {observer_name} removed!")

if __name__ == '__main__':
    observer: IObserver = Observer('my good observer')
    observable: IObservable = Observable()
    observable.add_observer(observer)
    observable.notify_observers()
    observable.remove_observer('my good observer')