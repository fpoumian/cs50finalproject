from abc import ABC, abstractmethod
from .water_color import WaterColor
from .depth_type import DepthType

class Pool(ABC):

    def __init__(self, **kwargs) -> None:
        self.gallon_volume = kwargs.get("gallon_volume", None)
        self.depth_swallow_end = kwargs.get("depth_swallow_end", None)
        self.depth_deep_end = kwargs.get("depth_deep_end", None)
        self.water_color = kwargs.get("water_color", None)
        self.depth_type = kwargs.get("depth_type", None)

    @classmethod
    @abstractmethod
    def generate(cls, **kwargs):
        pass

    @abstractmethod
    def get_volume(self):
        pass

    @property
    def gallon_volume(self) -> float:
        return self._gallon_volume

    @gallon_volume.setter
    def gallon_volume(self, gallon_volume: float) -> None:
        self._gallon_volume = gallon_volume

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

    @property
    def depth_type(self) -> DepthType:
        return self._depth_type

    @depth_type.setter
    def depth_type(self, depth_type: DepthType) -> None:
        if depth_type and not type(depth_type) is DepthType:
            raise ValueError
        self._depth_type = depth_type

    def get_required_shock_dose(self, unit="lbs") -> float:
        if not self.water_color:
            raise RuntimeError
        volume = self.get_volume()
        multiplier = None
        gallons_per_pound = 10000.0

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

        if unit == "g":
            return ((volume / gallons_per_pound) * multiplier) * 453.6
        else:
            return (volume / gallons_per_pound) * multiplier
