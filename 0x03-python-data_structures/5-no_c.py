#!/usr/bin/python3
def no_c(my_string):
    le = list(my_string)
    for x in le:
        if x == 'c':
            le.remove('c')
        if x == 'C':
            le.remove('C')
    my_string = "".join(le)
    return my_string
