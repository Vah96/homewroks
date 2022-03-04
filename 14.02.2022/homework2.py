
"""decorators"""


# 1. Գրել դեկորատոր և կիրառել number ֆունկցիայի վրա։ Դեկորացված ֆունկցիան պետք է վերադարձնի n-ը բազմապատկած 10-ով։


def number_decoration(orig_func):
    def wrapper(n):
        return 10 * orig_func(n)
    return wrapper


@number_decoration
def number(n):
    return n


# print(number(5))


# 2. Գրել դեկորատոր type_check անունով։ Այն կստուգի դեկորացված ֆունկցիայի արգումենտների տիպը։ Եթե ֆունկցիային սխալ տիպ
# փոխանցենք, ապա բարձրացնել TypeError exception:
# Օրինակ, ունենք add_integers(a, b) ֆունկցիա, որը պետք է գումարի a, b թվերը։ Այն կարող ենք դեկորացնել
# type_check(int)-ով և եթե add_integers-ին փոխանցենք ոչ int պարամետր, մենք կստանանք TypeError


def check_int_type(type_value):
    def wrapper_func(orig_func):
        def wrapper(*args):
            for i in args:  # args is a tuple
                if type(i) != type_value:
                    raise TypeError(f'"{i}" is not integer')
            return orig_func(*args)
        return wrapper
    return wrapper_func


@check_int_type(int)
def my_sum(a, b):
    return a + b


sum = my_sum(67, 7)
print(sum)

""" Recursion """

# 3. Write a recursive function to calculate the sum of elements of a list.
# Գրել ռեկուրսիվ ֆունկցիա, որը կվերադարձնի իրեն փոխանցված լիստի տարրերի գումարը։ Չօգտվել sum() կամ նման ֆունկցիաներից։


def list_elements_sum(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        return lst[0] + list_elements_sum(lst[1:])


lst_1 = [1, 2, 3, 4, 5]
elements_sum = list_elements_sum(lst_1)
print(elements_sum)


# 4. Write a recursive function to calculate the geometric sum of n, where r = 2, a = 1.
# Գրել ռեկուսրիվ ֆունկցիա, որը կհաշվի n տարրերի երկրաչափական գումարը, որտեղ r = 2, a = 1:
# Երկրաչափական գումարը՝ SUM(a * (r ** k)), որտեղ k աճում է 1-ից մինչև n:

def geometric_rec(k, a=1, r=2):
    if k == 1:
        return a * (r ** k)
    return (a * (r ** k)) + geometric_rec(k-1)


geometric_sum = geometric_rec(5)
print(geometric_sum)

