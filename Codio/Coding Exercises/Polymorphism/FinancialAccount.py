class FinancialAccount:
    def __init__(self, amount):
        self.account = amount

    def __add__(self, other):
        return self.account + other.account

    def __eq__(self, other):
        return self.account == other.account

    def __truediv__(self, other):
        return self.account / other.account

    def __floordiv__(self, other):
        return self.account // other.account


class BankAccount(FinancialAccount):
    pass


class InvestmentAccount(FinancialAccount):
    pass


if __name__ == '__main__':
    my_banking = BankAccount(500)
    my_investments = InvestmentAccount(750)
    print(my_investments + my_banking)
    print(my_investments == my_banking)
    print(my_investments / my_banking)
    print(my_investments // my_banking)