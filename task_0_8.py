def number_to_hours_and_minutes(number):
    hours = ' hour, '
    minute = ' minute.'
    remainder = divmod(number, 60)
    if remainder[0] != 1:
        hours = " hours, "

    if remainder[1] != 1:
        minute = " minutes."

    return str(remainder[0]) + hours + str(remainder[1]) + minute
