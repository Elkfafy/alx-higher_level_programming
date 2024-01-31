#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    i = 0
    success = 0
    while x != i:
        try:
            print("{:d}".format(my_list[i]), end="")
            success += 1
        except (ValueError, TypeError):
            pass
        i += 1
    print()
    return success
