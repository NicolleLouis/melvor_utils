from utils.human_number import human_number
from utils.time import print_all_time


class RefiningAction:
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

    # If is_stock: consider the time to use all input
    # Is not is_stock: consider the time to produce desired quantity
    def compute_action_number(self, resource_number, is_stock=True):
        if is_stock:
            input_number = resource_number / self.input_used
            return input_number / (1 - self.preservation_chance / 100)
        else:
            target_output_number = resource_number / self.output_produced
            return target_output_number / (1 + self.duplication_chance / 100)

    def compute_action_time(self, resource_number, is_stock=True):
        action_number = self.compute_action_number(resource_number=resource_number, is_stock=is_stock)
        return action_number * self.action_time

    def compute_final_resources(self, resource_number):
        action_number = self.output_produced * self.compute_action_number(resource_number=resource_number, is_stock=True)
        return action_number * (1 + self.duplication_chance / 100)

    def compute_needed_inputs(self, resource_number):
        action_number = self.output_produced * self.compute_action_number(resource_number=resource_number, is_stock=False)
        return action_number * (1 - self.preservation_chance / 100)

    # Time and gain by using stock_resource_number of inpus
    def empty_stock(self, stock_resource_number, item=None):
        final_ressources = self.compute_final_resources(stock_resource_number)
        total_time = self.compute_action_time(stock_resource_number, is_stock=True)
        self.display_base_emptying_analyse(total_time, final_ressources)
        if item is not None:
            self.display_price_analyse(final_ressources, total_time, item)

    @staticmethod
    def display_base_emptying_analyse(total_time, final_ressources):
        print("Time taken:")
        print_all_time(total_time)
        print("###")
        print(f"Final number of resources: {human_number(final_ressources)}")

    @staticmethod
    def display_price_analyse(final_ressources, total_time, item):
        total_price = final_ressources * item.price
        price_per_hour = 3600 * total_price / total_time
        print(f"Finale price: {human_number(total_price)}")
        print(f"Price per hour: {human_number(price_per_hour)}")

    # Stock and time neede to create target_resource_number refined items
    def create_stock(self, target_resource_number):
        total_time = self.compute_action_time(resource_number=target_resource_number, is_stock=False)
        needed_input = self.compute_needed_inputs(resource_number=target_resource_number)
        self.display_base_creating_analysis(needed_input, total_time)

    @staticmethod
    def display_base_creating_analysis(needed_input, total_time):
        print("Time needed:")
        print_all_time(total_time)
        print("###")
        print(f"Needed Number of ressources: {human_number(needed_input)}")
