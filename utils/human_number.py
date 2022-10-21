unit_list = ["", "k", "M"]


def display_human_number(raw_number):
    number = raw_number
    for unit in unit_list:
        if number < 1000:
            print(f"{round(number)}{unit}")
            return
        else:
            number = number/1000
    print(raw_number)
