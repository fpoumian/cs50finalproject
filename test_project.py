from project import map_answers_to_pool_init_args
from lib.pool.water_color import WaterColor
from lib.pool.depth_type import DepthType

def test_map_answers_to_pool_init_args_with_known_gallon_volume():
    answer = {
    'pool_volume': '5000',
    'pool_constant_depth': None,
    'pool_depth_type': None,
    'pool_known_information': 'known_gallon_volume',
    'pool_length': None,
    'pool_variable_depth_deep': None,
    'pool_variable_depth_swallow': None,
    'pool_water_color': 'TEAL_GREEN',
    'pool_width': None
 }

    init_args = map_answers_to_pool_init_args(answer)
    assert init_args['gallon_volume'] == 5000.00
    assert init_args['water_color'] == WaterColor.TEAL_GREEN


def test_map_answers_to_pool_init_args_with_unknown_gallon_volume_and_constant_depth():
    answer = {
    'pool_volume': None,
    'pool_constant_depth': '2.8',
    'pool_depth_type': 'CONSTANT_DEPTH',
    'pool_known_information': 'unknown_gallon_volume',
    'pool_length': '4.5',
    'pool_width': '3.5',
    'pool_variable_depth_deep': None,
    'pool_variable_depth_swallow': None,
    'pool_water_color': 'TEAL_GREEN',
 }

    init_args = map_answers_to_pool_init_args(answer)
    assert init_args['depth_type'] == DepthType.CONSTANT_DEPTH
    assert init_args['water_color'] == WaterColor.TEAL_GREEN
    assert init_args['depth_swallow_end'] == 2.8
    assert init_args['width'] == 3.5
    assert init_args['length'] == 4.5

def test_map_answers_to_pool_init_args_with_unknown_gallon_volume_and_variable_depth():
    answer = {
    'pool_volume': None,
    'pool_constant_depth': '2.8',
    'pool_depth_type': 'VARIABLE_DEPTH',
    'pool_known_information': 'unknown_gallon_volume',
    'pool_length': '4.5',
    'pool_width': '3.5',
    'pool_variable_depth_deep': '3.5',
    'pool_variable_depth_swallow': '3.2',
    'pool_water_color': 'DARK_GREEN',
 }

    init_args = map_answers_to_pool_init_args(answer)
    assert init_args['depth_type'] == DepthType.VARIABLE_DEPTH
    assert init_args['water_color'] == WaterColor.DARK_GREEN
    assert init_args['depth_swallow_end'] == 3.2
    assert init_args['depth_deep_end'] == 3.5
    assert init_args['width'] == 3.5
    assert init_args['length'] == 4.5
