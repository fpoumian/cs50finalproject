from lib.pool.rectangular_pool import RectangularPool

def test_init_rectangular_pool_with_all_args():

    init_args = {
        "volume": 5191.35,
        "length": 11.0,
        "width": 13.0,
        "depth_swallow_end": 3.3,
        "depth_deep_end": 4.5,
    }

    rect_pool = RectangularPool(**init_args)

    assert rect_pool.volume == 5191.35
    assert rect_pool.length == 11.0
    assert rect_pool.width == 13.0
    assert rect_pool.depth_swallow_end == 3.3
    assert rect_pool.depth_deep_end == 4.5