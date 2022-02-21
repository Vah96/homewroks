# 1. Create Animal class with three methods - make_noise(), walk() and fly(). The methods shall print what the animal is
# doing. Then, create a Bird and Feline classes which inherit from Animal. Override the superclass methods, so that
# a cat warns us that it can't fly and the bird only wants to fly as it is too lazy to walk.
# Ստեղծել Animal կլասս, որը կունենա երեք մեթոդ՝ make_noise(), walk() և fly()։ Այդ մեթոդները պետք է տպեն, թե ինչ է անում
# կենդանին։ Ապա ստեղծել Bird և Feline կլասեր, որոնք ժառանգում են Animal-ից։ Animal-ի մեթոդները իմպլեմենտացրեք
# այդ կլասերի մեջ, այնպես, որ եթե կատուն փորձի թռչել, կոնսոլում տպվի, որ նա չի կարող թռչել։ Իսկ եթե թռչնի վրա
# կիրառենք walk() մեթոդը, նա ասի, որ ալարում է և միայն կարող է թռչել։

#
# class Animal:
#     pass
#
#     def __init__(self, name, age, color, place='USA'):
#         self.name = name
#         self.age = age
#         self.color = color
#         self.place = place
#
#     def make_noise(self):
#         print(f'The {self.name} makes a noise.')
#
#     def walk(self):
#         print(f'Hi, my name is {self.name}.')
#
#     def fly(self):
#         print(f'I fly to {self.place}.')
#
#
# class Bird(Animal):
#     pass
#
#     def __init__(self, name, age, color, place):
#         super().__init__(name, age, color, place)
#
#     def make_noise(self):
#         super().make_noise()
#
#     def walk(self):
#         print(f'I get lazy. I can only fly.')
#
#     def fly(self):
#         super().fly()
#
#
# bird = Bird('Panda', 7, 'Black', 'Mexico')
# bird.make_noise()
# bird.walk()
# bird.fly()
#
#
# class Feline(Animal):
#     pass
#
#     def __init__(self, name, age, color, place=False):
#         super().__init__(name, age, color, place)
#
#     def make_noise(self):
#         super().make_noise()
#
#     def walk(self):
#         super().walk()
#
#     def fly(self):
#         print('I can not fly')
#
#
# feline = Feline('Luna', 10, 'Yellow')
# feline.make_noise()
# feline.walk()
# feline.fly()
#
# print('\n     Exercise 2 \n')

# 2. Create a calculator class. It will have 2 numerical instance attributes. Then declare 4 methods called add, sub,
# mult, div to respectively add, subtract, multiply and divide the attributes.
# Ստեղծել կալկուլատորի կլաս։ Այն պետք է ունենա երկու instance attribute։ Ապա ստեղծել չորս մեթոդ՝ add, sub,
# mult, div, որոնք համապատասխանաբար կգումարեն, կհանեն, կբազմապատկեն և կբաժանեն այդ ատրիբուտները։


class Calculator:

    def __init__(self, first_value, second_value):
        first_value_type = type(first_value)
        if first_value_type != int and first_value_type != float:
            raise TypeError(f'"{first_value}" is not integer or float')
        first_second_value = type(second_value)
        if first_second_value != int and first_second_value != float:
            raise TypeError(f'"{second_value}" is not integer or float')
        self.first_value = first_value
        self.second_value = second_value

    def add(self):
        return self.first_value + self.second_value

    def sub(self):
        return self.first_value - self.second_value

    def mul(self):
        return round(self.first_value * self.second_value, 8)

    def div(self):
        if self.second_value == 0:
            raise ZeroDivisionError(f'The divisor can not take a value of "{self.second_value}"')
        return round(self.first_value / self.second_value, 8)


calculator = Calculator(10, 4)
print(calculator.add())
print(calculator.sub())
print(calculator.mul
      ())
print(calculator.div())

print('\n     Exercise 3 \n')

# 3. Create a class called Shape. Define methods to calculate the shape's perimeter and the area.
# Ստեղծել Shape անունով կլաս։ Սահմանել մեթոդներ, սակայն չիմպլեմենտացնել (մեթոդի մեջ պարզապես գրել pass) երկու մեթոդ,
# դրանք անվանելով perimeter և area։


class Shape:

    def perimeter(self):
        pass

    def area(self):
        pass


print('\n     Exercise 4 \n')

# 4. Create a Circle class which will inherit from Shape. Implement the constructor and superclass methods to correctly
# calculate the perimeter and the area of the circle.
# Ստեղծել Circle կլաս, որը կժառանգի Shape-ից։ Իմպլեմենտ արեք կոնստրուկտորը (շրջանագծի դեպքում կունենանք մեկ instance
# attribute` շառավիղը) և Shape-ի երկու մեթոդներն այնպես, որ Circle տիպի օբյեկտի վրա կիրառենք perimeter-ը, կստանանք
# շրջանագծի երկարությունը, իսկ area-ն կիրառելու դեպքում՝ մակերեսը։


