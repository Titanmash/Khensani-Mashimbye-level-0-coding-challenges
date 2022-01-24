def hours(hour):
    hours = ' hour'
    minut = 'minute '
    x = divmod(hour, 60)
    if x[0] != 1:
        hours = " hours "

    if x[1] != 1:
        minut = " minutes "

    return str(x[0]) + hours + str(x[1]) + minut
