from models.refining_action import RefiningAction


class RefiningActions:
    JAVELIN_HEAD = RefiningAction(
        action_time=1.65,
        preservation_chance=50,
        duplication_chance=49,
        input_used=2,
        output_produced=5,
    )

    JAVELIN = RefiningAction(
        action_time=1.3,
        preservation_chance=43,
        duplication_chance=31,
        input_used=3,
        output_produced=12,
    )

    BOLT = RefiningAction(
        action_time=1.5,
        preservation_chance=40,
        duplication_chance=31,
        input_used=1,
        output_produced=8,
    )

    SUMMONING = RefiningAction(
        action_time=3.95,
        preservation_chance=30,
        duplication_chance=9,
        input_used=1,
        output_produced=51,
    )

    SMITHING = RefiningAction(
        action_time=1.65,
        preservation_chance=55,
        duplication_chance=29,
        input_used=1,
        output_produced=1
    )

    SUPERHEAT4 = RefiningAction(
        action_time=2,
        preservation_chance=0,
        duplication_chance=1,
        input_used=1,
        output_produced=3,
    )
