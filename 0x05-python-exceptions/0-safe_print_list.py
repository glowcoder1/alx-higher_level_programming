#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 0
    elem_printed = 0
    for i in range(0, x):
        try:
            print("{}".format(my_list[i]), end="")
            elem_printed += 1
        except Exception:
            continue
    print()
    return elem_printed
