class VideoGame:
    def __init__(self, player):
        self.player = player
        self.level = 1
        self.score = 0


class Player:
    def __init__(self):
        self.health = 100
        self.inventory = []

if __name__ == "__main__":
    my_game = VideoGame(player)
