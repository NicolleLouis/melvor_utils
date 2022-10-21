def print_detailed_time(time, unit):
    print(f"{round(time, 2)} {unit}")


def print_all_time(time):
    print_detailed_time(time, 'secs')

    time = time / 60
    if time < 1:
        return
    print_detailed_time(time, 'mins')

    time = time / 60
    if time < 1:
        return
    print_detailed_time(time, 'hours')

    time = time / 24
    if time < 1:
        return
    print_detailed_time(time, 'days')

    time = time / 7
    if time < 1:
        return
    print_detailed_time(time, 'weeks')