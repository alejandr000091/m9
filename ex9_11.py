from functools import reduce

numbers = [3, 4, 6, 9, 34, 12]

def sum_numbers(numbers):
    result = reduce((lambda x, y: x + y), numbers)
    return(result)


sum_numbers(numbers)