class Pool:

    def __init__(self, **kwargs) -> None:
        self.volume = kwargs['volume']
        self.depth_swallow_end = kwargs['depth_swallow_end']
        self.depth_deep_end = kwargs['depth_deep_end']


    @classmethod
    def generate(cls, **kwargs: float):
        return cls(**kwargs)
    
    @property
    def volume(self) -> float:
        return self._volume
    
    @volume.setter
    def volume(self, volume: float) -> None:
        self._volume = volume

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
