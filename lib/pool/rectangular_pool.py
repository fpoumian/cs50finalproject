from lib.pool.pool import Pool
from lib.pool.depth_type import DepthType

class RectangularPool(Pool):

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.length = kwargs.get('length', None)
        self.width = kwargs.get('width', None)

    @classmethod
    def generate(cls, **kwargs: dict):

        depth_type = kwargs.get('depth_type', None)
        gallon_volume = kwargs.get('gallon_volume', None)
        depth_swallow_end = kwargs.get('depth_swallow_end', None)
        depth_deep_end = kwargs.get('depth_deep_end', None)

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

    
        return cls(**kwargs)

    @property
    def length(self) -> float:
        return self._length
    
    @length.setter
    def length(self, length: float) -> None:
        self._length = length

    @property
    def width(self) -> float:
        return self._width
    
    @width.setter
    def width(self, width: float) -> None:
        self._width = width

    def calculate_constant_depth_volumen(self) -> float:
        return self.length * self.width * self.depth_swallow_end * 7.5
    
    def calculate_variable_depth_volumen(self) -> float:
        depth_average = (self.depth_deep_end + self.depth_swallow_end) / 2
        return self.length * self.width * depth_average * 7.5

    def get_volume(self) -> float:
        if self.gallon_volume:
            return self.gallon_volume
        elif self.length and self.width:
            if self.depth_type == DepthType.VARIABLE_DEPTH:
                return self.calculate_variable_depth_volumen()
            elif self.depth_type == DepthType.CONSTANT_DEPTH:
                return self.calculate_constant_depth_volumen()
            else:
                raise RuntimeError('Cannot calculate pool volume with current data')    
        else:
            raise RuntimeError('Cannot calculate pool volume with current data')
        
