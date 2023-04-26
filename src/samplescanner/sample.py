
class Sample:
    def __init__(self, filename:str, key:int, vel:int, loop_start:int=-1, loop_end:int=-1):
        self._filename= filename
        self._key = key
        self._vel = vel
        self._loop_start = loop_start
        self._loop_end = loop_end