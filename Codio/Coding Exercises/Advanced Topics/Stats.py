import statistics


class Stats:
    def mean(self, lst):
        return f'mean: {statistics.mean(lst)}'

    def median(self, lst):
        return f'median: {statistics.median(lst)}'

    def mode(self, lst):
        return f'mode: {statistics.mode(lst)}'