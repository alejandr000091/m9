"""solution Yiriy"""
# from functools import reduce

# payment = [100, -3, 400, 35, -100]

# def amount_payment(payment):
#     return reduce(lambda x, y: x+y, filter(lambda x: x>0, payment))

# print(amount_payment(payment))

"""other solution"""
# from functools import reduce

# payment = [100, -3, -400, 35, -100]

# def amount_payment(payment):
#     new_sum = []
#     for i in filter(lambda x: x>0, payment):
#         new_sum.append(i)
#     result = reduce(lambda x, y: x +y, new_sum)
#     return result

# print(amount_payment(payment))


"""my solution"""
#не вірене рішення тому що з першим від'ємним значенням не працює

from functools import reduce

payment = [100, -3, -400, 35, 100]

def amount_payment(payment):
    new_sum = []
    result = reduce(lambda x, y: x +y if x > 0 and y > 0 else x, payment)
    return result

print(amount_payment(payment))
