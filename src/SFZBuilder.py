"""SFZBuilder
---
Main application entry point.
"""
from sforzando import Soundfont, Control, Group, Region
from samplescanner import DirectoryScanner
import os.path
import argparse
import logging

def generate_soundfont_from_samples(samples: list) -> Soundfont:
    """Generate the soundbank from the provided samples definition
      :param samples the list of samples
    """
    sf = Soundfont()

    ct = Control()
    ct.set_param("default_path", f"{os.path.basename(scan_path)}{os.path.sep}")
    sf.add_control(ct)

    gp = Group()
    for sample in samples:
        # Sets sample guessed parameters or default ones
        reg = Region()
        reg.set_param("sample", sample.get('path', ""))
        reg.set_param("lokey", sample.get('key', 60))
        reg.set_param("hikey", sample.get('key', 60))
        reg.set_param("pitch_keycenter", sample.get('key', 60))
        reg.set_param("lovel", sample.get('lovel', 0))
        reg.set_param("hivel", sample.get('hivel', 127))
        reg.set_param("volume", sample.get('volume', 6))
        gp.add_region(reg)

    sf.set_param("volume", "0")
    sf.set_param("ampeg_attack", "0.001")
    sf.set_param("ampeg_release", "0.15")
    sf.set_param("ampeg_dynamic", "1")

    sf.add_group(gp)
    return sf


def scan_dir_for_samples(scan_path: str, mode: str = "melodic", velocity: bool = True) -> Soundfont:
    """Retrieve sample informations from a given directory.
      :param scan_path the directory to scan
      :param mode the scan mode (drum vs pitch)
      :param velocity manage sample velocity or bypass it
    """
    logger.info(f"Starting scan for samples in {scan_path}")
    ds = DirectoryScanner(scan_path)
    samples = ds.scan_for_samples()

    if samples is not None and len(samples) > 0:
        return generate_soundfont_from_samples(samples)

    return None


logger = logging.getLogger("folder2sfz")

if __name__ == '__main__':
    """
     Here is the main entry point.
    """
    logging.basicConfig(level=logging.INFO)

    parser = argparse.ArgumentParser(description="Builds a SFZ from a directory containing samples")
    parser.add_argument("path", type=str, nargs=1, help="path to the samples directory")
    mode_group = parser.add_mutually_exclusive_group()
    mode_group.add_argument("-m", dest='mode', action='store_const', const='melodic', help="sets parse mode to melodic")
    mode_group.add_argument("-d", dest='mode', action='store_const', const='drumset', default="melodic",
                            help="sets parse mode to drumset")
    parser.add_argument("-v", dest='velocity', action='store_true', help="activates multiple velocities per note")

    args = parser.parse_args()
    scan_path = args.path[0]
    mode = args.mode
    sf = scan_dir_for_samples(scan_path, mode=mode, velocity=args.velocity)

    # as of now, let's overwrite without prompt any existing sfz soundbank definition
    # if not os.path.exists(f"{scan_path}.sfz"):
    with open(f"{scan_path}.sfz", "w") as sfz:
        sfz.write(f"{sf}")
