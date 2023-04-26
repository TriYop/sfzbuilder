import logging

from . import SampleAnalyzer, Sample, AnalyzerException


class SampleAnalyzerChain:
    logger = logging.getLogger(__name__)

    def __init__(self, looping: bool = False):
        self._chain = []
        self._looping = looping

    def _get_key(self, filename: str):
        for analyzer in self._chain:
            key = None
            try:
                self.logger.debug(f"Trying to get key with {analyzer.__class__}")
                key = analyzer.get_key(filename)
            except AnalyzerException as ex:
                self.logger.warning(ex)
            if key is not None:
                self.logger.debug(f"identified key: {key}")
                return key

    def _get_vel(self, filename: str):
        for analyzer in self._chain:
            vel = None
            try:
                self.logger.debug(f"Trying to get vel with {analyzer.__class__}")
                vel = analyzer.get_vel(filename)
            except AnalyzerException as ex:
                self.logger.warning(ex)
            if vel is not None and vel < 128 and vel >= 0:
                self.logger.debug(f"identified vel: {vel}")
                return vel
        return 60

    def _get_looppoints(self, filename: str):
        for analyzer in self._chain:
            start = -1
            end = -1
            try:
                self.logger.debug(f"Trying to get looping points with {analyzer.__class__.__name__}")
                (start, end) = analyzer.find_loop_points(filename)
            except AnalyzerException as ex:
                self.logger.warning(ex)
            if start >= 0 and end >= start:
                self.logger.debug(f"identified loop: ({start},{end})")
                return (start, end)
        return (-1, -1)

    def append_analyzer(self, analyzer: SampleAnalyzer):
        self._chain.append(analyzer)

    def analyze(self, filename: str) -> Sample:
        self.logger.debug(f"Analyzing {filename}")
        key = self._get_key(filename)
        vel = self._get_vel(filename)
        self.logger.debug(f"Found sample in '{filename}' for key {key} with velocity {vel}")
        # Find loop points only if  required
        if self._looping:
            (lstart, lend) = self._get_looppoints(filename=filename)
            return Sample(filename=filename, key=key, vel=vel, loop_start=lstart, loop_end=lend)
        else:
            return Sample(filename=filename, key=key, vel=vel)
