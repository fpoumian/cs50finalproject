from project import map_answers_to_pool_init_args, generate_pool_with_answers, generate_pool_cleaning_instructions_message
from lib.pool.water_color import WaterColor
from lib.pool.depth_type import DepthType
from lib.pool.shape import Shape
from lib.pool.pool import Pool
from lib.pool.rectangular_pool import RectangularPool
from lib.pool.round_pool import RoundPool
import pytest

def test_map_answers_to_pool_init_args_with_known_gallon_volume():
    answer = {
    'pool_volume': '5000',
    'pool_constant_depth': None,
    'pool_depth_type': None,
    'pool_known_information': 'known_gallon_volume',
    'pool_length': None,
    'pool_variable_depth_deep': None,
    'pool_variable_depth_swallow': None,
    'pool_water_color': WaterColor.TEAL_GREEN.value,
    'pool_width': None
 }

    init_args = map_answers_to_pool_init_args(answer)
    assert init_args['gallon_volume'] == 5000.00
    assert init_args['water_color'] == WaterColor.TEAL_GREEN
    assert 'depth_type' not in init_args
    assert 'depth_swallow_end' not in init_args
    assert 'depth_deep_end' not in init_args
    assert 'width' not in init_args
    assert 'length' not in init_args


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
    'pool_water_color': WaterColor.TEAL_GREEN.value,
 }

    init_args = map_answers_to_pool_init_args(answer)
    assert init_args['depth_type'] == DepthType.CONSTANT_DEPTH
    assert init_args['water_color'] == WaterColor.TEAL_GREEN
    assert init_args['depth_swallow_end'] == 2.8
    assert init_args['width'] == 3.5
    assert init_args['length'] == 4.5
    assert 'depth_deep_end' not in init_args

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
    'pool_water_color': WaterColor.DARK_GREEN.value,
 }

    init_args = map_answers_to_pool_init_args(answer)
    assert 'pool_volume' not in init_args
    assert init_args['depth_type'] == DepthType.VARIABLE_DEPTH
    assert init_args['water_color'] == WaterColor.DARK_GREEN
    assert init_args['depth_swallow_end'] == 3.2
    assert init_args['depth_deep_end'] == 3.5
    assert init_args['width'] == 3.5
    assert init_args['length'] == 4.5

def test_generate_pool_with_answers_for_rectangular_pool():
   answers = {
    'pool_shape': Shape.RECTANGULAR.value,
    'pool_volume': '5000',
    'pool_constant_depth': None,
    'pool_depth_type': None,
    'pool_known_information': 'known_gallon_volume',
    'pool_length': None,
    'pool_variable_depth_deep': None,
    'pool_variable_depth_swallow': None,
    'pool_water_color': WaterColor.DARK_GREEN.value,
    'pool_width': None
   }

   pool = generate_pool_with_answers(answers)
   assert type(pool) is RectangularPool
   assert pool.gallon_volume == 5000.00
   assert pool.water_color == WaterColor.DARK_GREEN
   assert pool.get_required_chlorine_dose() == 1.5


def test_generate_pool_with_answers_for_round_pool():
   answers = {
    'pool_shape': Shape.ROUND.value,
    'pool_volume': '5000',
    'pool_constant_depth': None,
    'pool_depth_type': None,
    'pool_known_information': 'known_gallon_volume',
    'pool_length': None,
    'pool_variable_depth_deep': None,
    'pool_variable_depth_swallow': None,
    'pool_water_color': WaterColor.DARK_GREEN.value,
    'pool_width': None
   }

   pool = generate_pool_with_answers(answers)
   assert type(pool) is RoundPool
   assert pool.gallon_volume == 5000.00
   assert pool.water_color == WaterColor.DARK_GREEN
   assert pool.get_required_chlorine_dose() == 1.5

def test_generate_pool_with_answers_without_pool_shape():
      answers = {
      'pool_volume': '5000',
      'pool_constant_depth': None,
      'pool_depth_type': None,
      'pool_known_information': 'known_gallon_volume',
      'pool_length': None,
      'pool_variable_depth_deep': None,
      'pool_variable_depth_swallow': None,
      'pool_water_color': WaterColor.DARK_GREEN.value,
      'pool_width': None
      }

      with pytest.raises(ValueError):
         generate_pool_with_answers(answers)


def test_generate_pool_cleaning_instructions():
   answers = {
    'pool_shape': Shape.ROUND.value,
    'pool_volume': '5000',
    'pool_constant_depth': None,
    'pool_depth_type': None,
    'pool_known_information': 'known_gallon_volume',
    'pool_length': None,
    'pool_variable_depth_deep': None,
    'pool_variable_depth_swallow': None,
    'pool_water_color': WaterColor.DARK_GREEN.value,
    'pool_width': None
   }
     
   pool = generate_pool_with_answers(answers)

   instructions = generate_pool_cleaning_instructions_message(pool)

   assert 'You need 1.5 pounds of shock to clean your pool' in instructions
