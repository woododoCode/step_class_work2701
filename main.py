from datetime import date


class Human:
    count = 0

    def __init__(self, *args):
        name, year, height = args
        self.name = name
        self.year = year
        self.height = height
        Human.count += 1

    def update_info(self, **kwargs):
        self.name = kwargs.get('name') if kwargs.get('name') else self.name
        self.year = kwargs.get('age') if kwargs.get('age') else self.year
        self.height = kwargs.get('height') if kwargs.get('height') else self.height

    @classmethod
    def from_birth_year(cls, age):
        if cls.is_adult(age):
            human = cls(age=date.today().year - age)
            return human
        else:
            return

    @staticmethod
    def f_to_c(year):
        Human.count += 1
        if year < 5:
            print('You just a child')
            return False
        else:
            return True

    def __repr__(self):
        return f"Name: {self.name}, year: {self.year}, height: {self.height}"

    def __add__(self, *args):
        res = 0
        for item in args:
            res += item.age
        return res


human = Human(15, 'Mike', 135)
print(f'{human.height=}')
print(f'{human.year=}')
print(f'{human.name=}')
