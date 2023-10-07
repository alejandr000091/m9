payment = [100, -3, 400, 35, -100]    


def positive_values(list_payment):
    return_list = []
    for i in filter(lambda x: x > 0, list_payment):
        return_list.append(i)
        #print(i)
    return return_list

print(positive_values(payment))
