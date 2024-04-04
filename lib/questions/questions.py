
from lib.pool.water_color import WaterColor
from lib.pool.depth_type import DepthType
from lib.pool.shape import Shape


import inquirer

def is_pool_volume_known(ans):
    return ans['pool_known_information'] == 'known_gallon_volume'

def is_pool_volume_unknown(ans):
    return ans['pool_known_information'] == 'unknown_pool_volume'

def should_ignore_variable_pool_question(ans):
    return is_pool_volume_known(ans) or ans['pool_depth_type'] == DepthType.CONSTANT_DEPTH.value

def should_ignore_constant_pool_question(ans):
    return is_pool_volume_known(ans) or ans['pool_depth_type'] == DepthType.VARIABLE_DEPTH.value

def get_questions():
    questions = [
         inquirer.List("pool_shape", message="Which of these options best describes the shape of your pool?",
                choices=[
            ("My pool has a rectangular or squared shape", Shape.RECTANGULAR.value),
            ("My pool has a round shape", Shape.ROUND.value),
                    ]
        ),
         inquirer.List("pool_known_information", message="Which of these options best describes what you knwow about your pool?",
                choices=[
            ("I know the volume of my pool in gallons", "known_gallon_volume"),
            ("I do not know the volume of my pool, but I know the widht, length and depth of my pool", "unknown_pool_volume")
                    ]
        ),
        inquirer.Text("pool_volume", message="Enter the volume of your pool in gallons", default=None, ignore=is_pool_volume_unknown),
        inquirer.Text("pool_width", message="Enter the width of your pool in feet", ignore=is_pool_volume_known),
        inquirer.Text("pool_length", message="Enter the length of your pool in feet", ignore=is_pool_volume_known),
        inquirer.List("pool_depth_type", message="Which of these options best describes the depth of your pool?", ignore=is_pool_volume_known,
                choices=[
            ("My pool has one constant depth", DepthType.CONSTANT_DEPTH.value),
            ("My pool has a variable depth (i.e. one swallow depth and one deep depth)", DepthType.VARIABLE_DEPTH.value)
                    ]
        ),
        inquirer.Text("pool_constant_depth", message="Enter the depth of your pool", ignore=should_ignore_constant_pool_question),
        inquirer.Text("pool_variable_depth_swallow", message="Enter the swallow depth of your pool", ignore=should_ignore_variable_pool_question),
        inquirer.Text("pool_variable_depth_deep", message="Enter the deep depth of your pool", ignore=should_ignore_variable_pool_question),
        inquirer.List("pool_water_color", message="Which of these options illustrates the water color of your pool better?", ignore=is_pool_volume_unknown,
                choices=[
            ("Light blue", WaterColor.LIGHT_BLUE.value),
            ("Teal green", WaterColor.TEAL_GREEN.value),
            ("Dark green", WaterColor.DARK_GREEN.value),
            ("Black green", WaterColor.BLACK_GREEN.value),
                    ]
        ),

    ]
    return questions
