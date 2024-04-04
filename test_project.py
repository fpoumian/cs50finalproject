from project import map_answers_to_pool_init_args
from lib.pool.water_color import WaterColor

sample_answer = {
    'pool_capacity': '5000',
    'pool_constant_depth': None,
    'pool_depth_type': None,
    'pool_known_information': 'know_gallon_capacity',
    'pool_length': None,
    'pool_variable_depth_deep': None,
    'pool_variable_depth_swallow': None,
    'pool_water_color': 'TEAL_GREEN',
    'pool_width': None
 }

def test_map_answers_to_pool_init_args():
    init_args = map_answers_to_pool_init_args(sample_answer)
    assert init_args['gallon_capacity'] == 5000.00
    assert init_args['water_color'] == WaterColor.TEAL_GREEN
