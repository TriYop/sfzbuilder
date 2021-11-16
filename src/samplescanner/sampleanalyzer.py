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

    def __init__(self, filename:str):
        self.sample_filename = filename

    def _get_sample_key(self) -> int:
        # split sample name to determin sample pitch
        pass

    def analyze(self):
        return {
            "path": self.sample_filename,
            "key": self._get_sample_key(),

        }
