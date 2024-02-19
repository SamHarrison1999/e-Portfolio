class Country:
    def __init__(self, name: str, capital: str, population: int, continent: str) -> None:
        self._name = name
        self._capital = capital
        self._population = population
        self._continent = continent

    @property
    def name(self) -> str:
        return self._name

    @property
    def capital(self) -> str:
        return self._capital

    @property
    def population(self) -> int:
        return self._population

    @property
    def continent(self) -> str:
        return self._continent


if __name__ == "__main__":
    my_country = Country('France', 'Paris', 67081000, 'Europe')
    print(my_country.name)
    print(my_country.capital)
    print(my_country.population)
    print(my_country.continent)
