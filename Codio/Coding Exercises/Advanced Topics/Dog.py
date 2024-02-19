class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    # def __str__(self):
    #     return f'{self.name} is a {self.breed}'

    def __repr__(self):
        return f'Dog({self.name}, {self.breed})'


if __name__ == '__main__':
    dogs = [Dog('Rocky', 'Pomeranian'), Dog('Bullwinkle', 'Labrador Retriever')]
    print(dogs)
