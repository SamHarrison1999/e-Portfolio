class Employee:
    def __init__(self, first_name, last_name, email, annual_leave_remaining):
        self._first_name = first_name
        self._last_name = last_name
        self._email = email
        self._annual_leave_remaining = annual_leave_remaining

    def book_annual_leave(self):
        if self._annual_leave_remaining - 1 >= 0:
            print("Successfully booked annual leave")
            self._annual_leave_remaining -= 1
            print(str(self._annual_leave_remaining) + " days of annual leave remaining")
        else:
            print("Unable to book annual leave as you have no more annual leave.")

    @property
    def first_name(self):
        return self._first_name

    @property
    def last_name(self):
        return self._last_name

    @property
    def email(self):
        return self._email

    @property
    def annual_leave_remaining(self):
        return self._annual_leave_remaining


if __name__ == '__main__':
    employee = Employee("Sam", "Harrison", "samuel.harrison@verint.com", 28)
    print(employee.first_name)
    print(employee.last_name)
    print(employee.email)
    print(employee.annual_leave_remaining)
    employee.book_annual_leave()
