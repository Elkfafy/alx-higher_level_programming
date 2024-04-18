#!/usr/bin/python3
""" print sorted module """


class MyList(list):
    """ My List Class """

    def print_sorted(self):
        """ print sorted function """

        alist = [i for i in self]
        alist.sort()
        print(alist)
