contacts = {}

def input_errors(func):
    def inner(*args):
        try:
            return func(*args)
        except (KeyError, IndexError, ValueError):
            return "Not enough arguments."
    return inner


def hello(*args):
    return "How can I help you?"


@input_errors
def add(*args):
    list_of_contacts = args[0].split()
    contact = list_of_contacts[0]
    phone_number = list_of_contacts [1:]

    if not phone_number:
        raise IndexError()
        
    return f'contact : {contact}, phone_number: {phone_number}'



def good_bye(*args):
    return 'Good bye!'


# def exit(*args):
#     return 'Good bye!'


# def close(*args):
#     return 'Good bye!'


def no_command(*args):
    return "Unknown command, try again"


COMMANDS = {'hello': hello,
            'add': add,
            'good bye': good_bye,
            'exit': good_bye,
            'close': good_bye
}


def command_handler(text):
    for kword, command in COMMANDS.items():
        if text.startswith(kword):
            return command, text.replace(kword, '').strip()
    return no_command, None



def main():
    print(hello())
    while True:
        user_input = input(">>>")
        command, data = command_handler(user_input)
        print(command(data))
        if command == good_bye:
            break
            


if __name__ == '__main__':
    main()

