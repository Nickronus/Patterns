from abc import ABC, abstractmethod

class ICommand(ABC):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass

class Receiver():
    def __init__(self, name: str):
        self.__name = name
        
    def execute_command(self):
        print(f'Receiver {self.__name} execute command!')

    def undo_command(self):
        print(f'Receiver {self.__name} undo command!')

class CommandToReceiver(ICommand):
    def __init__(self, receiver: Receiver):
        self.__receiver = receiver

    def execute(self):
        self.__receiver.execute_command()

    def undo(self):
        self.__receiver.undo_command()

class Invoker():
    def __init__(self, command: ICommand):
        self.__command = command

    def set_command(self, command: ICommand):
        self.__command = command

    def send_execute_command(self):
        self.__command.execute()

    def send_undo_command(self):
        self.__command.undo()

if __name__ == '__main__':
    receiver = Receiver('my good receiver')
    good_receiver_command = CommandToReceiver(receiver)
    invoker = Invoker(good_receiver_command)    
    invoker.send_execute_command()
    invoker.send_undo_command()

    receiver = Receiver('my bad receiver')
    bad_receiver_command = CommandToReceiver(receiver)
    invoker.set_command(bad_receiver_command)
    invoker.send_execute_command()
    invoker.send_undo_command()