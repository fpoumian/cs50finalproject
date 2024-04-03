from lib.pool.rectangular_pool import RectangularPool
from lib.pool.water_color import WaterColor
from lib.pool.depth_type import DepthType
import pytest

def test_init_rectangular_pool_with_all_args():

    init_args = {
        "gallon_capacity": 5191.35,
        "length": 11.0,
        "width": 13.0,
        "depth_type": DepthType.VARIABLE_DEPTH,
        "depth_swallow_end": 3.3,
        "depth_deep_end": 4.5,
        "water_color": WaterColor.TEAL_GREEN,
    }

    rect_pool = RectangularPool(**init_args)

    assert rect_pool.gallon_capacity == 5191.35
    assert rect_pool.length == 11.0
    assert rect_pool.width == 13.0
    assert rect_pool.depth_swallow_end == 3.3
    assert rect_pool.depth_deep_end == 4.5
    assert rect_pool.water_color == WaterColor.TEAL_GREEN
    assert rect_pool.depth_type == DepthType.VARIABLE_DEPTH

def test_init_rectangular_pool_with_gallon_only():

    init_args = {
        "gallon_capacity": 5191.35,
    }

    rect_pool = RectangularPool(**init_args)

    assert rect_pool.gallon_capacity == 5191.35


def test_rectangular_pool_get_volume_with_gallons():

    init_args = {
        "gallon_capacity": 5191.35,
    }

    rect_pool = RectangularPool(**init_args)

    assert rect_pool.get_volume() == 5191.35


def test_rectangular_pool_get_volume_with_no_args_raises_error():

    with pytest.raises(RuntimeError):
        init_args = {}

        rect_pool = RectangularPool(**init_args)

        assert rect_pool.get_volume() == 5191.35

def test_rectangular_pool_wrong_water_color_value_raises_error():

    with pytest.raises(ValueError):
        init_args = {
            "water_color": 'green'
        }

        rect_pool = RectangularPool(**init_args)

        assert rect_pool.water_color

def test_rectangular_pool_wrong_depth_type_value_raises_error():

    with pytest.raises(ValueError):
        init_args = {
            "depth_type": 'variable'
        }

        rect_pool = RectangularPool(**init_args)

        assert rect_pool.depth_type

def test_rectangular_pool_get_volume_with_no_depths_raises_error():

    with pytest.raises(RuntimeError):
        
        init_args = {
        "length": 8.0,
        "width": 7.0,
        }

        rect_pool = RectangularPool(**init_args)

        assert rect_pool.get_volume() == 5191.35

def test_rectangular_pool_get_volume_with_constant_depth():

    init_args = {
        "length": 8.0,
        "width": 7.0,
        "depth_swallow_end": 4.5,
        "depth_type": DepthType.CONSTANT_DEPTH
    }

    rect_pool = RectangularPool(**init_args)

    assert rect_pool.get_volume() == 1890.0


def test_rectangular_pool_get_volume_with_variable_depth():

    init_args = {
        "length": 8.0,
        "width": 7.0,
        "depth_swallow_end": 4.5,
        "depth_deep_end": 6.5,
         "depth_type": DepthType.VARIABLE_DEPTH
    }

    rect_pool = RectangularPool(**init_args)

    assert rect_pool.get_volume() == 2310.0

def test_get_required_chlorine_shock():

    init_args = {
        "gallon_capacity": 5000.00,
        "water_color": WaterColor.TEAL_GREEN
    }

    rect_pool = RectangularPool(**init_args)

    assert rect_pool.get_required_chlorine_dose() == 1.0

    rect_pool.water_color = WaterColor.DARK_GREEN

    assert rect_pool.get_required_chlorine_dose() == 1.5

    rect_pool.water_color = WaterColor.BLACK_GREEN

    assert rect_pool.get_required_chlorine_dose() == 2.0


def test_rectangular_pool_generate():

        init_args = {
            "gallon_capacity": 5191.35,
            "length": 11.0,
            "width": 13.0,
            "depth_swallow_end": 3.3,
            "depth_deep_end": 4.5,
            "water_color": WaterColor.LIGHT_BLUE,
            "depth_type": DepthType.CONSTANT_DEPTH
        }

        rect_pool = RectangularPool.generate(**init_args)

        assert rect_pool.gallon_capacity == 5191.35
        assert rect_pool.length == 11.0
        assert rect_pool.width == 13.0
        assert rect_pool.depth_swallow_end == 3.3
        assert rect_pool.depth_deep_end == 4.5
        assert rect_pool.water_color == WaterColor.LIGHT_BLUE


def test_rectangular_pool_generate_raises_error_with_no_args():
    with pytest.raises(ValueError):
        RectangularPool.generate()



def test_rectangular_pool_generate_raises_error_with_missing_depth_type_arg():
    with pytest.raises(ValueError):
        init_args = {
            "length": 11.0,
            "width": 13.0,
        }

        RectangularPool.generate(**init_args)


def test_rectangular_pool_generate_raises_error_with_invalid_args_for_constant_depth():
    with pytest.raises(ValueError):
        init_args = {
            "depth_type": DepthType.CONSTANT_DEPTH,
             "length": 11.0,
             "width": 13.0,
        }
    
        RectangularPool.generate(**init_args)

def test_rectangular_pool_generate_raises_error_with_invalid_args_for_variable_depth():
    with pytest.raises(ValueError):
        init_args = {
            "depth_type": DepthType.VARIABLE_DEPTH,
             "length": 11.0,
             "width": 13.0,
             "depth_swallow_end": 3.3,
        }
        
    
        RectangularPool.generate(**init_args)


def test_rectangular_pool_generate_with_gallon_capacity_only():

        init_args = {
            "gallon_capacity": 5191.35,
        }

        rect_pool = RectangularPool.generate(**init_args)

        assert rect_pool.gallon_capacity == 5191.35
        assert rect_pool.get_volume() == 5191.35
