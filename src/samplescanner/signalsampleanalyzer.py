import logging
import re
import math
from . import SampleAnalyzer, PitchNotDeterminedException, AnalyzerException
from scipy.io import wavfile
from numpy import float32, int32, int16, uint8

PEAK_ANALYSIS_TIME = 15

class SignalSampleAnalyzer(SampleAnalyzer):
    logger = logging.getLogger(__name__)

    def __init__(self):
        super(SignalSampleAnalyzer, self).__init__()

    def get_key(self, filename: str) -> int:
        pass


    def _get_envelope_peak(self, input_signal, interval_length):
        absolute_signal = []
        amplitudes = [max(input_signal[i:i+interval_length]) - min(input_signal[i:i+interval_length]) for i in range(0, len(input_signal) - interval_length, math.floor(interval_length/2))]
        return max (amplitudes)

    def _get_velocity_from_float32(self, value:float32):
        pass

    def _get_velocity_from_int32(self, value:int32):
        pass

    def _get_velocity_from_int16(self, value:int16):
        return math.floor(8*math.log(value, 2))

    def _get_velocity_from_int8(self, value:uint8):
        pass

    def _get_sampling_depth(self, sample):
        if isinstance(sample, float32):
            return self._get_velocity_from_float32
        if isinstance(sample, int32):
            return self._get_velocity_from_int32
        if isinstance(sample, int16):
            return self._get_velocity_from_int16
        if isinstance(sample, uint8):
            return self._get_velocity_from_int8
        return None

    def get_vel(self, filename: str) -> int:
        self.logger.info("Analyzing %s", filename)
        w = wavfile.read(filename)
        sampling_freq = w[0]
        samples = w[1]
        get_velocity_from_amplitude = self._get_sampling_depth(samples[0][0])
        channels = len(samples[0])
        nsamples = len(samples)
        self.logger.debug(f"File has {channels} channels at {sampling_freq}Hz containing {nsamples} samples")
        period = PEAK_ANALYSIS_TIME * sampling_freq / 1000
        channel_peak = []
        for x in range(channels):
            self.logger.debug(f"Analyzing channel {x} of {channels}")
            channel_data = [i[x] for i in samples]
            channel_peak.append(self._get_envelope_peak(channel_data, math.floor(period)))
        self.logger.debug(f'Identified peaks: {channel_peak}')

        return get_velocity_from_amplitude(max(channel_peak))

