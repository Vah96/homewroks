# 1. Create Animal class with three methods - make_noise(), walk() and fly(). The methods shall print what the animal is
# doing. Then, create a Bird and Feline classes which inherit from Animal. Override the superclass methods, so that
# a cat warns us that it can't fly and the bird only wants to fly as it is too lazy to walk.
# Ստեղծել Animal կլասս, որը կունենա երեք մեթոդ՝ make_noise(), walk() և fly()։ Այդ մեթոդները պետք է տպեն, թե ինչ է անում
# կենդանին։ Ապա ստեղծել Bird և Feline կլասեր, որոնք ժառանգում են Animal-ից։ Animal-ի մեթոդները իմպլեմենտացրեք
# այդ կլասերի մեջ, այնպես, որ եթե կատուն փորձի թռչել, կոնսոլում տպվի, որ նա չի կարող թռչել։ Իսկ եթե թռչնի վրա
# կիրառենք walk() մեթոդը, նա ասի, որ ալարում է և միայն կարող է թռչել։

import abc

# qani vor voreve gortsoxutyun chi arvum Animal class-i methodneri mej, apa ogtagortselov @abc.abstractmethod
# argelum enq voreve instance sarqel Animal class-ic
#
#
# class Animal(abc.ABC):
#     @abc.abstractmethod
#     def make_noise(self):
#         pass
#
#     @abc.abstractmethod
#     def walk(self):
#         pass
#
#     @abc.abstractmethod
#     def fly(self):
#         pass
#
#
# a = Animal()  # print kani TypeError: Can't instantiate abstract class Animal with abstract methods fly, make_noise, walk


class Animal:

    # def make_noise(self):  # ete method-i mej self chenq ogtagortsum apa karox enq ogtagortsel 'static method'
    #     print('making noise')

    @staticmethod
    def make_noise():  # make_noise() darnum e static method 'static method'
        print('making noise')

    def walk(self):
        pass

    def fly(self):
        pass


class Bird(Animal):

    def walk(self):
        print('I am too lazy')

    def fly(self):
        print('I am flying')


class Feline(Animal):

    def walk(self):
        print('I am walking')

    def fly(self):
        print('I can\'t fly. I am only walk')


class Calculator:

    def __init__(self, a, b):
        if type(a) in [int, float] and type(b) in [int, float]:
            self.a = a
            self.b = b
        else:
            raise ValueError("Must be an integer")

    def add(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b

    def mul(self):
        return self.a * self.b

    def divide(self):
        return self.a / self.b


calculator = Calculator(5, 10)
print(calculator.add())
print(calculator.sub())
print(calculator.mul())
print(calculator.divide())


""" 3 """


class Shape(abc.ABC):

    @abc.abstractmethod
    def perimeter(self):
        pass

    @abc.abstractmethod
    def area(self):
        pass


from math import pi
# import math  # nerarum e amboxj math-@


class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def perimeter(self):
        return 2 * pi * self.radius

    def area(self):
        return 2 * pi * self.radius ** 2
