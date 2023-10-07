numbers = [1, 2, 3, 4, 5]

for i in map(lambda x: x ** 2, numbers):
    print(i)


# some_str = 'aaAbbB C F DDd EEe'
# for i in filter(lambda x: x[0].isupper(), some_str):
#     i.upper()
#     print(i)


contacts = [{'name': 'Allen Raymond', 'email': 'nulla.ante@vestibul.co.uk', 'phone': '(992) 914-3792', 'favorite': False}, 
            {'name': 'Chaim Lewis', 'email': 'dui.in@egetlacus.ca', 'phone': '(294) 840-6685', 'favorite': False}, 
            {'name': 'Kennedy Lane', 'email': 'mattis.Cras@nonenimMauris.net', 'phone': '(542) 451-7038', 'favorite': False}, 
            {'name': 'Wylie Pope', 'email': 'est@utquamvel.net', 'phone': '(692) 802-2949', 'favorite': False}, 
            {'name': 'Cyrus Jackson', 'email': 'nibh@semsempererat.com', 'phone': '(501) 472-5218', 'favorite': False}]


def get_emails(list_contacts):
    return_list = []
    for el in map(lambda x: x.get("email"), list_contacts):
        return_list.append(el)
        print(el)
    return return_list
        #print(el.get("email"))
#     return_list = []
#     return return_list(map(lambda x: x.get("email"), list_contacts))

# result = get_emails(contacts)
# print(result)

print(get_emails(contacts))

print(3*0)

func = lambda x: bool(x%2)
print(func(10),func(11))