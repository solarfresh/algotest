# -*- coding: utf-8 -*-
from typing import Any, Tuple
from algotest.common.search import BinarySearch


class Job:
    def __init__(self, start, finish, profit):
        self.start = start
        self.finish = finish
        self.profit = profit


class WeightedSchedule(BinarySearch):
    def __init__(self, jobs):
        super(WeightedSchedule, self).__init__(jobs)
        self.jobs = jobs
        self.items = [job.finish for job in jobs]

    def schedule(self):
        """
        :return: the maximum profit subset of jobs such that no two jobs in the subset overlap
        """
        # Sort jobs according to finish time
        self.jobs = sorted(self.jobs, key=lambda j: j.finish)
        self.items = [job.finish for job in self.jobs]

        # Create an array to store solutions of subproblems.  table[i]
        # stores the profit for jobs till arr[i] (including arr[i])
        job_nb = len(self.items)
        table = job_nb * [0]

        table[0] = self.jobs[0].profit;

        # Fill entries in table[] using recursive property
        for i in range(1, job_nb):
            # Find profit including the current job
            including_profit = self.jobs[i].profit
            state = self.search(self.jobs[i].start, 0, i)
            if state != -1:
                including_profit += table[state]
                # Store maximum of including and excluding
            table[i] = max(including_profit, table[i - 1])

        return table[job_nb - 1]

    def comparator(self,
                   objective: Any,
                   lower_index: int,
                   middle_index: int,
                   upper_index: int) -> Tuple[int, int]:

        if objective > self.jobs[middle_index].finish:
            lower_index = middle_index + 1

        if objective < self.jobs[middle_index].finish:
            upper_index = middle_index - 1

        return lower_index, upper_index
