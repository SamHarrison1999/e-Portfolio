class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed


if __name__ == '__main__':
    dogs = [Dog("Marceline", "German Shepherd"), Dog("Cajun", "Belgian Malinois"), Dog("Daisy", "Border Collie"),
            Dog("Rocky", "Golden Retriever"), Dog("Bella", "Irish Setter")]
    for dog in dogs:
        print(dog.name)
        print(dog.breed)
