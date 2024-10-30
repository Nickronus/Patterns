class Singleton(object):
  _instance = None

  def __new__(cls, *args, **kwargs):
    if cls._instance is None:
      cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
    return cls._instance

class SingletonClass(Singleton):
    def set_text(self, text: str):
        self.__text = text
    
    def print_text(self):
        print(self.__text)

if __name__ == '__main__':
    singleton_1 = SingletonClass()
    singleton_1.set_text('Singleton!')
    singleton_2 = SingletonClass()
    singleton_2.print_text()