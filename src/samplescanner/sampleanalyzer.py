import re
import logging

class SampleAnalyzer():

    # Base key mapping
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

    # Articulations
    ARTS_CENTER_VEL = {
        "softest": 0,
        "softer": 21,
        "soft": 42,
        "medium": 63,
        "hard": 84,
        "harder": 105,
        "hardest": 127,
        "ppp":8,
        "pp": 24,
        "p": 30,
        "mp": 56,
        "mf": 72,
        "f": 88,
        "ff": 104,
        "fff": 110
    }

    KEYS_REX = r'_([A-G][#b]?)(-?[0-9])[_\.]'
    ARTICULATION_REX= r'_((soft|hard)(est|er)?|medium|m[pf]|p{1,3}|f{1,3})[_\.]'
    FILENAME_REX = r'^(' \
                   r'[^_]+' \
                   r'(_([A-G][#b]?)(-?[0-9]))?' \
                   r'(_((soft|hard)(est|er)?|medium|m[pf]|p{1,3}|f{1,3}))?' \
                   r'.(wav|aif|flac|ogg|mp3)' \
                   r')$'

    logger = logging.getLogger("SampleAnalyzer")

    def __init__(self, filename:str):
        self.sample_filename = filename

    def _get_sample_key(self) -> int:
        m = re.search(self.KEYS_REX, self.sample_filename)
        pitch = 60
        if m is not None:
            keydef= m.group(1)
            octave= int(m.group(2))
            pitch= self.KEYS.get(keydef, 0) + 12*(octave+1)

        return pitch

    def _get_sample_vel(self):

        m = re.search(self.ARTICULATION_REX, self.sample_filename)
        velocity = 100
        if m is not None:
            veldef = m.group(1)
            velocity = self.ARTS_CENTER_VEL.get(veldef, 100)

        return velocity

    def analyze(self):
        if re.match(self.FILENAME_REX, string=self.sample_filename):

            return {
                "path": self.sample_filename,
                "key": self._get_sample_key(),
                "velocity": self._get_sample_vel(),
                "lovel": 0,
                "hivel": 127,
            }
        self.logger.info(f"File '{self.sample_filename}' does not meet filename requirements")
        return None
