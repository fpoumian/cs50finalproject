from abc import ABC, abstractmethod
from lib.pool.water_color import WaterColor

class Pool(ABC):

    def __init__(self, **kwargs: dict) -> None:
        self.gallon_capacity = kwargs.get('gallon_capacity', None)
        self.depth_swallow_end = kwargs.get('depth_swallow_end', None)
        self.depth_deep_end = kwargs.get('depth_deep_end', None)
        self.water_color = kwargs.get('water_color', None)

    @classmethod
    def generate(cls, **kwargs: dict):
        return cls(**kwargs)
    
    @abstractmethod
    def get_volume():
        pass
    
    @property
    def gallon_capacity(self) -> float:
        return self._gallon_capacity
    
    @gallon_capacity.setter
    def gallon_capacity(self, gallon_capacity: float) -> None:
        self._gallon_capacity = gallon_capacity

    @property
    def depth_swallow_end(self) -> float:
        return self._depth_swallow_end
    
    @depth_swallow_end.setter
    def depth_swallow_end(self, depth_swallow_end: float) -> None:
        self._depth_swallow_end = depth_swallow_end

    @property
    def depth_deep_end(self) -> float:
        return self._depth_deep_end
    
    @depth_deep_end.setter
    def depth_deep_end(self, depth_deep_end: float) -> None:
        self._depth_deep_end = depth_deep_end

    @property
    def water_color(self) -> WaterColor:
        return self._water_color
    
    @water_color.setter
    def water_color(self, water_color: WaterColor) -> None:
        if water_color and not type(water_color) is WaterColor:
            raise ValueError
        self._water_color = water_color

    def get_required_chlorine_dose(self):
        if not self.water_color:
            raise RuntimeError
        volume = self.get_volume()
        multiplier = None

        match self.water_color:
            case WaterColor.LIGHT_BLUE:
                multiplier = 1
            case WaterColor.TEAL_GREEN:
                multiplier = 2
            case WaterColor.DARK_GREEN:
                multiplier = 3
            case WaterColor.BLACK_GREEN:
                multiplier = 4
            case _:
                raise RuntimeError

        return (volume / 10000.0) * multiplier

