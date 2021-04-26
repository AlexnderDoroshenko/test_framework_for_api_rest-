import math
import os


def count_numbers_from_string(string: str, sep="\n"):
    """Method takes a string and calculate filtered data - numbers"""
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
    """Method can read files only from help_utils folder"""
    file = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), file_name), "r")
    content = file.read()
    return content


def count_numbers(file_name):
    """Write a script (""count_numbers"") to calculate and print out the sum of all numbers in the file named "number.txt", ignoring lines that are empty or start with '#' symbol.
====== number.txt=========
# 1000000 <-- do not count this
123.4
-34.21
56.71
000
444.45
-555.72
+234.2
========================

Requirement 1. Create or use your GITHUB repo. Push code there and provide link to this repo as an answer;
Requirement 2. Your code runs without Exceptions;
Requirement 3. Lines that start with '#' symbol shall be ignored;
Requirement 4. Empty lines shall be ignored;
Requirement 5. Numbers can be positive and negative. e.g. "-1+2=1"
Requirement 6. Use your main language;"""
    string_numbers  = read_file(file_name)
    return count_numbers_from_string(string_numbers)

