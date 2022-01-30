def triangle_area(length_one, length_two, length_three):

    semiperimeter = (length_one + length_two + length_three)/2
    area = (semiperimeter * (semiperimeter - length_one)*(semiperimeter - length_two) *
            (semiperimeter - length_three))**0.5
    return area

