from lib.pool.rectangular_pool import RectangularPool
from lib.pool.pool import Pool
from lib.pool.water_color import WaterColor
from lib.pool.depth_type import DepthType
from lib.questions.questions import get_questions
import inquirer
from pprint import pprint
import typing
from typing_extensions import TypedDict

PoolInitArgs = TypedDict('PoolInitArgs', {
    'gallon_volume': float,
    'depth_type': DepthType,
    'depth_swallow_end': float,
    'water_color': WaterColor,
    'depth_deep_end': float,
    'width': float,
    'length': float,
}, total=False)


def main():
    questions = get_questions()
    answers = inquirer.prompt(questions)

    pprint(answers)

def map_answers_to_pool_init_args(answers) -> PoolInitArgs:
    gallon_volume = answers.get('pool_volume', None)
    depth_type = answers.get('pool_depth_type', None)
    pool_constant_depth = answers.get('pool_constant_depth', None)
    pool_variable_depth_swallow = answers.get('pool_variable_depth_swallow', None)
    pool_variable_depth_deep = answers.get('pool_variable_depth_deep', None)
    length = answers.get('pool_length', None)
    width = answers.get('pool_width', None)

    init_args: PoolInitArgs = {
        "water_color":  WaterColor[answers.get('pool_water_color')],
    }

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


def make_pool(**kwargs):
    pass

if __name__ == "__main__":
    main()
