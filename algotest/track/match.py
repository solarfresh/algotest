# -*- coding: utf-8 -*-
from typing import Any, List, Tuple


class PathCountMatch(object):
    """
    Number of paths to reach mat[m][n] from mat[0][0]
    with exactly k coins
    """
    def __init__(self, mat: List[List]):
        """
        :param mat: a 2D map with numbers
        """
        self.mat = mat
        self.state = 0
        self.path = {}

    def match(self, k: Any, m: int, n: int) -> int:
        """
        :param k: target coins
        :param m: target position along x-axis
        :param n: target position along y-axis
        :return: number of path
        """
        # m and m must not be negative
        if (m < 0) or (n < 0):
            return 0
        else:
            self.path_record((m, n), command='APPEND')

        # There is a path if the start point matches the target value
        if (m == 0) and (n == 0):
            path_count = int(k == self.mat[m][n])
            if path_count:
                self.path_record((m, n), command='RESET')
            else:
                self.path_record((m, n), command='CLEAN')

            return path_count

        # number of path reaches the position (m, n) is counted from its neighbors
        k_prev = k - self.mat[m][n]
        return self.match(k_prev, m - 1, n) + self.match(k_prev, m, n - 1)

    def path_record(self, point: Tuple[int, int], command='APPEND'):
        """
        :param point: coordinate (m, n) which would be record
        :param command: APPEND, RESET, CLEAN
        """
        m, n = point
        if command.upper() == 'APPEND':
            if self.state not in self.path.keys():
                if self.state > 0:
                    path_list = self.path[self.state - 1]
                else:
                    path_list = []
            else:
                path_list = self.path[self.state]

            if path_list and (path_list[-1] == (0, 0)):
                path_list = [(a, b) for a, b in path_list if (a >= m) and (b >= n)]

            path_list.append((m, n))
            self.path[self.state] = path_list

        if command.upper() == 'RESET':
            self.state += 1

        if command.upper() == 'CLEAN':
            del self.path[self.state]

        return self
