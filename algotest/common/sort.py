# -*- coding: utf-8 -*-


class PairSorter(object):

    def __init__(self):
        self.pairs = []

    def pair(self, array, comparator, reverse=True):
        array = sorted(array, reverse=reverse)
        length = len(array)

        shift = 0
        for i in range(length):
            switch = True
            for j in range(shift, length):
                if comparator(array[i], array[j]):
                    if switch:
                        shift = j
                        switch = False
                    self.pairs.append((array[i], array[j]))

        return self.pairs


if __name__ == '__main__':
    def comparator0(a, b):
        return True if a > 2 * b else False

    data = [5, 4, 3, 2, 1]

    sorter = PairSorter()
    sorter.pair(data, comparator0)
    print(sorter.pairs)
    print(len(sorter.pairs))
