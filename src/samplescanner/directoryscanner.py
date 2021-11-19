"""SFZBuilder
---
Directory sample scanner
"""
from os import scandir
from . import SampleAnalyzer


class DirectoryScanner():
    """Scans a directory for samples"""

    def __init__(self, directory_path):
        """Initialize directory scanner"""
        self.path = directory_path

    def scan_for_samples(self) -> list:
        """Scans the directory for files (single level, no subdirectory scans) and launches analysis of found files."""
        samples= list()
        with scandir(path=self.path) as it:
            for entry in it:
                if entry.is_file() :
                    # and len(entry.name)>3 and  entry.name[-3:] in formats
                    smpl_info= SampleAnalyzer(entry.name).analyze()
                    if smpl_info is not None:
                        samples.append(smpl_info)
        return samples
