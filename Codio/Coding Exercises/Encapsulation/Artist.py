class Artist:

    def __init__(self, name: str, medium: str, style: str, famous_artwork: str) -> None:
        self.name = name
        self.medium = medium
        self.style = style
        self.famous_artwork = famous_artwork


if __name__ == "__main__":
    my_artist = Artist('Bill Watterson', 'ink and paper', 'cartoons', 'Calvin and Hobbes')
    print(my_artist.name)
    print(my_artist.medium)
    print(my_artist.style)
    print(my_artist.famous_artwork)
