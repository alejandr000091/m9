def carring_calc(a):
    def inner_b(b):
        def inner_c(c):
            return a + b + c
        return inner_c
    return inner_b
a, b, c = 1, 2, 3

my_func1 = carring_calc(a)
my_func2 = my_func1(b)
my_func3 = my_func2(c)

print(my_func3)

"""for home work from mentor"""

# def input_error(func):
#     def inner(*args):
#         try:
#             return func(*args)
#         except IndexError:
#             return "Not enough params"
#     return inner


# @input_error
# def my_func(*args):
#     name = args[0]
#     phone = args[1]
#     return f"Add {name = } {phone = }"


# while True:
#     user_input = input(">>>")
#     if user_input == "exit":
#         break
#     print(my_func(*user_input.split()))