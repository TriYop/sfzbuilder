from sforzando import Soundfont, Control, Group, Region
from samplescanner import DirectoryScanner, SAMPLE_FORMAT_OGG, SAMPLE_FORMAT_WAV, SAMPLE_FORMAT_MP3, SAMPLE_FORMAT_FLAC, SAMPLE_FORMAT_AIF
import os.path

"""

"""

def generate_soundfont_from_samples(samples:list) -> Soundfont:
    sf = Soundfont()

    ct = Control()
    ct.set_param("default_path", scan_path)
    sf.add_control(ct)

    gp = Group()

    for sample in samples:
        reg = Region()
        reg.set_param("sample", sample['path'])
        reg.set_param("lokey", sample['key'])
        reg.set_param("hikey", sample['key'])
        reg.set_param("pitch_keycenter", sample['key'])
        reg.set_param("lovel", 0)
        reg.set_param("hivel", 127)
        gp.add_region(reg)

    sf.set_param("volume", "0")
    sf.add_group(gp)
    return sf

def scan_dir_for_samples(scan_path:str) -> Soundfont:
    """Generates a sforzando soundfont from a directory"""
    ds = DirectoryScanner(scan_path)
    samples= ds.scan_for_samples([SAMPLE_FORMAT_OGG, SAMPLE_FORMAT_WAV, SAMPLE_FORMAT_MP3, SAMPLE_FORMAT_FLAC, SAMPLE_FORMAT_AIF])

    if samples is not None and len(samples)>0:
        return generate_soundfont_from_samples(samples)

    return None


if __name__ == '__main__':

    scan_path = "/home/yvan/SoundFonts/Samples a preparer/SoundBytes - Early Patches/PANFLUTE"
    sf = scan_dir_for_samples(scan_path)

    #if not os.path.exists(f"{scan_path}.sfz"):
    with open(f"{scan_path}.sfz", "w") as sfz:
        sfz.write(f"{sf}")

    print(sf)

