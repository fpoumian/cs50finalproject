from lib.pool.pool import Pool

class RectangularPool(Pool):

    def __init__(self, **kwargs: float) -> None:
        super().__init__(**kwargs)
        self.length = kwargs['length']
        self.width = kwargs['width']

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