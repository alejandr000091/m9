def format_phone_number(func):
    def inner(number):
        if len(func(number)) >= 12:
            return "+" + func(number)
        else:
            return "+38" + func(number)
    return inner
        

phone =  ('(093)', '-', '428','-', '38','-', '93')

@format_phone_number
def sanitize_phone_number(phone):
    collected_phone = ""
    for ch in phone:
        collected_phone += ch
    new_phone = (
        collected_phone.strip()
            .removeprefix("+")
            .replace("(", "")
            .replace(")", "")
            .replace("-", "")
            .replace(" ", "")
    )
    return new_phone