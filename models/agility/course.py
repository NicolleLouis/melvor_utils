class Course:
    levels = None
    obstacles = None
    EXPECTED_LEVELS = set([1, 2, 3, 4, 5, 6, 7, 8, 9])

    def __init__(
            self,
            obstacles
    ):
        self.obstacles = obstacles
        self.set_levels()

    def add_obstacle(self, obstacle):
        self.obstacles.append(obstacle)

    def remove_obstacle(self, obstacle):
        self.obstacles.remove(obstacle)

    def set_levels(self):
        self.levels = set(
            list(
                map(
                    lambda obstacle: obstacle.level,
                    self.obstacles
                )
            )
        )

    def is_course_legal(self):
        self.set_levels()
        return self.levels == self.EXPECTED_LEVELS

    def compute_average_money(self):
        if not self.is_course_legal():
            return 0

        total_time = sum(map(lambda obstacle: obstacle.time, self.obstacles))
        total_money = sum(map(lambda obstacle: obstacle.money, self.obstacles))
        return total_money/total_time
