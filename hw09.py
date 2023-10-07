records = {}


def user_error(func):
    def inner(*args):
        try:
            return func(*args)
        except IndexError:
            return "Give me name and phone please"
        except KeyError:
            return "Enter correct user name"
        except ValueError as e:
            if str(e) == "Not enough number":
                return "Not enought number"
            else:
                raise e  # Піднімаэмо помилку наверх, якщо вона іншого типу
    return inner

# @user_error
def sanitize_phone_number(phone):
    collected_phone = ""
    for ch in phone:
        collected_phone += ch
    new_phone = (
        collected_phone.strip()
            .removeprefix("+38")
            .replace("(", "")
            .replace(")", "")
            .replace("-", "")
            .replace(" ", "")
    )
    #print(new_phone)
    if len(new_phone) == 10:
         return "+38" + new_phone
    else: 
        raise ValueError("Not enough number")

@user_error
def add_record(*args):
    name = args[0]
    phone_number = sanitize_phone_number(args[1:])
    records[name] = phone_number
    return f"Add record {name = }, {phone_number = }"


@user_error
def change_record(*args):
    name = args[0]
    new_phone_number = sanitize_phone_number(args[1:])
    rec = records[name]
    if rec:
        records[name] = new_phone_number
        return f"Change record {name = }, {new_phone_number = }"


def unknown_cmd(*args):
    return "Unknown command. Try again. Or use 'help'"

def hello_cmd(*args):
    return "How can I help you?"

def help_cmd(*args):
    return_str = "\n"
    cmd_list = ["avalible command:",
            "hello - just say hello",
            "help - show avalible cmd",
            "add - add record - format 'name' 'phone'",
            "change - change record - format 'name' 'phone'",
            "phone - get phone by name",
            "show all - show all phone book",
            "good bye/close/exit - shotdown this script"]
    for ch in cmd_list:
        return_str += ch + "\n"
    return return_str

@user_error
def get_phone(*args):
    name = args[0]
    rec = records[name]
    if rec:
        return f"Phone number: {rec}"
    
@user_error 
def show_all(*args):
    return_str = "\n"
    for name,numbers in records.items():
        return_str += name + " " + numbers + "\n"
    return return_str

def close_cmd(*args):
    return "Good bye!"

COMMANDS = {add_record: "add",
            change_record: "change",
            hello_cmd: "hello",
            get_phone: "phone",
            show_all: "show all",
            help_cmd: "help",
            close_cmd: ("good bye", "close", "exit")}


def parser(text: str):
    for func, kw in COMMANDS.items():
        if text.lower().startswith(kw):
            return func, text[len(kw):].strip().split()
    return unknown_cmd, []


def main():
    while True:
        user_input = input(">>>")
        func, data = parser(user_input)
        print(func(*data))
        if func == close_cmd:
            break
        
        
if __name__ == '__main__':
    main()