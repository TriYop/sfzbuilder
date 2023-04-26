import logging
import re

from . import SampleAnalyzer, PitchNotDeterminedException, AnalyzerException


class NamingSampleAnalyzer(SampleAnalyzer):
    KEYS = {
        "C": 0, "B#": 0, "do": 0, "Do": 0,
        "C#": 1, "Db": 1, "#C": 1, "do#": 1, "Do#": 1, "reb": 1, "Reb": 1, "réb": 1, "Réb": 1,
        "D": 2, "re": 2, "Re": 2, "ré": 2, "Ré": 2,
        "D#": 3, "Eb": 3, "#D": 3, "mib": 3, "Mib": 3, "re#": 3, "Re#": 3, "ré#": 3, "#Ré#": 3,
        "E": 4, "Fb": 4, "mi": 4, 'Mi': 4,
        "F": 5, "E#": 5, "fa": 5, "Fa": 5,
        "F#": 6, "Gb": 6, "#F": 6, "fa#": 6, "Fa#": 6, "solb": 6, "Solb": 6,
        "G": 7, "sol": 7, "Sol": 7,
        "G#": 8, "Ab": 8, "#G": 8, "sol#": 8, "Sol#": 8, "lab": 8, "Lab": 8,
        "A": 9, "la": 9, "La": 9,
        "A#": 10, "Bb": 10, "#A": 10, "la#": 10, "La#": 10, "sib": 10, "Sib": 10,
        "B": 11, "Cb": 11, "si": 11, "Si": 11
    }

    VELOCITIES = {
        'fff': 120,
        'ff': 104,
        'f': 88,
        'mf': 72,
        'mp': 56,
        'p': 40,
        'pp': 24,
        'ppp': 8
    }

    # Sample pitch patterns
    PITCH_PATTERN_AMERICAN = r'[_ \-]?(#?[A-G][#b]?)(-?[0-9])[_\.\- ]'
    PITCH_PATTERN_FRENCH = r'[_ \-]?(#?(do|re|mi|fa|sol|la|si))[#b]?)(-?[0-9])[_\.\- ]'
    PITCH_PATTERN_MIDINOTE = r'^0?(\d{2})-.*$'

    # Sample velocity pattern
    VELS = "|".join(VELOCITIES.keys())
    VEL_PATTERN = r'[_\.\- ](' + VELS + r')[_\.\- ]'

    DEFAULT_PITCH = 60

    logger = logging.getLogger(__name__)

    def __init__(self):
        super(NamingSampleAnalyzer, self).__init__()

    def get_key(self, filename: str) -> int:
        """check for sample key in filename
        :param filename:
        :return:
        """
        pitch = self.DEFAULT_PITCH

        m = re.search(self.PITCH_PATTERN_AMERICAN, filename)
        if m is not None:
            keydef = m.group(1)
            octave = int(m.group(2))
            pitch = self.KEYS.get(keydef, 0) + 12 * (octave + 1)
            return pitch

        m = re.search(self.PITCH_PATTERN_FRENCH, filename)
        if m is not None:
            keydef = m.group(1)
            octave = int(m.group(2))
            pitch = self.KEYS.get(keydef, 0) + 12 * (octave + 1)
            return pitch

        # check if sample key in filename
        m = re.search(self.PITCH_PATTERN_MIDINOTE, filename)
        if m is not None:
            pitch = int(m.group(1))
            return pitch

        raise PitchNotDeterminedException()

    def get_vel(self, filename: str) -> int:
        """check for sample velocity as nuance (p, mf, ff, ...) format.
        :param filename:
        :return:
        """
        m = re.search(self.VEL_PATTERN, filename)
        if m is not None:
            veldef = m.group(1)
            velocity = self.KEYS.get(veldef, 0)
        else:
            raise AnalyzerException()
        return velocity

    def find_loop_points(self, filename: str) -> (int, int):
        """ Identify potential loop points for sample
        :param filename:
        :return: a tuple containing start and end points
        """
        return (-1, -1)
