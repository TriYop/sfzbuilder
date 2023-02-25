from os import scandir
from samplescanner import *



class DirectoryScanner():
    def __init__(self, directory_path, analyzers:SampleAnalyzerChain):
        self.path = directory_path
        self.analyzers= analyzers


    def scan_for_samples(self, formats:list) -> list:
        samples= list()
        with scandir(path=self.path) as it:
            for entry in it:
                if entry.is_file() :
                    samples.append(self.analyzers.analyze(entry.path))
        return samples
