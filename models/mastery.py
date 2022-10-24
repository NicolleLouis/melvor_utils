from utils.human_number import human_number
from utils.time import print_all_time


class Mastery:
    MAXIMUM_MASTERY = 13034431

    def __init__(
            self,
            current_mastery,
            action_time,
            mastery_per_action,
            input_per_action,
    ):
        self.current_mastery = current_mastery
        self.action_time = action_time
        self.mastery_per_action = mastery_per_action
        self.input_per_action = input_per_action

        self.remaining_actions = self.compute_remaining_action()
        self.remaining_time = self.compute_remaining_time()
        self.needed_inputs = self.compute_needed_inputs()

    def compute_remaining_action(self):
        remaining_mastery = self.MAXIMUM_MASTERY - self.current_mastery
        return remaining_mastery / self.mastery_per_action

    def compute_remaining_time(self):
        return self.remaining_actions * self.action_time

    def compute_needed_inputs(self):
        return self.remaining_actions * self.input_per_action

    def display(self):
        print(f"Needed inputs: {human_number(self.needed_inputs)}")
        print("Time remaining: ")
        print_all_time(self.remaining_time)
