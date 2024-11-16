from abc import ABC, abstractmethod

class AbstractSubject(ABC):
    @abstractmethod
    def request(self):
        pass

class Subject(AbstractSubject):
    def request(self):
        print('This is concrete subject!')

class Proxy(AbstractSubject):
    def __init__(self, subject: AbstractSubject, role: str):
        self.__subject = subject
        self.__role = role

    def request(self):
        if self.__role == 'admin':
            self.__subject.request()

if __name__ == '__main__':
    subject: AbstractSubject = Subject()
    proxy: AbstractSubject = Proxy(subject, 'admin')
    proxy.request()