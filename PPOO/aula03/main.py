from random import randint

class Pessoa:
    year = 2019

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def getBirthYear(self):
        print(self.year - self.age)

    @classmethod
    def perBirthYear(cls, name, BirthYear):
        age = cls.year - BirthYear
        return cls(name, age)

    @staticmethod
    def getId():
        rand = randint(10000, 19999)
        return rand

p1 = Pessoa.perBirthYear('Matheus', 20)

print(p1)
print(p1.name, p1.age)
p1.getBirthYear()
print(Pessoa.getId())

print('-' * 50)

p2 = Pessoa('Samantha', 24)

print(p2)
print(p2.name, p2.age)
p2.getBirthYear()