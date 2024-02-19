class Cyclist:
    def __init__(self, name: str, nationality: str, nickname: str) -> None:
        self._name = name
        self._nationality = nationality
        self._nickname = nickname

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        self._name = name

    @property
    def nationality(self) -> str:
        return self._nationality

    @nationality.setter
    def nationality(self, nationality: str) -> None:
        self._nationality = nationality

    @property
    def nickname(self) -> str:
        return self._nickname

    @nickname.setter
    def nickname(self, nickname: str) -> None:
        self._nickname = nickname


if __name__ == "__main__":
    my_cyclist = Cyclist("Greg LeMond", "American", "Le Montstre")
    print(my_cyclist.name)
    print(my_cyclist.nationality)
    print(my_cyclist.nickname)
    my_cyclist.name = "Eddy Merckx"
    my_cyclist.nationality = "Belgian"
    my_cyclist.nickname = "The Cannibal"
    print(my_cyclist.name)
    print(my_cyclist.nationality)
    print(my_cyclist.nickname)
