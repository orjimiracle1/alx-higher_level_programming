t(my_list, idx):
    for x in my_list:
        if idx == my_list.index(x):
            return(x)
        elif idx > len(my_list):
            return None
        elif idx < 0:
            return None
