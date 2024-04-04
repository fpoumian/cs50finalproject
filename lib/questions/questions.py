
from lib.pool.water_color import WaterColor

import inquirer

def is_pool_capacity_known(ans):
    return ans['pool_known_information'] == 'know_gallon_capacity'

def is_pool_capacity_unknown(ans):
    return ans['pool_known_information'] == 'unknow_pool_capacity'

def should_ignore_variable_pool_question(ans):
    return is_pool_capacity_known(ans) or ans['pool_depth_type'] == 'pool_depth_type_is_constant'

def should_ignore_constant_pool_question(ans):
    return is_pool_capacity_known(ans) or ans['pool_depth_type'] == 'pool_depth_type_is_variable'

def get_questions():
    questions = [
         inquirer.List("pool_known_information", message="Which of these options best describes what you knwow about your pool?",
                choices=[
            ("I know the capacity/volume of my pool in Gallons", "know_gallon_capacity"),
            ("I do not know the capacity/volume of my pool, but I know the widht, length and depth of my pool", "unknown_pool_capacity")
                    ]
        ),
        inquirer.Text("pool_capacity", message="Enter the capacity of your pool in gallons", default=None, ignore=is_pool_capacity_unknown),
        inquirer.Text("pool_width", message="Enter the width of your pool in feet", ignore=is_pool_capacity_known),
        inquirer.Text("pool_length", message="Enter the length of your pool in feet", ignore=is_pool_capacity_known),
        inquirer.List("pool_depth_type", message="Which of these options best describes the depth of your pool?", ignore=is_pool_capacity_known,
                choices=[
            ("My pool has one constant depth", "pool_depth_type_is_constant"),
            ("My pool has a variable depth (i.e. one swallow depth and one deep depth)", "pool_depth_type_is_variable")
                    ]
        ),
        inquirer.Text("pool_constant_depth", message="Enter the depth of your pool", ignore=should_ignore_constant_pool_question),
        inquirer.Text("pool_variable_depth_swallow", message="Enter the swallow depth of your pool", ignore=should_ignore_variable_pool_question),
        inquirer.Text("pool_variable_depth_deep", message="Enter the deep depth of your pool", ignore=should_ignore_variable_pool_question),
        inquirer.List("pool_water_color", message="Which of these options illustrates the water color of your pool better?", ignore=is_pool_capacity_unknown,
                choices=[
            ("Light blue", WaterColor.LIGHT_BLUE.value),
            ("Teal green", WaterColor.TEAL_GREEN.value),
            ("Dark green", WaterColor.DARK_GREEN.value),
            ("Black green", WaterColor.BLACK_GREEN.value),
                    ]
        ),

    ]
    return questions
