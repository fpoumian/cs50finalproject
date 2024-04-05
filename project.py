from lib.pool.rectangular_pool import RectangularPool
from lib.pool.round_pool import RoundPool
from lib.pool.pool import Pool
from lib.pool.water_color import WaterColor, get_water_color_label
from lib.pool.depth_type import DepthType
from lib.pool.shape import Shape
from lib.questions.questions import get_questions
import inquirer
from tabulate import tabulate
from pprint import pprint
from typing_extensions import TypedDict
import sys

PoolInitArgs = TypedDict('PoolInitArgs', {
    'gallon_volume': float,
    'depth_type': DepthType,
    'depth_swallow_end': float,
    'water_color': WaterColor,
    'depth_deep_end': float,
    'width': float,
    'length': float,
}, total=False)

PromptAnswers = TypedDict('PromptAnswers', {
    'pool_shape': str,
    'pool_volume': str,
    'pool_depth_type': str,
    'pool_constant_depth': str,
    'pool_water_color': str,
    'pool_variable_depth_swallow': str,
    'pool_variable_depth_deep': str,
    'pool_width': str,
    'pool_length': str,
}, total=False)


def main():
    try:
        questions = get_questions()
        answers = inquirer.prompt(questions)
        pool = generate_pool_with_answers(answers)
        instructions = generate_pool_cleaning_instructions_message(pool)
        table = map_pool_data_to_table_data(pool)
    except (ValueError, RuntimeError) as e:
        sys.exit(e)

    print(instructions)
    print(tabulate(table))


def map_answers_to_pool_init_args(answers: PromptAnswers) -> PoolInitArgs:
    pool_water_color = answers.get('pool_water_color')
    gallon_volume = answers.get('pool_volume', None)
    depth_type = answers.get('pool_depth_type', None)
    pool_constant_depth = answers.get('pool_constant_depth', None)
    pool_variable_depth_swallow = answers.get('pool_variable_depth_swallow', None)
    pool_variable_depth_deep = answers.get('pool_variable_depth_deep', None)
    length = answers.get('pool_length', None)
    width = answers.get('pool_width', None)

    init_args: PoolInitArgs = {}

    if pool_water_color:
        init_args['water_color'] = WaterColor[pool_water_color]

    if gallon_volume:
        init_args['gallon_volume'] = float(gallon_volume)

    if depth_type:
        init_args['depth_type'] = DepthType[depth_type]

    if pool_constant_depth:
        init_args['depth_swallow_end'] = float(pool_constant_depth)

    if pool_variable_depth_swallow:
        init_args['depth_swallow_end'] = float(pool_variable_depth_swallow)

    if pool_variable_depth_deep:
        init_args['depth_deep_end'] = float(pool_variable_depth_deep)

    if length:
        init_args['length'] = float(length)

    if width:
        init_args['width'] = float(width)


    return init_args


def generate_pool_with_answers(answers: PromptAnswers) -> Pool:

    if not 'pool_shape' in answers:
        raise ValueError

    pool_shape: Shape = Shape[answers['pool_shape']]
    init_args: PoolInitArgs = map_answers_to_pool_init_args(answers)

    if pool_shape == Shape.RECTANGULAR:
        return RectangularPool.generate(**init_args) 
    elif pool_shape == Shape.ROUND:
        return RoundPool.generate(**init_args)
    else:
        raise RuntimeError('Cannot generate pool with current data')
    
def map_pool_data_to_table_data(pool: Pool) -> list:
    return [
        ['Pool Volume (gallons)', pool.get_volume()],
        ['Water Color', get_water_color_label(pool.water_color)],
        ['Required dose of Shock (lbs)', pool.get_required_chlorine_dose()],
        ['Required dose of Shock (g)', round(pool.get_required_chlorine_dose() * 453.592, 2)]
    ]
    
def generate_pool_cleaning_instructions_message(pool: Pool) -> str:
    required_chlorine_dose = pool.get_required_chlorine_dose()
    return f'You need {required_chlorine_dose:.2f} pounds (lbs) of shock to clean your pool. \nThe most common types of shock are calcium hypochlorite (cal hypo), sodium dichlor (dichlor shock), and non-chlorine shock.'

if __name__ == "__main__":
    main()
