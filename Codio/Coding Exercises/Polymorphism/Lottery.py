import random


class Lottery:
    def shuffle(self):
        results = []
        for i in range(5):
            results.append(random.randint(1, 20))
        return results


class PowerBall(Lottery):
    def shuffle(self):
        results = []
        for i in range(6):
            results.append(random.randint(1, 99))
        return results


if __name__ == '__main__':
    powerBall = PowerBall()
    print(powerBall.shuffle())
