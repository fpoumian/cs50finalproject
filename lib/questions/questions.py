import inquirer.errors
from lib.pool import DepthType, WaterColor, Shape


import inquirer


def is_pool_volume_known(ans):
    return ans["pool_known_information"] == "known_gallon_volume"


def is_pool_volume_unknown(ans):
    return ans["pool_known_information"] == "unknown_pool_volume"


def should_ignore_variable_pool_question(ans):
    return (
        is_pool_volume_known(ans)
        or ans["pool_depth_type"] == DepthType.CONSTANT_DEPTH.value
    )


def should_ignore_constant_pool_question(ans):
    return (
        is_pool_volume_known(ans)
        or ans["pool_depth_type"] == DepthType.VARIABLE_DEPTH.value
    )


def validate_numeric_answer(_, current: str):

    try:
        answer = float(current)

        if answer <= 0:
            raise inquirer.errors.ValidationError(
                "", reason="Your answer must be higher than zero."
            )
        return True

    except ValueError:
        raise inquirer.errors.ValidationError(
            "", reason="Your answer must be a valid number."
        )


def get_questions() -> list:
    questions = [
        inquirer.List(
            "pool_known_information",
            message="Which of these options best describes what you know about your swimming pool?",
            choices=[
                ("I know the volume of my pool in gallons", "known_gallon_volume"),
                (
                    "I do not know the volume of my pool, but I know other measurements of my pool (i.e. width, length or diameter)",
                    "unknown_pool_volume",
                ),
            ],
        ),
        inquirer.List(
            "pool_shape",
            message="Which of these options best describes the shape of your swimming pool?",
            ignore=is_pool_volume_known,
            choices=[
                ("My pool has a rectangular or squared shape", Shape.RECTANGULAR.value),
                ("My pool has a round shape", Shape.ROUND.value),
            ],
        ),
        inquirer.Text(
            "pool_volume",
            message="Enter the volume of your swimming pool (in gallons)",
            validate=validate_numeric_answer,
            default=None,
            ignore=is_pool_volume_unknown,
        ),
        inquirer.Text(
            "pool_width",
            validate=validate_numeric_answer,
            message="Enter the width of your swimming pool (in feet)",
            ignore=is_pool_volume_known,
        ),
        inquirer.Text(
            "pool_length",
            validate=validate_numeric_answer,
            message="Enter the length of your swimming pool (in feet)",
            ignore=is_pool_volume_known,
        ),
        inquirer.List(
            "pool_depth_type",
            message="Which of these options best describes the depth of your swimming pool?",
            ignore=is_pool_volume_known,
            choices=[
                ("My pool has one constant depth", DepthType.CONSTANT_DEPTH.value),
                (
                    "My pool has a variable depth (i.e. one swallow depth and one deep depth)",
                    DepthType.VARIABLE_DEPTH.value,
                ),
            ],
        ),
        inquirer.Text(
            "pool_constant_depth",
            validate=validate_numeric_answer,
            message="Enter the depth of your swimming pool (in feet)",
            ignore=should_ignore_constant_pool_question,
        ),
        inquirer.Text(
            "pool_variable_depth_swallow",
            validate=validate_numeric_answer,
            message="Enter the swallow depth of your swimming pool (in feet)",
            ignore=should_ignore_variable_pool_question,
        ),
        inquirer.Text(
            "pool_variable_depth_deep",
            validate=validate_numeric_answer,
            message="Enter the deep depth of your swimming pool (in feet)",
            ignore=should_ignore_variable_pool_question,
        ),
        inquirer.List(
            "pool_water_color",
            message="Which of these options best illustrates the color of the water in your swimming pool?",
            choices=[
                ("Light blue (maintenance)", WaterColor.LIGHT_BLUE.value),
                ("Teal green", WaterColor.TEAL_GREEN.value),
                ("Dark green", WaterColor.DARK_GREEN.value),
                ("Black green", WaterColor.BLACK_GREEN.value),
            ],
        ),
    ]
    return questions
