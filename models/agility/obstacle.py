class Obstacle:
    def __init__(
            self,
            name,
            level,
            time,
            money,
    ):
        self.name = name
        self.level = level
        self.time = time
        self.money = money

        self.average_money = money/time
