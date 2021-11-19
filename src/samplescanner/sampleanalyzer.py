"""SFZBuilder
---
Sample filename analyzer
"""
import re
import logging


class SampleAnalyzer():
    """Analyzes a sample file"""

    # Base key mapping that will be complimented with octave definition
    KEYS = {
        "C": 0,
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

    # Articulations mapping to velocity
    ARTS_CENTER_VEL = {
        "softest": 0,
        "softer": 21,
        "soft": 42,
        "medium": 63,
        "hard": 84,
        "harder": 105,
        "hardest": 127,
        "ppp": 8,
        "pp": 24,
        "p": 30,
        "mp": 56,
        "mf": 72,
        "f": 88,
        "ff": 104,
        "fff": 110
    }

    # Base sample name
    SAMPLE_NAME_REX = r'[^_]+'
    # Sample key
    KEYS_REX = r'([A-G][#b]?)(-?[0-9])'
    # Sample articulation
    ARTICULATION_REX = r'((soft|hard)(est|er)?|medium|m[pf]|p{1,3}|f{1,3})'
    # Samples if drums (TODO: enhance drums list)
    DRUM_REX = r'(kicka|kickb|kick|snarea|snareb|snare|hihatc|hihatf|hihato|tom[1-6]|crash1|crash2|ride1|ride2)'
    # Sample allowed file extension
    SAMPLE_TYPE_REX = r'\.(wav|aif|flac|ogg|mp3)'
    # sample filename field separator (we do not only support _ (underscore) but also . (dot) and - (dash).
    FIELD_SEPARATOR_REX = r'[_\.\-]'
    # Filename may be composed of at least one sample and contain much fields.
    FILENAME_REX = rf'^{SAMPLE_NAME_REX}(({FIELD_SEPARATOR_REX}({KEYS_REX}|{ARTICULATION_REX}|{DRUM_REX}))+' \
                   rf'{SAMPLE_TYPE_REX})$'

    logger = logging.getLogger("SampleAnalyzer")

    def __init__(self, filename: str):
        """Initialize analyzer
            :param filename the sample file name (without full path)
        """
        self.sample_filename = filename

    def _get_sample_key(self) -> int:
        """Get sample key from filename.
        We are using REGEX patterns for this rather than direct matching
        """
        rex = rf'{self.FIELD_SEPARATOR_REX}{self.KEYS_REX}{self.FIELD_SEPARATOR_REX}'
        m = re.search(rex, self.sample_filename)
        pitch = 60
        if m is not None:
            keydef = m.group(1)
            octave = int(m.group(2))
            pitch = self.KEYS.get(keydef, 0) + 12 * (octave + 1)

        return pitch

    def _get_sample_vel(self):
        """Get sample velocity from filename.
        We are using REGEX patterns for this rather than direct matching
        """
        rex = rf'{self.FIELD_SEPARATOR_REX}{self.ARTICULATION_REX}{self.FIELD_SEPARATOR_REX}'
        m = re.search(rex, self.sample_filename)
        velocity = 100
        if m is not None:
            veldef = m.group(1)
            velocity = self.ARTS_CENTER_VEL.get(veldef, 100)

        return velocity

    def analyze(self):
        """Launches analysis of the sample file"""
        # TODO: use only sample velocity here and apply velocity range in the soundbank (actual mapping will depend on
        #  the different available velocities).
        if re.match(self.FILENAME_REX, string=self.sample_filename):
            return {
                "path": self.sample_filename,
                "key": self._get_sample_key(),
                "velocity": self._get_sample_vel(),
            }
        self.logger.info(f"File '{self.sample_filename}' does not meet filename requirements")
        return None
