from . import SampleAnalyzer, Sample, AnalyzerException

import logging
class SampleAnalyzerChain:
    logger = logging.getLogger(__name__)
    def __init__(self):
        self._chain= []

    def _get_key(self, filename:str):
        for analyzer in self._chain:
            key = None
            try:
                self.logger.debug(f"Trying to get key with {analyzer.__class__}")
                key= analyzer.get_key(filename)
            except AnalyzerException as ex:
                self.logger.info(ex)
            if key is not None:
                self.logger.debug(f"identified key: {key}")
                return key


    def _get_vel(self, filename:str):
        for analyzer in self._chain:
            vel = None
            try:
                self.logger.debug(f"Trying to get vel with {analyzer.__class__}")
                vel= analyzer.get_vel(filename)
            except AnalyzerException as ex:
                self.logger.info(ex)
            if vel is not None:
                self.logger.info(f"identified vel: {vel}")
                return vel
        return 60


    def append_analyzer(self, analyzer: SampleAnalyzer):
        self._chain.append(analyzer)

    def analyze(self, filename:str) -> Sample:
        key = self._get_key(filename)
        vel = self._get_vel(filename)
        return Sample(filename=filename, key=key, vel=vel)


