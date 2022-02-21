# 1. Create a custom integer class. The class should have one instance attribute as its value. Now, your class must
# satisfy the following criteria:
#    a) we can use Python arithmetic operators to add, subtract, multiply and divide the values.
#    b) create another class called Inf. For the sake of consistency, this class may inherit from int class.
#    c) if we divide by zero, we don't get an exception. Instead, we get inf, which was implemented in our previous step
#    d) when we print our class, we want it to be represented as nicely as possible. As our class represents an integer
#    number, we want to see the value when we print it or cast it to a string.
#    e) as with every number, we want to be able to compare our integer instances using the logical operators.
#    Implement those as well.
#    f) finally, there is one thing that all Python objects have in common. If we neglect 0, '', None, False etc., then
# #    every object holds a value of True when casted to bool. We want our Integer to behave as a normal integer in this
# #    sense. When we cast an Integer to bool, we must get False, if the value of our object is 0. True otherwise.


class Integer(object):

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f'New integer value is {self.value}'

    def __add__(self, other):  # +
        self.check_type(other)
        return Integer(self.value + other.value)

    def __sub__(self, other):  # -
        self.check_type(other)
        return Integer(self.value - other.value)

    def __mul__(self, other):  # *
        self.check_type(other)
        return Integer(self.value * other.value)

    def __truediv__(self, other):  # /
        self.check_type(other)
        if other.value == 0:
            return Inf(other.value)
        return Integer(self.value / other.value)

    def __lt__(self, other):  # <
        self.check_type(other)
        return self.value < other.value

    def __le__(self, other):  # <=
        self.check_type(other)
        return self.value <= other.value

    def __eq__(self, other):  # ==
        self.check_type(other)
        return self.value == other.value

    def __ne__(self, other):  # !=
        self.check_type(other)
        return self.value != other.value

    def __ge__(self, other):  # >=
        self.check_type(other)
        return self.value >= other.value

    def __bool__(self):
        return True if self.value != 0 else False

    def check_type(self, other):
        if not isinstance(other, Integer):
            raise TypeError(f'Both operands should be of type {self.__class__}')


class Inf(Integer):

    def __init__(self, value):
        super().__init__(value)
        self.value = value

    def __str__(self):
        return 'Inf ...'

#
# integer1 = Integer(12)
# integer2 = Integer(4)
# integer3 = Integer(0)
#
# print(integer1 + integer2)
# print(integer1 - integer2)
# print(integer1 * integer2)
# print(integer1 / integer2)
# print(integer1 / integer3)
#
# # check logical operators
# print(integer1 < integer3)
# print(integer1 >= integer3)
# print(integer1 == integer2)
# print(integer2 != integer3)
# print(integer2 >= integer3)
#
#
# print(bool(integer3))


# 2. Create a Color class. This will hold 3 instance variables, red, green, blue (RGB).
# Each parameter (red, green, and blue) defines the intensity of the color as an integer between 0 and 255. We want to be able to get new
# colors if we add instances of the color class. I'm not sure how much sense it will make to also subtract the colors,
# but lets do it for fun! In summary, we can add 2 or more colors and get a new color object with added RGB values
# (don't forget about the boundaries!), subtract them to get a new color object with subtracted values. When printed,
# we want to have a nice representation of our color (maybe even the color itself?). One more fun thing! As colors
# are quite often represented in hexadecimals, lets override the corresponding function such that when hex() is called
# on our class, we get the hex color code for our color.


class Color:

    def __init__(self, red, green, blue):
        # self.red = self.check_value(red)
        # self.green = self.check_value(green)
        # self.blue = self.check_value(blue)
        self.red = red
        self.green = green
        self.blue = blue

    def __str__(self):
        return f'Your color is RGB({self.red}, {self.green}, {self.blue})'

    def __index__(self):  # index-@ veradardznum e class-i integer nerkayacum@
        return 256 * 256 * self.red + 256 * self.green + self.blue

    def __add__(self, other):  # +
        self.check_type(other)
        self.red = self.red + other.red if self.red + other.red <= 255 else 255
        self.green = self.green + other.green if self.green + other.green <= 255 else 255
        self.blue = self.blue + other.blue if self.blue + other.blue <= 255 else 255
        return Color(self.red, self.green, self.blue)

    def __sub__(self, other):  # -
        self.check_type(other)
        print(self.red)
        print(other.red)
        self.red = self.red - other.red if self.red - other.red >= 0 else 0
        self.green = self.green - other.green if self.green - other.green >= 0 else 0
        self.blue = self.blue - other.blue if self.blue - other.blue >= 0 else 0
        return Color(self.red, self.green, self.blue)

    @staticmethod
    def check_value(value):
        if 0 <= value <= 255 and isinstance(value, int):
            return value
        else:
            raise ValueError(f'Your setting value need to be as an integer between 0 and 255')

    def check_type(self, other):
        if not isinstance(other, Color):
            raise TypeError(f'Your object type need to be {self.__class__}, but it is {type(other)}')


color1 = Color(12, 128, 0)
color2 = Color(123, 123, 123)
colorAdd = color1 + color2
print(colorAdd)

# color1 = Color(20, 128, 0)
# color2 = Color(20, 128, 0)
colorSub = color1 - color2
print(colorSub)

print(hex(colorAdd))
print(hex(colorSub))
