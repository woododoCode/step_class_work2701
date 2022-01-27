class Human:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def __repr__(self):
        return f"Name: {self.__name}, age: {self.__age}"


human = Human('Mike', 15)
print(human.get_name())
human.set_name('Lis')
print(human.get_name())