class Circle(Shape):

    def __init__(self, radius):
        type_radius = type(radius)
        if (type_radius == float or type_radius == int) and radius > 0:
            self.radius = radius
        else:
            raise TypeError(f'The circle radius can not take a value of "{radius}"')

    def perimeter(self):
        return round(2 * 3.14 * self.radius, 2)

    def area(self):
        return round(3.14 * self.radius ** 2, 2)


circle = Circle(10)
print(circle.perimeter())
print(circle.area())


print('\n     Exercise 5 \n')

# 5. Create a Rectangle class which will inherit from Shape. Implement the constructor and superclass methods to
# correctly calculate the perimeter and the area of the circle.
# Ստեղծել Rectangle կլաս, որը կժառանգի Shape-ից։ Իմպլեմենտ արեք կոնստրուկտորը և Shape-ի երկու մեթոդները ուղղանկյան համար


class Rectangle(Shape):

    def __init__(self, width, height):
        type_width = type(width)
        if (type_width != int and type_width != float) or width <= 0:
            raise TypeError(f'The width of the rectangle can not take a value of "{width}"')
        self.width = width
        type_height = type(height)
        if (type_height != int and type_height != float) or height <= 0:
            raise TypeError(f'The height of the rectangle can not take a value of "{height}"')
        self.height = height

    def perimeter(self):
        return round(2 * (self.width + self.height), 2)

    def area(self):
        return round(self.width * self.height, 2)


rectangle = Rectangle(5.5, 5.5)
print(rectangle.perimeter())
print(rectangle.area())

print('\n     Exercise 6 \n')

# 6. Create a Triangle class which will inherit from Shape. Implement the constructor and superclass methods to
# correctly calculate the perimeter and the area of the circle. Note, that you must check whether a triangle with the
# given lengths can exist.
# Ստեղծել Triangle կլաս, որը կժառանգի Shape-ից։ Իմպլեմենտ արեք կոնստրուկտորը և Shape-ի երկու մեթոդները եռանկյան համար։
# Եռանկյուն օբյեկտը ստեղծելուց անպայման ստուգել, թե արդյո՞ք տրված կողմերով եռանկյուն կարող է գոյություն ունենալ։


class Triangle(Shape):

    def __init__(self, side1, side2, side3):
        type_side1 = type(side1)
        if type_side1 != int and type_side1 != float:
            raise TypeError(f'The side of the triangle can not take a value of "{side1}"')
        type_side2 = type(side2)
        if type_side2 != int and type_side2 != float:
            raise TypeError(f'The side of the triangle can not take a value of "{side1}"')
        type_side3 = type(side3)
        if type_side3 != int and type_side3 != float:
            raise TypeError(f'The side of the triangle can not take a value of "{side1}"')
        if side1 + side2 < side3 or side1 + side3 < side2 or side2 + side3 < side1:
            raise ValueError('The sum of two sides of the triangle must be greater than the third side')

        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def perimeter(self):
        return round(self.side1 + self.side2 + self.side3, 2)

    def area(self):
        p = self.perimeter() / 2
        return round((p * ((p-self.side1) * (p-self.side2) * (p-self.side3))) ** (1/2), 2)


triangle = Triangle(3, 4, 5)
print(triangle.perimeter())
print(triangle.area())

print('\n     Exercise 7 \n')


# 7. a) Create a Vehicle class. The class should have the following instance attributes: name, mileage (defaults to 0),
#    condition, price, max_speed, current_speed and engine_on (defaults to False). It should also have
#    unimplemented methods called start_engine, accelerate (takes a number as an argument), stop.
#    b) Create 2 classes called ElectricVehicle and PetrolVehicle. These classes inherit from the Vehicle class.
#    ElectricVehicle should have the following instance attributes: driving_range, charging_time. PetrolVehicle has the
#    following instance attributes: engine (the volume in litres), transmission, num_of_gears, current_gear. Of course,
#    these classes should call the parent class constructor in their constructor.
#    c) Implement the methods from Vehicle class in each of the child classes accordingly. start_engine should notify us
#    that the engine is on and change the engine_on attribute to True. accelerate method should accelerate the car
#    with the amount of its acceleration attribute and accordingly change the velocity of the car. stop method reduces
#    the speed to 0 and stops the engine. You should also do some checks, e.g. the speed can't be more than max_speed
#    of the car, the car can't start with its engine off etc.
#    d) For the PetrolCar, you should be able to change the transmission gears as well. If the transmission is manual,
#    you should increase the current_gear as the speed increases (current_gear can't be more than the number_of_gears).
#    e) Finally, create some petrol and electric vehicle objects and test your methods.
#
#    a) Ստեղծել Vehicle կլաս։ Կլասը պետք է ունենա հետևյալ instance attribute-ները - name, mileage (նախնական 0 է),
#    condition, price, max_speed, current_speed and engine_on (նախնական False է)։ Կլասը պետք է ունենա նաև երեք
#    չիմպլեմենտացված մեթոդ՝ start_engine, accelerate (ունի մեկ արգումենտ), stop.
#    b) Ստեղծել երկու կլաս՝ ElectricVehicle և PetrolVehicle։ Այս կլասերը ժառանգում են Vehicle—ից։ Էլեկտրական մեքենան
#    պետք է ունենա հետևյալ ատրիբուտները - driving_range, charging_time։ Իսկ վառելիքայինը՝ engine (ծավալը լիտրերով),
#    transmission, num_of_gears, current_gear։ Այս կլասերը պետք է նաև կանչեն Vehicle-ի __init__-ը (super()-ի միջոցով):
#    c) Իմպլեմենտ անել Vehicle-ից ժառանգված բոլոր մեթոդները։ start_engine-ը պետք է զգուշացնի, որ շարժիչը միացված է և
#    engine_on ատրիբուտը դարձնի True. accelerate-ը պետք է բարձրացնի մեքենայի արագությունը, իսկ stop-ը պետք է
#    արագությունն իջեցնի 0-ի և անջատի շարժիչը։ Պետք է նաև կատարել որոշակի վալիդացիա։ Օրինակ՝ արագութոյւնը չի կարող
#    գերազանցել max_speed-ը, մեքենան չի կարող արագանալ, եթե դրա շարժիչը անջատված է և այլն։
#    d) Վառելիքային մեքենայի համար պետք է նաև ներառել որոշակի տրամաբանություն փոխանցման տուփի հետ կապված։ Եթե այն
#    մեխանիկական է, կախված արագությունից պետք է փոխել current_gear-ը (current_gear-ը չի կարող գերազանգել
#    number_of_gears-ը):
#    e) Վերջապես ստեղծել մի քանի էլեկտրական և վառելիքային մեքենա օբյեկտներ և թեստավորել բոլոր մեթոդները։


