# a program that takes any String input and converts it into Morse Code
from codes_data import codes_dict
from ascii_art import logo


def convert_text(text: str) -> str:
    '''Converts text into morse code'''
    encoded_string = ""
    for symbol in text.upper():
        if symbol == " ":
            encoded_string += "/ "
        else:
            try:
                encoded_string += codes_dict[symbol] + " "
            except KeyError:
                representation = input(f'Can not proceed. "{symbol}" is '
                                       f'not a valid symbol. Please type '
                                       f'a text representation\n>>>')
                encoded_string += convert_text(representation)
    return encoded_string

def check_another() -> bool:
    '''Checks if you want to convert another time'''
    answer = input("Do you want to convert another sentence? (Y/N)\n>>>")
    return True if answer.upper() == "Y" else False


print(logo + "\n")
run_program = True
while run_program:
    my_string = input("Type the string that you want to convert\n>>>")
    print(convert_text(my_string))
    run_program = check_another()