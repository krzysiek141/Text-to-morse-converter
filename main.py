# a program that takes any String input and converts it into Morse Code
from codes_data import codes_dict

my_string = input("Type the string that you want to convert\n")

encoded_string = ""
for symbol in my_string.upper():
    if symbol == " ":
        encoded_string += "/ "
    else:
        encoded_string += codes_dict[symbol] + " "

print(encoded_string)
print(codes_dict['"'])