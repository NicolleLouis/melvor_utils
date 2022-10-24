unit_list = ["", "k", "M"]


def human_number(raw_number):
    number = raw_number
    for unit in unit_list:
        if number < 1000:
            return f"{round(number)}{unit}"
        else:
            number = number/1000
    return raw_number
