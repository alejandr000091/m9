def format_phone_number(func):
    def inner(number):
        if len(func(number)) >= 12:
            return "+" + func(number)
        else:
            return "+38" + func(number)
    return inner
        

phone =  ' +38(050)123-32-34'

@format_phone_number
def sanitize_phone_number(phone):
    new_phone = (
        phone.strip()
            .removeprefix("+")
            .replace("(", "")
            .replace(")", "")
            .replace("-", "")
            .replace(" ", "")
    )
    return new_phone

print(sanitize_phone_number(phone))