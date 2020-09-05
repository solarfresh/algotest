# -*- coding: utf-8 -*-
from typing import Any, Tuple


class BinarySearch(object):
    """
    A Binary Search based function
    """
    def __init__(self, items: list):
        """
        :param items: a set where the objective might belong
        """
        self.items = items

    def search(self, objective: Any, lower_index: int, upper_index: int) -> int:
        """
        :param objective: an interesting target
        :param lower_index: a lower bound of searching range
        :param upper_index: an upper bound of searching range
        :return: an index indicating the objective
        """

        middle_index = (lower_index + upper_index) // 2
        lower_index, upper_index = self.comparator(objective, lower_index, middle_index, upper_index)

        if upper_index < lower_index:
            return -1

        if (objective >= self.items[middle_index]) and (objective < self.items[middle_index + 1]):
            return middle_index

        return self.search(objective, lower_index, upper_index)

    def comparator(self,
                   objective: Any,
                   lower_index: int,
                   middle_index: int,
                   upper_index: int) -> Tuple[int, int]:

        if objective > self.items[middle_index]:
            lower_index = middle_index + 1

        if objective < self.items[middle_index]:
            upper_index = middle_index - 1

        return lower_index, upper_index
