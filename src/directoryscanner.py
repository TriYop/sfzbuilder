import logging
import os.path
from os import scandir
from samplescanner import *



class DirectoryScanner():
    logger = logging.getLogger("DirectoryScanner")
    SUPPORTED_SAMPLES_FORMAT = ['.wav', '.aiff', '.flac', '.mp3', ".ogg"]
    def __init__(self, directory_path, analyzers:SampleAnalyzerChain):
        self.path = directory_path
        self.analyzers= analyzers


    def is_sample_file(self, file_name):
        ext = os.path.splitext(file_name)[1]
        self.logger.debug(f"File extension: {ext}")
        return ext in self.SUPPORTED_SAMPLES_FORMAT

    def scan_for_samples(self, formats:list) -> list:
        samples= list()
        with scandir(path=self.path) as it:
            for entry in it:
                if entry.is_file() and self.is_sample_file(entry.name) :
                    samples.append(self.analyzers.analyze(entry.path))
        self.logger.debug(f"Found {len(samples)} samples in '{self.path}'")
        return samples