class Vehicle:

    # name, condition, price, max_Speed and current_speed is positional arguments

    def __init__(self, name, condition, price, max_speed, current_speed, mileage=0, engine_on=False):
        self.name = name
        self.condition = condition
        self.price = price
        self.max_speed = max_speed
        self.current_speed = current_speed
        self.mileage = mileage
        self.engine_on = engine_on

    def start_engine(self):
        self.engine_on = True
        print(f'{self.name} engine is on...')

    def accelerate(self, value):
        if self.engine_on is False:
            print(f'You can not increase the speed of the car "{self.name}" because the engine is off')
        else:
            if self.current_speed + value <= self.max_speed:
                self.current_speed += value
                print(f'Your current speed {self.current_speed}')
            else:
                self.current_speed = self.max_speed
                print(f'The maximum speed of your car "{self.name}" is "{self.current_speed}" and you are now '
                      f'driving at maximum speed')

    def stop(self):
        self.engine_on = False
        self.current_speed = 0
        print('You are stop. You can go down...')


class ElectricVehicle(Vehicle):

    def __init__(self, name, condition, price, max_speed, current_speed, driving_range, charging_time, mileage=0,
                 engine_on=False):
        super().__init__(name, condition, price, max_speed, current_speed, mileage, engine_on)
        self.driving_range = driving_range
        self.charging_time = charging_time

    def start_engine(self):
        super().start_engine()

    def accelerate(self, value):
        super().accelerate(value)

    def stop(self):
        super().stop()


electricVehicle = ElectricVehicle('BMW', 'new', 15000, 260, 0, 50, 4)
electricVehicle.start_engine()
electricVehicle.accelerate(10)
electricVehicle.accelerate(30)
electricVehicle.accelerate(40)
electricVehicle.accelerate(50)
electricVehicle.accelerate(60)
electricVehicle.accelerate(70)
electricVehicle.accelerate(10)
electricVehicle.stop()
electricVehicle.accelerate(30)


class GearBox(Exception):
    pass


class PetrolVehicle(Vehicle):

    each_gear_speed = 0

    def __init__(self, name, condition, price, max_speed, current_speed, engine, transmission, num_of_gears,
                 current_gear=0, mileage=0, engine_on=False):
        super().__init__(name, condition, price, max_speed, current_speed, mileage, engine_on)
        self.engine = engine
        self.transmission = transmission
        self.num_of_gears = num_of_gears
        self.current_gear = current_gear

        self.each_gear_speed = max_speed / num_of_gears

    def start_engine(self):
        super().start_engine()

    def accelerate(self, value):
        super().accelerate(value)
        if self.transmission == 'mechanical':
            if self.current_speed > self.each_gear_speed * self.current_gear:
                self.current_gear += 1
            elif self.current_gear == 0:
                self.current_gear = 1

    def stop(self):
        super().stop()


petrolVehicle = PetrolVehicle('Audi', 'new', 15000, 220, 0, 2.0, 'mechanical', 6)
petrolVehicle.stop()
petrolVehicle.start_engine()
petrolVehicle.stop()
petrolVehicle.start_engine()
petrolVehicle.accelerate(10)
petrolVehicle.accelerate(30)
petrolVehicle.accelerate(40)
petrolVehicle.accelerate(40)
petrolVehicle.accelerate(40)
petrolVehicle.accelerate(40)
petrolVehicle.accelerate(39)
petrolVehicle.stop()

