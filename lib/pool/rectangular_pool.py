from lib.pool.pool import Pool

class RectangularPool(Pool):

    def __init__(self, **kwargs: float) -> None:
        super().__init__(**kwargs)
        self.length = kwargs.get('length', None)
        self.width = kwargs.get('width', None)

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
        if self.gallon_capacity:
            return self.gallon_capacity
        elif self.length and self.width:
            if self.depth_swallow_end and self.depth_deep_end:
                return self.calculate_variable_depth_volumen()
            elif self.depth_swallow_end and not self.depth_deep_end:
                return self.calculate_constant_depth_volumen()
            else:
                raise RuntimeError('Cannot calculate pool volume with current data')    
        else:
            raise RuntimeError('Cannot calculate pool volume with current data')
        
