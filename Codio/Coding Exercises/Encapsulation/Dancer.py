class Dancer:
    def __init__(self, name: str, nationality: str, style: str) -> None:
        self._name = name
        self._nationality = nationality
        self._style = style

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
    def style(self) -> str:
        return self._style

    @style.setter
    def style(self, style: str) -> None:
        self._style = style


if __name__ == "__main__":
    my_dancer = Dancer("Savion Glover", "American", "tap")
    print(my_dancer.name)
    print(my_dancer.nationality)
    print(my_dancer.style)
    my_dancer.name = 'Anna Pavlova'
    my_dancer.nationality = 'Russian'
    my_dancer.style = 'ballet'
    print(my_dancer.name)
    print(my_dancer.nationality)
    print(my_dancer.style)
