from .pool import Pool, DepthType
import math


class RoundPool(Pool):

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.diameter = kwargs.get("diameter", None)

    @classmethod
    def generate(cls, **kwargs):

        depth_type = kwargs.get("depth_type", None)
        gallon_volume = kwargs.get("gallon_volume", None)
        depth_swallow_end = kwargs.get("depth_swallow_end", None)
        depth_deep_end = kwargs.get("depth_deep_end", None)
        diameter = kwargs.get("diameter", None)

        if gallon_volume:
            return cls(**kwargs)

        if not depth_type:
            raise ValueError

        if depth_type == DepthType.CONSTANT_DEPTH:
            if not depth_swallow_end:
                raise ValueError

        if depth_type == DepthType.VARIABLE_DEPTH:
            if not depth_swallow_end or not depth_deep_end:
                raise ValueError

        if not diameter:
            raise ValueError(
                "required parameter (diameter) is missing when trying to instantiate RoundPool object"
            )

        return cls(**kwargs)

    @property
    def diameter(self) -> float:
        return self._diameter

    @diameter.setter
    def diameter(self, diameter: float) -> None:
        self._diameter = diameter

    def calculate_constant_depth_volumen(self) -> float:
        return math.pi * ((self.diameter / 2) ** 2) * self.depth_swallow_end * 7.5

    def calculate_variable_depth_volumen(self) -> float:
        depth_average = (self.depth_deep_end + self.depth_swallow_end) / 2
        return math.pi * ((self.diameter / 2) ** 2) * depth_average * 7.5

    def get_volume(self) -> float:
        if self.gallon_volume:
            return self.gallon_volume
        elif self.diameter:
            if self.depth_type == DepthType.VARIABLE_DEPTH:
                return self.calculate_variable_depth_volumen()
            elif self.depth_type == DepthType.CONSTANT_DEPTH:
                return self.calculate_constant_depth_volumen()
            else:
                raise RuntimeError("Cannot calculate pool volume with current data")
        else:
            raise RuntimeError("Cannot calculate pool volume with current data")
