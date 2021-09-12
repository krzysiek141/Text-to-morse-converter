# a program that takes any String input and converts it into Morse Code
from codes_data import codes_dict
from ascii_art import logo


def convert_text():
    my_string = input("Type the string that you want to convert\n>>>")

    encoded_string = ""
    for symbol in my_string.upper():
        if symbol == " ":
            encoded_string += "/ "
        else:
            encoded_string += codes_dict[symbol] + " "

    print(encoded_string)

def check_another():
    answer = input("Do you want to convert another sentence? (Y/N)\n>>>")
    return True if answer.upper() == "Y" else False

print(logo + "\n")
run_program = True
while run_program:
    convert_text()
    run_program = check_another()
