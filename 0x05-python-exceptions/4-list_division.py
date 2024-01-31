#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    i = 0
    alist = []
    while i != list_length:
        number = 0
        try:
            number = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        finally:
            alist.append(number)
        i += 1
    return alist
