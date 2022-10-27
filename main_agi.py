from constants.agility.level_1 import *
from constants.agility.level_2 import *
from constants.agility.level_3 import *
from constants.agility.level_4 import *
from constants.agility.level_5 import *
from constants.agility.level_6 import *
from constants.agility.level_7 import *
from constants.agility.level_8 import *
from constants.agility.level_9 import *
from models.agility.course import Course

obstacles = [
    CARGO_NET, #1
    BALANCE_BEAM, #2
    BALANCE_SEESAW, #3
    GAP_JUMP, #4
    TREE_CLIMB, #5
    TREE_BALANCE, #6
    HEAT_TRAP, #7
    A_LOVELY_JOG, #8
    ICE_JUMP, #9
]

course = Course(obstacles=obstacles)
print(course.compute_average_money())
