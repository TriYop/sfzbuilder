from sforzando import Soundfont, Control, Group, Region
from samplescanner import DirectoryScanner, SAMPLE_FORMAT_OGG, SAMPLE_FORMAT_WAV, SAMPLE_FORMAT_MP3, SAMPLE_FORMAT_FLAC, SAMPLE_FORMAT_AIF
import os.path
import argparse
import logging

"""

"""

def generate_soundfont_from_samples(samples:list) -> Soundfont:
    sf = Soundfont()

    ct = Control()
    ct.set_param("default_path", f"{os.path.basename(scan_path)}{os.path.sep}")
    sf.add_control(ct)

    gp = Group()

    for sample in samples:
        reg = Region()
        reg.set_param("sample", sample.get('path',""))
        reg.set_param("lokey", sample.get('key',60))
        reg.set_param("hikey", sample.get('key',60))
        reg.set_param("pitch_keycenter", sample.get('key',60))
        reg.set_param("lovel", sample.get('lovel',0))
        reg.set_param("hivel", sample.get('hivel',127))
        reg.set_param("volume", sample.get('volume', 6))
        gp.add_region(reg)

    sf.set_param("volume", "0")
    sf.set_param("ampeg_attack", "0.001")
    sf.set_param("ampeg_release", "0.15")
    sf.set_param("ampeg_dynamic", "1")


    sf.add_group(gp)
    return sf

def scan_dir_for_samples(scan_path:str) -> Soundfont:
    """Generates a sforzando soundfont from a directory"""
    logger.info(f"Starting scan for samples in {scan_path}")
    ds = DirectoryScanner(scan_path)
    samples= ds.scan_for_samples([SAMPLE_FORMAT_OGG, SAMPLE_FORMAT_WAV, SAMPLE_FORMAT_MP3, SAMPLE_FORMAT_FLAC, SAMPLE_FORMAT_AIF])

    if samples is not None and len(samples)>0:
        return generate_soundfont_from_samples(samples)

    return None

logger = logging.getLogger("folder2sfz")

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)


    parser = argparse.ArgumentParser(description="Builds a SFZ from a directory containing samples")
    parser.add_argument("path", type=str, nargs=1, help="path to the samples directory")

    args = parser.parse_args()
    scan_path = args.path[0]
    sf = scan_dir_for_samples(scan_path)

    #if not os.path.exists(f"{scan_path}.sfz"):
    with open(f"{scan_path}.sfz", "w") as sfz:
        sfz.write(f"{sf}")
