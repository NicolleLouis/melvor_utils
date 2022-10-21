from utils.human_number import display_human_number
from utils.time import print_all_time


class Action:
    def __init__(
            self,
            action_time,
            preservation_chance=0,
            duplication_chance=0,
            input_used=1,
            output_produced=1
    ):
        self.action_time = action_time
        self.preservation_chance = preservation_chance
        self.duplication_chance = duplication_chance
        self.input_used = input_used
        self.output_produced = output_produced

    def compute_action_number(self, resource_number):
        input_number = resource_number / self.input_used
        return input_number / (1 - self.preservation_chance / 100)

    def compute_action_time(self, resource_number):
        action_number = self.compute_action_number(resource_number)
        return action_number * self.action_time

    def compute_final_resources(self, resource_number):
        action_number = self.output_produced * self.compute_action_number(resource_number)
        return action_number * (1 + self.duplication_chance / 100)

    def analyse(self, resource_number):
        print("Time taken:")
        print_all_time(self.compute_action_time(resource_number))
        print("###")
        print("Final number of resources: ")
        display_human_number(self.compute_final_resources(resource_number))
