import math


def count_numbers_from_string(string: str, sep="\n"):
    result = 0
    num_list = string.split(sep=sep)
    for number in num_list:
        if number.startswith("#"):
            continue
        elif number.startswith("+"):
            result += float(number.replace("+", ""))
        elif number.startswith("-"):
            result -= float(number.replace("-", ""))
        else:
            result += float(number)
    return result


def read_file(file_name: str):
    file = open(file_name, "r")
    content = file.read()
    return content

def count_numbers(file_name):
    string_numbers  = read_file(file_name)
    return count_numbers_from_string(string_numbers)
