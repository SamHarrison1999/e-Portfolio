import copy
from datetime import *


class Time:

    def __init__(self, hour=0, minute=0, second=0):
        minutes = hour * 60 + minute
        self.second = minutes * 60 + second

    def __str__(self):
        minutes, second = divmod(self.second, 60)
        hour, minute = divmod(minutes, 60)
        return '%.2d:%.2d:%.2d' % (hour, minute, second)

    def __add__(self, other):
        if isinstance(other, Time):
            return self.add_time(other)
        else:
            return self.increment(other)

    def __radd__(self, other):
        return self.__add__(other)

    def print_time(self):
        print('%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second))

    def time_to_int(self):
        minutes = self.hour * 60 + self.minute
        seconds = minutes * 60 + self.second
        return seconds

    def add_time(self, other):
        assert valid_time(self) and valid_time(other)
        seconds = self.time_to_int() + other.time_to_int()
        return int_to_time(seconds)

    def is_after(self, other):
        # convert time objects to integer
        integer_t1 = 3600 * self.hour + 60 * self.minute + self.second
        integer_t2 = 3600 * other.hour + 60 * other.minute + other.second

        return integer_t1 > integer_t2

    def increment(self, seconds):
        new_time = copy.copy(self)
        total_time = new_time.time_to_int() + seconds
        return int_to_time(total_time)

    def mul_time(self, factor):
        seconds = int(self.time_to_int() * factor)
        return int_to_time(seconds)

    def race_pace(self, number):
        return self.mul_time(1 / float(number))


def valid_time(time):
    if time.hour < 0 or time.minute < 0 or time.second < 0:
        return False
    if time.minute >= 60 or time.second >= 60:
        return False
    return True


def int_to_time(seconds):
    return Time(0, 0, seconds)


def today_day():
    return datetime.today().strftime("%A")


def birthday_countdown(birth_date):
    today = date.today()
    birthday = birth_date.replace(year=today.year)
    birthday = birthday.replace(year=birthday.year + 1) if birthday <= today else birthday
    age = today.year - birth_date.year - 1 if birth_date.year == birthday.year else today.year - birth_date.year - 1
    countdown = datetime(birthday.year, birthday.month, birthday.day, 0, 0, 0) - datetime.now()
    return f"You are currently {age} years old\nIt is {countdown.days} days, {countdown.seconds // 3600} hours, {countdown.seconds // 60 % 60} minutes, and {countdown.seconds % 60} seconds until your next birthday"


def double_day(date_1, date_2):
    d1 = min(date_1, date_2)
    d2 = max(date_1, date_2)
    double_day = (d2 - d1).days  # double_day is this many days from d2
    return d2 + timedelta(days=double_day)


def the_day_when_one_person_is_n_times_older_than_the_other(date_1, date_2, product):
    d1 = min(date_1, date_2)
    d2 = max(date_1, date_2)
    difference = (d2 - d1).days
    day = difference / (product - 1)
    return d2 + timedelta(days=day)
