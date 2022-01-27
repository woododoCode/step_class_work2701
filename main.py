class Human:
    def __init__(self, **kwargs):
        self.__name = kwargs.get('name')
        self.__age = kwargs.get('age')
        self.__height = kwargs.get('height')

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def update_info(self, **kwargs):
        self.__name = kwargs.get('name') if kwargs.get('name') else self.__name
        self.__age = kwargs.get('age') if kwargs.get('age') else self.__age
        self.__height = kwargs.get('height') if kwargs.get('height') else self.__height

    def __repr__(self):
        return f"Name: {self.__name}, age: {self.__age}, height: {self.__height}"


human = Human(age=15, name='Mike', height=135)
d = {"age": 15, "name": 'Mike'}
print(human)
human.update_info(name="Lisa")
print(human)
