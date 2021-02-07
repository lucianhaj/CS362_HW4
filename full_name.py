import random


def full_name(first, last):
    try:
        global full_name2
        middle_names = ("Hoven", "Everett", "Avery", "Evan", "River", "Devin", "Gavin", "Vardhan" )

        full_name2 = first + " " + (random.choice(middle_names)) + " " + last
    #full.append(full_name2)
    except TypeError:
        return "InvalidType"
    else:
        if first == "":
            return "One or more name(s) not provided"
        elif last == "":
            return "One or more name(s) not provided"
        elif str(first).isdigit() == 1:
            return "One or more name(s) are not numbers"
        elif str(last).isdigit() == 1:
            return "One or more name(s) are not numbers"
        else:
            return full_name2
