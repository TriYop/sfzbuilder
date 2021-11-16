from os import scandir
from . import SampleAnalyzer


class DirectoryScanner():
    def __init__(self, directory_path):
        self.path = directory_path

    def scan_for_samples(self, formats:list) -> list:
        samples= list()
        with scandir(path=self.path) as it:
            for entry in it:
                if entry.is_file() :
                    # and len(entry.name)>3 and  entry.name[-3:] in formats
                    samples.append(SampleAnalyzer(entry.name).analyze())
        print(samples)
        return samples
