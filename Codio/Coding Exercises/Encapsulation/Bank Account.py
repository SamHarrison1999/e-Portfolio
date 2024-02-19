class BankAccount():
    def __init__(self, checking=0, savings=0) -> None:
        self._checking = checking
        self._savings = savings

    def get_checking(self) -> float:
        return self._checking

    def set_checking(self, checking: float) -> None:
        self._checking = checking

    def get_savings(self) -> float:
        return self._savings

    def set_savings(self, savings: float) -> None:
        self._savings = savings


if __name__ == "__main__":
    my_account = BankAccount()
    my_account.set_checking(523.48)
    print(my_account.get_checking())
    my_account.set_savings(386.15)
    print(my_account.get_savings())
