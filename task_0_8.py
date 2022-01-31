def hours_converter(hour):
    hours = ' hour, '
    minute = ' minute '

    x = divmod(hour, 60)
    if x[0] != 0 and x[0] != 1 and x[0] != 0:
        hours = " hours, "

    if x[1] != 0 and x[0] != 1 and x[1] != 1:
        minute = " minutes "

    return str(x[0]) + hours + str(x[1]) + minute
