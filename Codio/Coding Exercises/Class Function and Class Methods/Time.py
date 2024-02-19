class Time:
    hour = None
    minute = None
    second = None


def increment(time, seconds):
    time.second += seconds

    if time.second >= 60:
        time.second -= 60
        time.minute += 1

    if time.minute >= 60:
        time.minute -= 60
        time.hour += 1


def add_time(t1, t2):
    sum = Time()
    sum.hour = t1.hour + t2.hour
    sum.minute = t1.minute + t2.minute
    sum.second = t1.second + t2.second

    if sum.second >= 60:
        sum.second -= 60
        sum.minute += 1

    if sum.minute >= 60:
        sum.minute -= 60
        sum.hour += 1

    return sum


def print_time(self):
    print('%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second))


if __name__ == '__main__':
    start = Time()
    start.hour = 9
    start.minute = 45
    start.second = 0

    duration = Time()
    duration.hour = 1
    duration.minute = 35
    duration.second = 0

    done = add_time(start, duration)
    print_time(done)
