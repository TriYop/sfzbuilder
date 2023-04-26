import logging
import math
import os.path
import struct
import wave

from numpy import float32, int32, int16, uint8

from samplescanner.sampleanalyzer import SampleAnalyzer

PEAK_ANALYSIS_TIME = 15


class SignalSampleAnalyzer(SampleAnalyzer):
    logger = logging.getLogger("SignalSampleAnalyzer")

    def __init__(self):
        super(SignalSampleAnalyzer, self).__init__()

    def get_key(self, filename: str) -> int:
        pass

    def _get_envelope_peak(self, input_signal, interval_length):
        self.logger.debug("Getting peaks.")
        absolute_signal = []
        amplitudes = [max(input_signal[i:i + interval_length]) - min(input_signal[i:i + interval_length])
                      for i in range(0, len(input_signal) - interval_length, math.floor(interval_length / 2))]
        return max(amplitudes)

    def _get_velocity_from_float32(self, value: float32):
        pass

    def _get_velocity_from_int32(self, value: int32):
        pass

    def _get_velocity_from_int16(self, value: int16):
        return math.floor(8 * math.log(value, 2))

    def _get_velocity_from_int8(self, value: uint8):
        pass

    def _get_velocity_from_int(self, value: int, depth: int = 24):
        if value == 0:
            retval = 0
        else:
            retval = math.floor(127 / depth * (math.log(value, 2)))

        return retval
        # return math.floor(8 * math.log(value, 2))

    def _get_sampling_depth(self, sample):
        if isinstance(sample, float32):
            return self._get_velocity_from_float32
        if isinstance(sample, int32):
            return self._get_velocity_from_int32
        if isinstance(sample, int16):
            return self._get_velocity_from_int16
        if isinstance(sample, uint8):
            return self._get_velocity_from_int8
        if isinstance(sample, int):
            return self._get_velocity_from_int
        return None

    def load_wav(filename):
        with wave.open(filename, 'rb') as f:
            num_channels = f.getnchannels()
            sample_width = f.getsampwidth()
            num_frames = f.getnframes()
            sample_freq = f.getframerate()

            # Determine the format string for unpacking the raw binary data
            if sample_width == 1:
                fmt = f'{num_channels}B'
            elif sample_width == 2:
                fmt = f'{num_channels}h'
            elif sample_width == 3:
                fmt = f'{num_channels}i'
            else:
                raise ValueError('Unsupported sample width')

            # Read all data from WAV file
            raw_data = f.readframes(num_frames)

            # Unpack the raw binary data and convert to integers
            ints = []
            for i in range(0, len(raw_data), sample_width * num_channels):
                data = raw_data[i:i + sample_width * num_channels]
                vals = struct.unpack(fmt, data)
                ints.append(vals)

            # Transpose the data and convert to lists of integers
            channels = [[] for i in range(num_channels)]
            for vals in ints:
                for i, val in enumerate(vals):
                    channels[i].append(val)

            return channels, num_channels, num_frames, sample_freq, sample_width

    def load_wav24(filename):
        # ChatGPT Generated
        with wave.open(filename, 'rb') as f:
            num_channels = f.getnchannels()
            sample_width = f.getsampwidth()
            num_frames = f.getnframes()

            # Read all data from WAV file
            raw_data = f.readframes(num_frames)

            # Unpack the 24-bit data and convert to signed integers
            ints = []
            for i in range(0, len(raw_data), 3):
                b3, b2, b1 = raw_data[i:i + 3]
                val = (b1 << 8) | (b2 << 16) | (b3 << 24)
                if val >= 0x800000:
                    val -= 0x1000000
                ints.append(val)

            # Split the data into separate channels
            channels = [[] for i in range(num_channels)]
            for i, val in enumerate(ints):
                channels[i % num_channels].append(val)

            return channels

    def compute_loudness(self, filename):
        with wave.open(filename, 'rb') as f:
            num_channels = f.getnchannels()
            sample_width = f.getsampwidth()
            num_frames = f.getnframes()
            sample_rate = f.getframerate()

            # Determine the format string for unpacking the raw binary data
            if sample_width == 1:
                fmt = f'{num_channels}B'
            elif sample_width == 2:
                fmt = f'{num_channels}h'
            elif sample_width == 3:
                fmt = f'{num_channels}i'
            else:
                raise ValueError('Unsupported sample width')

            # Read all data from WAV file
            raw_data = f.readframes(num_frames)

            # Unpack the raw binary data and convert to integers
            ints = []
            for i in range(0, len(raw_data), sample_width * num_channels):
                data = raw_data[i:i + sample_width * num_channels]
                vals = struct.unpack(fmt, data)
                ints.append(vals)

            # Compute the RMS power for each channel
            rms_powers = []
            for i in range(num_channels):
                channel = [vals[i] for vals in ints]
                rms_power = math.sqrt(sum(val * val for val in channel) / len(channel))
                rms_powers.append(rms_power)

            # Compute the maximum loudness in decibels
            max_loudness = max(20 * math.log10(rms_power) for rms_power in rms_powers)

            return max_loudness

    def read_file(self, filename: str):
        # FIXME: get real value. It currently always finish with level = 126 ...
        fileabspath = os.path.abspath(filename)
        self.logger.info("Analyzing %s", fileabspath)

        with wave.open(fileabspath, 'rb') as wavefile:

            chans = wavefile.getnchannels()
            samples_count = wavefile.getnframes()
            sample_width = wavefile.getsampwidth()
            sample_freq = wavefile.getframerate()

            raw_samples = wavefile.readframes(samples_count)
            # self.logger.debug("Read sample data: %s", raw_samples )

            samples = [[] for chan in range(chans)]

            for sample_idx in range(samples_count):
                for chan in range(0, chans):
                    sample_start = sample_idx * chans * sample_width + chan * sample_width
                    sample_end = sample_idx * chans * sample_width + chan * sample_width + sample_width
                    samples[chan].append(int.from_bytes(raw_samples[sample_start:sample_end], 'little'))
                #    samples.append( [int.from_bytes(raw_samples[sample_start:sample_end], 'little') for sampleidx in raw_samples])

            # samples[chan][sample_n]
            assert len(samples[0]) == samples_count, "File wrongly loaded"

            # samples = [int.from_bytes(raw_samples[c:(c+3)], 'little') for c in range(0, 3 * chans, 3)]

        return samples, chans, samples_count, sample_freq, sample_width

    def get_vel(self, filename: str) -> int:
        fileabspath = os.path.abspath(filename)
        loudness = self.compute_loudness(fileabspath)
        # self.logger.info("=========================================================================================\n\n")
        # self.logger.info("Analyzing %s", fileabspath)
        self.logger.info(f"Found max loudness = {loudness}dB")
        return min(127, math.trunc(2 * loudness))
        # try:
        #     samples, channels, nsamples, sample_freq, sample_width = self.read_wav(fileabspath)
        #     self.logger.debug(
        #         f"File has {channels} channels at {sample_freq}Hz containing {nsamples} {sample_width * 8}bits samples")
        #     self.logger.debug(f"We have read {len(samples[0])} samples from {fileabspath}.")
        #
        #     # get_velocity_from_amplitude = self._get_sampling_depth(samples[0])
        #
        #     period = PEAK_ANALYSIS_TIME * sample_freq / 1000
        #     channel_peak = []
        #     for chan in range(channels):
        #         self.logger.debug(f"Analyzing channel {chan + 1} of {channels}")
        #         # channel_data = [smpl[chan] for smpl in samples]
        #         # channel_peak.append(self._get_envelope_peak(channel_data, math.floor(period)))
        #         channel_peak.append(self._get_envelope_peak(samples[chan], math.floor(period)))
        #
        #     self.logger.debug(f'Identified peaks: {channel_peak}')
        #
        #     return self._get_velocity_from_int(max(channel_peak), 8 * sample_width)
        #     # return get_velocity_from_amplitude(max(channel_peak))
        #
        # except Exception as e:
        #     self.logger.error("%s", e)
        #
        #     return 128

    def find_loop_points(self, filename: str) -> (int, int):
        """ Identify potential loop points for sample
        :param filename:
        :return: a tuple containing start and end points
        """
        return (-1, -1)
