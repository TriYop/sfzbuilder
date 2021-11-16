import re
import logging

class SampleAnalyzer():

    KEYS = {
        "C": 0 ,
        "C#": 1, "Db": 1,
        "D": 2,
        "D#": 3, "Eb": 3,
        "E": 4,
        "F": 5,
        "F#": 6, "Gb": 6,
        "G": 7,
        "G#": 8, "Ab": 8,
        "A": 9,
        "A#": 10, "Bb": 10,
        "B": 11,
    }

    logger = logging.getLogger("SampleAnalyzer")

    def __init__(self, filename:str):
        self.sample_filename = filename

    def _get_sample_key(self) -> int:
        m = re.search(r'_([A-G][#b]?)(-?[0-9])[_\.]', self.sample_filename)
        pitch = 60
        if m is not None:

            keydef= m.group(1)
            self.logger.info(keydef)
            self.logger.info(m.group(2))
            octave= int(m.group(2))
            pitch= self.KEYS.get(keydef, 0) + 12*(octave+1)

        return pitch

    def analyze(self):
        return {
            "path": self.sample_filename,
            "key": self._get_sample_key(),

        }
