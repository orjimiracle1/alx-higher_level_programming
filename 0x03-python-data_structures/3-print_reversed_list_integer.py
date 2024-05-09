st_integer(my_list=[]):
    if my_list is None:
        return ('None')
    my_list.reverse()
    for i in my_list:
        print("{:d}".format(i))
