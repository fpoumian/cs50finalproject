from lib.pool.rectangular_pool import RectangularPool
from lib.pool.water_color import WaterColor
import pytest

def test_init_rectangular_pool_with_all_args():

    init_args = {
        "gallon_capacity": 5191.35,
        "length": 11.0,
        "width": 13.0,
        "depth_swallow_end": 3.3,
        "depth_deep_end": 4.5,
        "water_color": WaterColor.TEAL_GREEN
    }

    rect_pool = RectangularPool(**init_args)

    assert rect_pool.gallon_capacity == 5191.35
    assert rect_pool.length == 11.0
    assert rect_pool.width == 13.0
    assert rect_pool.depth_swallow_end == 3.3
    assert rect_pool.depth_deep_end == 4.5
    assert rect_pool.water_color == WaterColor.TEAL_GREEN

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
    }

    rect_pool = RectangularPool(**init_args)

    assert rect_pool.get_volume() == 1890.0


def test_rectangular_pool_get_volume_with_variable_depth():

    init_args = {
        "length": 8.0,
        "width": 7.0,
        "depth_swallow_end": 4.5,
        "depth_deep_end": 6.5,
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

