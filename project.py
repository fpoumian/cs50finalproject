from lib.pool.rectangular_pool import RectangularPool
from lib.pool.pool import Pool
from lib.pool.water_color import WaterColor
from lib.questions.questions import get_questions
import inquirer
from pprint import pprint



def main():
    questions = get_questions()
    answers = inquirer.prompt(questions)

    pprint(answers)

def map_answers_to_pool_init_args(answers) -> dict:
    init_args = {
        "gallon_capacity": float(answers.get('pool_capacity')),
        "water_color":  WaterColor[answers.get('pool_water_color')],
    }

    return init_args


def make_pool(**kwargs):
    pass

if __name__ == "__main__":
    main()
