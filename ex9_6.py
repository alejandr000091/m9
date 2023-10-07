import re

def generator_numbers(string=""):
    numbers = re.findall("\d+", string)
    for number in numbers:
        yield int(number)

def sum_profit(string):
    total = 0
    numbers = generator_numbers(string)
    for number in numbers:
        total += int(number)
    return total




# import re

# string = "The resulting profit was: from the southern possessions $ 100, from the northern colonies $500, and the king gave $1000."

# def generator_numbers(string=""):
#     numbers = re.findall("\d+", string)
#     for number in numbers:
#         yield int(number)

# search_number = generator_numbers(string)

# def sum_profit(numbers):
#     total = 0
#     for number in numbers:
#         try:
#             total += int(number)
#         except:
#             pass
#     return total

# print(sum_profit(search_number))