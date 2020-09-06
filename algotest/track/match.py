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


class SquareSticksMatch(object):
    def __init__(self, items: list):
        self.items = sorted(items, key=self.comparator, reverse=True)
        self.total = sum(items)
        self.index = 0
        self.path = []

    def match(self):
        if len(self.items) < 4:
            return False

        if not self.total % 4 == 0:
            return False

        square_length = self.total // 4

        return self.search((square_length, square_length, square_length, square_length))

    def search(self, point):
        m, n, p, q = point

        if self.index < len(self.items):
            pick_stick_length = self.items[self.index]
            self.index += 1
        else:
            return 0

        if (m < 0) or (n < 0) or (p < 0) or (q < 0):
            self.path = [(s, t, u, v) for s, t, u, v in self.path if (s >= m) and (t >= n) and (u >= p) and (v >= q)]
            self.index = len(self.path)
            return 0
        else:
            self.path.append(point)

        if point in [(pick_stick_length, 0, 0, 0),
                     (0, pick_stick_length, 0, 0),
                     (0, 0, pick_stick_length, 0),
                     (0, 0, 0, pick_stick_length)]:
            self.path = [(s, t, u, v) for s, t, u, v in self.path if (s >= m) and (t >= n) and (u >= p) and (v >= q)]
            self.index = len(self.path)
            return 1

        return self.search((m - pick_stick_length, n, p, q)) \
            + self.search((m, n - pick_stick_length, p, q)) \
            + self.search((m, n, p - pick_stick_length, q)) \
            + self.search((m, n, p, q - pick_stick_length))

    @staticmethod
    def comparator(item):
        return item


if __name__ == '__main__':
    # items = [1,1,2,2,2]
    items = [3,3,3,3,4]
    square_match = SquareSticksMatch(items)
    print(square_match.match())
