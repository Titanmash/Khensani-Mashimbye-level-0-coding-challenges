def hours_converter(hour):
    hours = ' hour '
    minute = ' minute '
    x = divmod(hour, 60)
    if x[0] != 1:
        hours = " hours "

    if x[1] != 1:
        minute = " minutes "

    return str(x[0]) + hours + str(x[1]) + minute
